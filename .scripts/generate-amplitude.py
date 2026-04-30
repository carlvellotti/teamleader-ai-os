#!/usr/bin/env python3
"""
Generate engineered synthetic Amplitude-style event-level data for CloudSign
quote engagement analysis.

Story: "Valuable signal, wrong surface"
  - CloudSign tracks rich buyer engagement (views, downloads, feedback)
  - But reps rarely check "View activity" (popover on deal page)
  - Senior reps check it more -> close more deals
  - High-engagement quotes (3+ views, downloads, feedback) close at dramatically
    higher rates — but most reps never see this signal

Target distributions:
  - 10 reps, ~55-60 unique quotes across ~35-40 deals
  - ~300-400 total event rows
  - 5 senior reps (tenure 18+ months): click View activity on ~60% of quotes,
    close rate ~65-70%
  - 5 junior reps (tenure <12 months): click View activity on ~15% of quotes,
    close rate ~40-45%
  - Quotes with 3+ views close at ~75%+
  - Quotes with 1 view close at ~35%
  - Quotes with 0 views close at ~20%
  - Quotes with downloads close at ~80%+
  - Quotes with feedback close at ~85%+
  - ~30% of deals have 2-3 quotes; the most-viewed quote converts
"""
import csv
import random
import uuid
from datetime import datetime, timedelta
from pathlib import Path

random.seed(99)

# ── Rep definitions ──────────────────────────────────────────────────────────
REPS = [
    # Senior reps (tenure >= 18 months)
    {"id": "user_001", "name": "Sara van den Berg",  "region": "NL", "tenure": 24, "senior": True},
    {"id": "user_002", "name": "David O'Connor",     "region": "UK", "tenure": 36, "senior": True},
    {"id": "user_003", "name": "Maaike de Vries",    "region": "NL", "tenure": 20, "senior": True},
    {"id": "user_004", "name": "Eric Larsson",       "region": "DE", "tenure": 48, "senior": True},
    {"id": "user_005", "name": "Mark Devos",         "region": "BE", "tenure": 30, "senior": True},
    # Junior reps (tenure < 12 months)
    {"id": "user_006", "name": "Pieter Janssens",    "region": "BE", "tenure": 8,  "senior": False},
    {"id": "user_007", "name": "Lisa Hofmann",       "region": "FR", "tenure": 6,  "senior": False},
    {"id": "user_008", "name": "Anna Smit",          "region": "NL", "tenure": 4,  "senior": False},
    {"id": "user_009", "name": "Tom Bakker",         "region": "UK", "tenure": 10, "senior": False},
    {"id": "user_010", "name": "Sofia Klein",        "region": "DE", "tenure": 7,  "senior": False},
]

SENIOR_REPS = [r for r in REPS if r["senior"]]
JUNIOR_REPS = [r for r in REPS if not r["senior"]]

ACCOUNT_SIZE_DIST = [("smb", 0.50), ("mid", 0.35), ("enterprise", 0.15)]

# Date range: Jan 5 2026 – Apr 20 2026
DATE_START = datetime(2026, 1, 5)
DATE_END = datetime(2026, 4, 20)
DATE_RANGE_DAYS = (DATE_END - DATE_START).days


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


def random_date_in_range():
    offset = random.randint(0, DATE_RANGE_DAYS - 30)
    return DATE_START + timedelta(days=offset)


def make_event_id():
    return str(uuid.uuid4())[:12]


# ── Build deals with DETERMINISTIC engagement profiles ───────────────────────
#
# Instead of rolling dice and hoping the distributions land, we explicitly
# define how many deals of each engagement tier each rep group gets, then
# shuffle to feel organic.

# Engagement tiers for a deal's "best quote":
#   tier_0: 0 views          → close ~20%
#   tier_1: 1 view           → close ~35%
#   tier_2: 2 views          → close ~50% (transitional)
#   tier_3: 3+ views         → close ~75%
#   tier_dl: 3+ views + DL   → close ~82%
#   tier_fb: 3+ views + FB   → close ~88%

# Senior reps: 5 deals each = 25 deals total.  Target close rate ~68%.
# Tier distribution for ALL senior deals combined:
SENIOR_TIERS = (
    [("tier_0", False)] * 2 +
    [("tier_1", True)]  * 1 + [("tier_1", False)] * 2 +
    [("tier_2", True)]  * 1 + [("tier_2", False)] * 2 +
    [("tier_3", True)]  * 6 + [("tier_3", False)] * 2 +
    [("tier_dl", True)] * 4 + [("tier_dl", False)] * 1 +
    [("tier_fb", True)] * 4
)
# = 25 deals, 16 won = 64%

# Junior reps: 5 deals each = 25 deals total.  Target close rate ~40-44%.
# Junior deals skew toward lower engagement.
JUNIOR_TIERS = (
    [("tier_0", True)]  * 1 + [("tier_0", False)] * 4 +
    [("tier_1", True)]  * 2 + [("tier_1", False)] * 5 +
    [("tier_2", True)]  * 2 + [("tier_2", False)] * 3 +
    [("tier_3", True)]  * 3 + [("tier_3", False)] * 1 +
    [("tier_dl", True)] * 2 +
    [("tier_fb", True)] * 1 + [("tier_fb", False)] * 1
)
# = 25 deals, 11 won = 44%

random.shuffle(SENIOR_TIERS)
random.shuffle(JUNIOR_TIERS)


def assign_views(tier):
    """Return view count for the best quote in a deal based on its tier."""
    if tier == "tier_0":
        return 0
    elif tier == "tier_1":
        return 1
    elif tier == "tier_2":
        return 2
    elif tier in ("tier_3", "tier_dl", "tier_fb"):
        return random.randint(3, 8)
    return 0


# Decide which deals are multi-quote (~30% of total = ~15 deals)
# We'll pick 8 from senior, 7 from junior
MULTI_QUOTE_SENIOR = set(random.sample(range(25), 8))
MULTI_QUOTE_JUNIOR = set(random.sample(range(25), 7))

deals = []
quotes = []
deal_counter = 1
quote_counter = 1


def build_deals(rep_list, tiers, multi_quote_set, deals_per_rep=4):
    global deal_counter, quote_counter
    tier_idx = 0
    for rep in rep_list:
        for d in range(deals_per_rep):
            deal_id = f"deal_{deal_counter:03d}"
            deal_counter += 1

            tier, won = tiers[tier_idx]
            overall_idx = tier_idx
            tier_idx += 1

            is_multi = overall_idx in multi_quote_set
            n_quotes = random.choice([2, 3]) if is_multi else 1

            size = pick_account_size()
            base_value = quote_value(size)
            sent_date = random_date_in_range()

            best_views = assign_views(tier)
            has_dl = tier == "tier_dl"
            has_fb = tier == "tier_fb"

            deal_quotes = []
            for q_idx in range(n_quotes):
                qid = f"Q-{quote_counter:04d}"
                quote_counter += 1

                q_sent_date = sent_date + timedelta(days=q_idx * random.randint(2, 7))
                q_value = base_value + random.randint(-500, 500) if n_quotes > 1 else base_value
                q_value = max(q_value, 1000)

                # Last quote in multi-quote deal gets the best engagement
                is_best_quote = (q_idx == n_quotes - 1)

                if is_best_quote:
                    n_views = best_views
                    q_dl = has_dl
                    q_fb = has_fb
                else:
                    # Non-best quotes: low engagement
                    n_views = random.choice([0, 0, 1, 1, 1, 2])
                    q_dl = False
                    q_fb = False

                n_downloads = 0
                if q_dl:
                    n_downloads = random.choice([1, 1, 2, 2])

                # Rep clicked "View activity"?
                if rep["senior"]:
                    clicked = random.random() < 0.60
                else:
                    clicked = random.random() < 0.10

                deal_quotes.append({
                    "quote_id": qid,
                    "deal_id": deal_id,
                    "rep": rep,
                    "account_size": size,
                    "quote_value_eur": q_value,
                    "sent_date": q_sent_date,
                    "n_views": n_views,
                    "has_download": q_dl,
                    "n_downloads": n_downloads,
                    "has_feedback": q_fb,
                    "clicked_activity": clicked,
                    "is_won_quote": won and is_best_quote,
                })

            deal_obj = {
                "deal_id": deal_id,
                "rep": rep,
                "quotes": deal_quotes,
                "account_size": size,
                "won": won,
                "tier": tier,
            }
            deals.append(deal_obj)
            quotes.extend(deal_quotes)


build_deals(SENIOR_REPS, SENIOR_TIERS, MULTI_QUOTE_SENIOR, deals_per_rep=5)
build_deals(JUNIOR_REPS, JUNIOR_TIERS, MULTI_QUOTE_JUNIOR, deals_per_rep=5)

# ── Post-process: fix junior "View activity" clicks to be exactly ~15% ──────
# The random approach gives too much variance with small per-rep samples.
# Instead: each junior rep clicks on exactly 1 of their quotes (~14-18%).
for rep in JUNIOR_REPS:
    rep_quotes = [q for q in quotes if q["rep"]["id"] == rep["id"]]
    # Reset all clicks for this rep
    for q in rep_quotes:
        q["clicked_activity"] = False
    # Pick exactly 1 quote to click on (prefer one with views, for realism)
    viewed_quotes = [q for q in rep_quotes if q["n_views"] > 0]
    pick_from = viewed_quotes if viewed_quotes else rep_quotes
    chosen = random.choice(pick_from)
    chosen["clicked_activity"] = True


# ── Generate event rows ─────────────────────────────────────────────────────

events = []

for q in quotes:
    rep = q["rep"]
    sent_date = q["sent_date"]

    # 1. quote_sent event
    events.append({
        "event_id": make_event_id(),
        "event_type": "quote_sent",
        "timestamp": sent_date.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": rep["id"],
        "user_name": rep["name"],
        "user_tenure_months": rep["tenure"],
        "user_region": rep["region"],
        "quote_id": q["quote_id"],
        "deal_id": q["deal_id"],
        "account_size": q["account_size"],
        "quote_value_eur": q["quote_value_eur"],
    })

    # 2. quote_viewed events (buyer)
    view_base = sent_date + timedelta(hours=random.randint(2, 48))
    for v in range(q["n_views"]):
        view_ts = view_base + timedelta(
            hours=random.randint(0, 24 * (v + 1)),
            minutes=random.randint(0, 59)
        )
        events.append({
            "event_id": make_event_id(),
            "event_type": "quote_viewed",
            "timestamp": view_ts.strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": "buyer",
            "user_name": "buyer",
            "user_tenure_months": "",
            "user_region": "",
            "quote_id": q["quote_id"],
            "deal_id": q["deal_id"],
            "account_size": q["account_size"],
            "quote_value_eur": q["quote_value_eur"],
        })

    # 3. quote_downloaded events
    if q["has_download"]:
        for d in range(q["n_downloads"]):
            dl_ts = view_base + timedelta(
                hours=random.randint(6, 96),
                minutes=random.randint(0, 59)
            )
            events.append({
                "event_id": make_event_id(),
                "event_type": "quote_downloaded",
                "timestamp": dl_ts.strftime("%Y-%m-%d %H:%M:%S"),
                "user_id": "buyer",
                "user_name": "buyer",
                "user_tenure_months": "",
                "user_region": "",
                "quote_id": q["quote_id"],
                "deal_id": q["deal_id"],
                "account_size": q["account_size"],
                "quote_value_eur": q["quote_value_eur"],
            })

    # 4. quote_feedback_sent
    if q["has_feedback"]:
        fb_ts = view_base + timedelta(
            hours=random.randint(24, 120),
            minutes=random.randint(0, 59)
        )
        events.append({
            "event_id": make_event_id(),
            "event_type": "quote_feedback_sent",
            "timestamp": fb_ts.strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": "buyer",
            "user_name": "buyer",
            "user_tenure_months": "",
            "user_region": "",
            "quote_id": q["quote_id"],
            "deal_id": q["deal_id"],
            "account_size": q["account_size"],
            "quote_value_eur": q["quote_value_eur"],
        })

    # 5. cloudsign_activity_clicked (rep)
    if q["clicked_activity"]:
        click_ts = sent_date + timedelta(
            hours=random.randint(12, 168),
            minutes=random.randint(0, 59)
        )
        events.append({
            "event_id": make_event_id(),
            "event_type": "cloudsign_activity_clicked",
            "timestamp": click_ts.strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": rep["id"],
            "user_name": rep["name"],
            "user_tenure_months": rep["tenure"],
            "user_region": rep["region"],
            "quote_id": q["quote_id"],
            "deal_id": q["deal_id"],
            "account_size": q["account_size"],
            "quote_value_eur": q["quote_value_eur"],
        })

    # 6. deal_won
    if q.get("is_won_quote"):
        last_event_offset = max(q["n_views"] * 24 + 48, 72)
        won_ts = sent_date + timedelta(
            hours=last_event_offset + random.randint(24, 168),
            minutes=random.randint(0, 59)
        )
        events.append({
            "event_id": make_event_id(),
            "event_type": "deal_won",
            "timestamp": won_ts.strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": rep["id"],
            "user_name": rep["name"],
            "user_tenure_months": rep["tenure"],
            "user_region": rep["region"],
            "quote_id": q["quote_id"],
            "deal_id": q["deal_id"],
            "account_size": q["account_size"],
            "quote_value_eur": q["quote_value_eur"],
        })

# Sort all events by timestamp
events.sort(key=lambda e: e["timestamp"])


# ── Write CSV ────────────────────────────────────────────────────────────────

FIELDNAMES = [
    "event_id", "event_type", "timestamp", "user_id", "user_name",
    "user_tenure_months", "user_region", "quote_id", "deal_id",
    "account_size", "quote_value_eur"
]


def write_csv(events, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(events)


# ── Summary / verification ──────────────────────────────────────────────────

def summary():
    """Print key distributions for verification."""
    print("=" * 65)
    print("AMPLITUDE EVENT DATA — DISTRIBUTION SUMMARY")
    print("=" * 65)

    print(f"\nTotal events: {len(events)}")
    print(f"Unique quotes: {len(quotes)}")
    print(f"Unique deals: {len(deals)}")

    by_type = {}
    for e in events:
        by_type[e["event_type"]] = by_type.get(e["event_type"], 0) + 1
    print(f"\nEvent type breakdown:")
    for et in ["quote_sent", "quote_viewed", "quote_downloaded",
               "quote_feedback_sent", "cloudsign_activity_clicked", "deal_won"]:
        print(f"  {et}: {by_type.get(et, 0)}")

    multi_quote_deals = [d for d in deals if len(d["quotes"]) > 1]
    print(f"\nMulti-quote deals: {len(multi_quote_deals)}/{len(deals)} "
          f"({len(multi_quote_deals)/len(deals):.0%})")

    # ── Senior vs junior ─────────────────────────────────────────────────
    senior_deals = [d for d in deals if d["rep"]["senior"]]
    junior_deals = [d for d in deals if not d["rep"]["senior"]]

    senior_won = sum(1 for d in senior_deals if d["won"])
    junior_won = sum(1 for d in junior_deals if d["won"])

    sr_rate = senior_won / len(senior_deals) if senior_deals else 0
    jr_rate = junior_won / len(junior_deals) if junior_deals else 0

    print(f"\n── REP SENIORITY ──")
    print(f"Senior reps (18+ mo): {senior_won}/{len(senior_deals)} deals won "
          f"({sr_rate:.0%})")
    print(f"Junior reps (<12 mo): {junior_won}/{len(junior_deals)} deals won "
          f"({jr_rate:.0%})")

    senior_quotes = [q for q in quotes if q["rep"]["senior"]]
    junior_quotes = [q for q in quotes if not q["rep"]["senior"]]
    sr_clicked = sum(1 for q in senior_quotes if q["clicked_activity"])
    jr_clicked = sum(1 for q in junior_quotes if q["clicked_activity"])

    print(f"Senior 'View activity' click rate: {sr_clicked}/{len(senior_quotes)} "
          f"({sr_clicked/len(senior_quotes):.0%})")
    print(f"Junior 'View activity' click rate: {jr_clicked}/{len(junior_quotes)} "
          f"({jr_clicked/len(junior_quotes):.0%})")

    print(f"\n── PER-REP BREAKDOWN ──")
    for rep in REPS:
        rep_deals = [d for d in deals if d["rep"]["id"] == rep["id"]]
        rep_quotes_list = [q for q in quotes if q["rep"]["id"] == rep["id"]]
        rep_won = sum(1 for d in rep_deals if d["won"])
        rep_clicked = sum(1 for q in rep_quotes_list if q["clicked_activity"])
        seniority = "SR" if rep["senior"] else "JR"
        print(f"  {rep['name']:22s} ({seniority}, {rep['tenure']:2d}mo): "
              f"{rep_won}/{len(rep_deals)} won, "
              f"{rep_clicked}/{len(rep_quotes_list)} activity clicks")

    # ── Engagement → close rate (deal-level) ─────────────────────────────
    print(f"\n── ENGAGEMENT → CLOSE RATE (deal-level, by best quote views) ──")

    def deal_best_views(deal):
        return max(q["n_views"] for q in deal["quotes"])

    def deal_has_dl(deal):
        return any(q["has_download"] for q in deal["quotes"])

    def deal_has_fb(deal):
        return any(q["has_feedback"] for q in deal["quotes"])

    zero_view_deals = [d for d in deals if deal_best_views(d) == 0]
    one_view_deals = [d for d in deals if deal_best_views(d) == 1]
    two_view_deals = [d for d in deals if deal_best_views(d) == 2]
    three_plus_deals = [d for d in deals if deal_best_views(d) >= 3]

    for label, group in [("0 views", zero_view_deals), ("1 view", one_view_deals),
                         ("2 views", two_view_deals), ("3+ views", three_plus_deals)]:
        won = sum(1 for d in group if d["won"])
        rate = won / len(group) if group else 0
        print(f"  {label:10s}: {won}/{len(group)} won ({rate:.0%})")

    dl_deals = [d for d in deals if deal_has_dl(d)]
    dl_won = sum(1 for d in dl_deals if d["won"])
    dl_rate = dl_won / len(dl_deals) if dl_deals else 0
    print(f"  {'downloads':10s}: {dl_won}/{len(dl_deals)} won ({dl_rate:.0%})")

    fb_deals = [d for d in deals if deal_has_fb(d)]
    fb_won = sum(1 for d in fb_deals if d["won"])
    fb_rate = fb_won / len(fb_deals) if fb_deals else 0
    print(f"  {'feedback':10s}: {fb_won}/{len(fb_deals)} won ({fb_rate:.0%})")

    # Multi-quote: does the most-viewed quote win?
    print(f"\n── MULTI-QUOTE DEALS ──")
    multi_won = [d for d in multi_quote_deals if d["won"]]
    if multi_won:
        most_viewed_won = 0
        for d in multi_won:
            best_q = max(d["quotes"], key=lambda q: q["n_views"])
            if best_q.get("is_won_quote"):
                most_viewed_won += 1
        print(f"  Won multi-quote deals: {len(multi_won)}")
        print(f"  Most-viewed quote was winner: {most_viewed_won}/{len(multi_won)} "
              f"({most_viewed_won/len(multi_won):.0%})")
    else:
        print("  No won multi-quote deals")

    timestamps = [e["timestamp"] for e in events]
    print(f"\n── DATE RANGE ──")
    print(f"  First event: {min(timestamps)}")
    print(f"  Last event:  {max(timestamps)}")

    print(f"\n{'=' * 65}")


if __name__ == "__main__":
    import sys
    here = Path(__file__).resolve().parent.parent
    out = here / "data" / "amplitude" / "quote-events.csv"
    if "--summary-only" not in sys.argv:
        write_csv(events, out)
        print(f"Wrote {len(events)} events to {out}\n")
    summary()
