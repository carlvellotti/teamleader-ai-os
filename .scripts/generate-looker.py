#!/usr/bin/env python3
"""
Generate engineered synthetic Looker quote-engagement data.

Target distributions:
  - 100 rows, 10 reps × 10 quotes each
  - 5 high-clicker reps (click on >50% of quotes), close at ~70%
  - 5 low-clicker reps (click on <20% of quotes), close at ~45%
  - ~30% of "offline"-labeled rows have cloudsign engagement events (false-offline rate)
"""
import csv
import random
from pathlib import Path

random.seed(42)

# Each rep gets explicit allocations (deterministic, balanced).
# n_signed = quotes that close
# n_clicked = quotes the rep clicked "View activity" on
REPS = [
    {"id": "rep_001", "name": "Sara van den Berg",  "region": "NL", "tenure": 24, "n_signed": 5, "n_clicked": 7, "high_clicker": True},
    {"id": "rep_002", "name": "Pieter Janssens",    "region": "BE", "tenure": 8,  "n_signed": 2, "n_clicked": 2, "high_clicker": False},
    {"id": "rep_003", "name": "David O'Connor",     "region": "UK", "tenure": 36, "n_signed": 6, "n_clicked": 8, "high_clicker": True},
    {"id": "rep_004", "name": "Maaike de Vries",    "region": "NL", "tenure": 12, "n_signed": 5, "n_clicked": 6, "high_clicker": True},
    {"id": "rep_005", "name": "Eric Larsson",       "region": "DE", "tenure": 48, "n_signed": 5, "n_clicked": 7, "high_clicker": True},
    {"id": "rep_006", "name": "Lisa Hofmann",       "region": "FR", "tenure": 18, "n_signed": 3, "n_clicked": 2, "high_clicker": False},
    {"id": "rep_007", "name": "Anna Smit",          "region": "NL", "tenure": 4,  "n_signed": 2, "n_clicked": 1, "high_clicker": False},
    {"id": "rep_008", "name": "Mark Devos",         "region": "BE", "tenure": 30, "n_signed": 5, "n_clicked": 6, "high_clicker": True},
    {"id": "rep_009", "name": "Sofia Klein",        "region": "DE", "tenure": 14, "n_signed": 3, "n_clicked": 2, "high_clicker": False},
    {"id": "rep_010", "name": "Tom Bakker",         "region": "UK", "tenure": 6,  "n_signed": 2, "n_clicked": 2, "high_clicker": False},
]

ACCOUNT_SIZE_DIST = [("smb", 0.50), ("mid", 0.35), ("enterprise", 0.15)]


def pick_account_size():
    r = random.random()
    cum = 0
    for size, p in ACCOUNT_SIZE_DIST:
        cum += p
        if r < cum:
            return size
    return "smb"


def quote_value(size):
    if size == "smb":
        return random.randint(2000, 12000)
    if size == "mid":
        return random.randint(15000, 60000)
    return random.randint(80000, 250000)


def date_in_q1_q2():
    month = random.choice(["01", "02", "03", "04"])
    day = random.randint(1, 28)
    return f"2026-{month}-{day:02d}"


rows = []
quote_id = 1

for rep in REPS:
    # 10 quotes per rep. Allocate which are signed and which are clicked.
    quote_indices = list(range(10))

    signed_indices = set(random.sample(quote_indices, rep["n_signed"]))

    # Clicked indices should overlap heavily with signed (clicking correlates with closing).
    # 70% of clicked quotes are also signed.
    clicked_pool_signed = list(signed_indices)
    random.shuffle(clicked_pool_signed)
    n_clicked_from_signed = min(rep["n_clicked"], int(0.7 * rep["n_clicked"]) + 1)
    clicked_from_signed = clicked_pool_signed[:n_clicked_from_signed]
    remaining_click_slots = rep["n_clicked"] - len(clicked_from_signed)
    unsigned_indices = [i for i in quote_indices if i not in signed_indices]
    random.shuffle(unsigned_indices)
    clicked_from_unsigned = unsigned_indices[:remaining_click_slots]
    clicked_indices = set(clicked_from_signed + clicked_from_unsigned)

    for i in quote_indices:
        size = pick_account_size()
        account_id = f"acc_{random.randint(1000, 9999):04d}"
        signed = i in signed_indices
        clicked = i in clicked_indices
        click_count = (
            random.choices([1, 2, 3, 4, 5], [0.35, 0.30, 0.20, 0.10, 0.05])[0]
            if clicked else 0
        )

        # Cloudsign event: real customer engagement.
        # Signed quotes always have cloudsign signal (signed event).
        # Of unsigned: ~45% had real engagement (opened/viewed_long), rest none.
        if signed:
            cloudsign_event = "signed"
        elif random.random() < 0.45:
            cloudsign_event = random.choice(["opened", "viewed_long"])
        else:
            cloudsign_event = "none"

        # UI status:
        # - signed → "opened" (UI catches up after signature)
        # - cloudsign opened/viewed_long → ~50% show "offline" anyway (the bug) — false-offline rate
        # - cloudsign none → mostly "offline" (correctly), some "online"
        if cloudsign_event == "signed":
            ui_status = "opened"
        elif cloudsign_event in ("opened", "viewed_long"):
            ui_status = "offline" if random.random() < 0.50 else random.choice(["opened", "online"])
        else:
            ui_status = "offline" if random.random() < 0.85 else "online"

        time_to_signed = random.randint(3, 21) if signed else ""

        rows.append({
            "quote_id": f"Q-{quote_id:04d}",
            "rep_id": rep["id"],
            "rep_name": rep["name"],
            "rep_tenure_months": rep["tenure"],
            "region": rep["region"],
            "account_id": account_id,
            "account_size": size,
            "quote_value_eur": quote_value(size),
            "quote_sent_at": date_in_q1_q2(),
            "view_activity_click_count": click_count,
            "view_activity_clicked": clicked,
            "ui_status_shown": ui_status,
            "cloudsign_event": cloudsign_event,
            "quote_signed": signed,
            "time_to_signed_days": time_to_signed,
        })
        quote_id += 1


def write_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summary(rows):
    high = [r for r in rows if any(rep["id"] == r["rep_id"] and rep["high_clicker"] for rep in REPS)]
    low = [r for r in rows if any(rep["id"] == r["rep_id"] and not rep["high_clicker"] for rep in REPS)]

    def close_rate(group):
        return sum(1 for r in group if r["quote_signed"]) / len(group) if group else 0

    high_close = close_rate(high)
    low_close = close_rate(low)

    offline = [r for r in rows if r["ui_status_shown"] == "offline"]
    false_offline = [r for r in offline if r["cloudsign_event"] in ("opened", "viewed_long")]

    print(f"Total rows: {len(rows)}")
    print(f"High-clicker close rate: {high_close:.1%} ({sum(1 for r in high if r['quote_signed'])}/{len(high)})")
    print(f"Low-clicker close rate:  {low_close:.1%} ({sum(1 for r in low if r['quote_signed'])}/{len(low)})")
    print(f"Gap: {(high_close - low_close)*100:.1f}pp")
    print(f"Total 'offline' rows: {len(offline)}")
    print(f"False-offline rows: {len(false_offline)} ({len(false_offline)/len(offline):.1%} of offline rows)")


if __name__ == "__main__":
    here = Path(__file__).resolve().parent.parent
    out = here / "data" / "looker" / "quote-engagement.csv"
    write_csv(rows, out)
    print(f"Wrote {out}")
    summary(rows)
