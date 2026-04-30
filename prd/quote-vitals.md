# Quote Vitals

**Owner:**
**Status:** Draft
**Last updated:** 2026-04-30

---

## 1. Problem

CloudSign already tracks the engagement signal that best predicts deal close — view count correlates with an 80% close rate at 3+ views, and correctly predicts the winning quote in 7/7 multi-quote deals (`findings/quote-behavior.md` L18-19, L54). But the Quotations table buries this data behind a per-quote "View activity" popover click, and reps have largely stopped clicking it.

The scan-level view — where reps triage 30+ active deals during stand-ups and pipeline reviews — shows only a single-word stage label (Online / Viewed / Offline) that collapses all engagement into one term. "Viewed" covers everything from a single accidental open to seven deliberate reads. "Offline" means both "not sent via CloudSign" and "sent but tracking failed" — even experienced reps can't agree on the definition (`findings/quote-tracking-finding.md` L46-49, Zendesk TKT-004).

Usage data confirms the popover has failed as a delivery mechanism: reps click "View activity" 0.35 times per quote globally, and junior reps (≤10 months tenure) click just 0.15 times — effectively never (`findings/quote-behavior.md` L106-107). Senior reps who do check frequently supplement with personal spreadsheets because the data they find is unreliable (`findings/quote-tracking-finding.md` L74-77, Planhat account-002). Junior reps take the panel at face value and delay follow-ups, producing the lowest win rates on the team (44% vs 64% for seniors, `findings/quote-behavior.md` L127-128).

The result: the most predictive signal in the product — repeated quote views — exists in the system but is invisible at the level where reps actually work.

## 2. Users

**Primary: Sales managers running pipeline reviews.** Team leads and heads of sales ops who scan across 30+ deals in a stand-up or weekly pipeline review. They need to triage quickly — which deals are hot, which quotes are getting attention, where should the team focus. Today they can't do this without opening individual popovers on individual quotes on individual deals. James Hartley, a Head of Sales Operations managing 30+ active deals, explicitly described the missing columns: "a Views column, a Last Opened column, and icons for downloads/feedback" — framed around team workflows, not individual convenience (`findings/quote-tracking-finding.md` L55-58, Zendesk TKT-008).

**Secondary: All reps who send quotes and follow up.** The inline data helps individual reps too — particularly junior reps (≤10 months tenure) who click the activity panel the least (0.15 times per quote), trust it the most when they do, and have the lowest win rate (44% vs 64% for seniors). But the primary job-to-be-done is the manager scanning across deals, not the rep working a single deal (`findings/quote-behavior.md` L127-128).

**Job-to-be-done:** During a pipeline review, look at the Quotations table and instantly answer: *Which quotes are being actively engaged with? Which ones have gone cold? In multi-quote deals, which option is the buyer leaning toward?*

## 3. Success — what changes in the world

**Direct success metric:** Reduction in "View activity" popover clicks per quote. If the inline columns deliver the signal reps need at the scan level, the popover becomes a detail drill-down rather than the primary path to engagement data. A drop in click rate means the table is doing its job.

**Baseline (where we are today):**
- 0.35 "View activity" clicks per quote globally (`findings/quote-behavior.md` L106)
- 0.15 clicks per quote for junior reps (≤10 months tenure, `findings/quote-behavior.md` L128)
- 0.53 clicks per quote for senior reps (`findings/quote-behavior.md` L128)
- 23% of NorthPath reps click View Activity more than once a week, despite 89% using deal management weekly (`findings/quote-tracking-finding.md` L130-131)

**Target:** Popover clicks drop while deal-page engagement stays flat or rises — reps are still working the deal page, they're just getting the signal from the table instead of the popover. If popover clicks drop but deal-page time also drops, the feature isn't delivering value — reps are skipping over it.

**Indirect / leading indicators:**
- Junior rep click rate converges toward senior rep rate (the gap should narrow because the table carries the signal juniors weren't getting from the popover)
- Qualitative signal from CS and sales managers: fewer complaints about "Offline" confusion, fewer reps maintaining parallel spreadsheets
- Support ticket volume related to CloudSign tracking confusion (baseline: TKT-004, TKT-007 type tickets)

**Time horizon:** 4-6 weeks post-launch for click behavior to stabilize. Qualitative signal (spreadsheet abandonment, CS feedback) within one quarter.

## 4. The decision — what we're building (and not building)

**We are building:** Inline CloudSign engagement data on the Quotations table — starting with two new columns (Views and Last Opened) on the deal page, positioned after Amount. This moves the most predictive engagement signal from behind a popover to the scan level where reps and managers actually triage deals.

**We are not building:** A CloudSign sync reliability fix. The tracking data has known false negatives ("Offline" on quotes that were actually viewed — device/browser-dependent, unpredictable). We're shipping against this imperfect sync. The bet: a visible wrong number is more useful than a correct number hidden behind a popover nobody clicks, and the visibility creates measurable pressure to fix the sync as a separate initiative (`findings/solution-direction.md` L115).

**Trade-offs we're making:**
- Accepting imperfect data in exchange for shipping faster. Some view counts will be wrong (underreported). This is already the case today — the popover shows the same wrong data — but making it inline makes it more visible.
- Adding two columns to an already dense table. This trades horizontal space for information density. The stage label (Online/Viewed/Offline) is removed to partially offset the width increase.
- Not building sorting, filtering, or visual heat encoding. The raw numbers carry the signal — 4 views vs 0 views is obvious without color coding. These can be added later if the numbers alone aren't enough.

**Why this approach over the alternatives we considered:**
- *Redesigned popover* — still requires a click. Doesn't solve the scan-level problem.
- *Sidebar panel* — adds a new UI surface; more engineering and design work for something that could live in the existing table.
- *Badges/chips on the title column* — saves table width but mixes metadata with the quote name. Harder to scan across rows.
- *Fix sync first, then surface data* — gates the value on a backend investigation with unclear timeline. The IA problem is independent of the sync problem and can ship first.

## 5. The MVP line

**MVP includes:**
- Views column on the Quotations table (integer count, dash for offline/untracked)
- Last Opened column on the Quotations table (relative timestamp, dash for never-viewed)
- Removal of the stage label (Online/Viewed/Offline) from its current position next to "View activity"
- "View activity" link and popover retained as detail drill-down (unchanged)
- Both columns read from the existing CloudSign event data path — no new backend data source

**Non-goals (explicitly out of v1):**
- **Other surfaces.** v1 is the Quotations table on the deal page only. Not the deal list view, not the pipeline board, not a dashboard widget. We validate the table works before expanding to other surfaces. This is the line most likely to be challenged — stakeholders will ask "can we show this on the pipeline board too?" The answer is: after v1 ships and we see whether inline data changes triage behavior.
- **Visual encoding / thresholds.** No color-coding, no badges, no green-for-hot/grey-for-cold. The raw numbers carry the signal. Color coding requires threshold decisions (is 3 the cutoff? 5?), accessibility testing, and design iteration. If the numbers alone aren't enough, we add encoding in a fast follow.
- **Sortable columns.** No clicking the Views header to sort. Useful for deals with many quotes, but adds interaction design scope. Defer.
- **CloudSign sync reliability fix.** Known false negatives exist (iPad, mobile, Firefox). v1 ships against the current sync. The sync fix is a separate backend initiative.
- **Download/feedback inline indicators.** These are strong signals (85.7% and 83.3% close rate) but rare (7 and 6 events out of 54 viewed quotes). They stay in the popover for v1.
- **Per-recipient tracking.** Out of scope entirely — CloudSign uses a single shared URL, so this requires a product change upstream (`findings/cloudsign-capabilities.md` L79-80).

**Definition of done:**
- [ ] Views and Last Opened columns visible on the Quotations table for all deals with at least one quote
- [ ] Stage label (Online/Viewed/Offline) no longer appears next to "View activity"
- [ ] View count matches the count shown in the existing CloudSign activity popover (same data source)
- [ ] Offline/untracked quotes display a dash, not a zero
- [ ] "View activity" popover continues to function as before

## 6. Risks and assumptions

| Assumption | Evidence (or "assumption only") | What would flip our position |
|---|---|---|
| Reps stopped clicking the popover because the signal is behind a click (discoverability), not because the data is unreliable | **Mixed evidence.** Usage data shows juniors barely click (0.15/quote) while seniors click 3.5x more (0.53/quote) — consistent with a discoverability problem. But seniors who click most also maintain shadow spreadsheets (`findings/quote-tracking-finding.md` L74-77), suggesting distrust compounds the discoverability issue. | If we ship inline numbers and click behavior doesn't change — reps still ignore the data — then distrust is the root cause, not IA, and the sync fix becomes the prerequisite. We'd know within 4-6 weeks from popover click rates and qualitative feedback. |
| View count is predictive enough to drive rep behavior without visual encoding | **Strong evidence.** 80% close rate at 3+ views vs 33% at 0-1 (`findings/quote-behavior.md` L18-19). 7/7 winner prediction in multi-quote deals. Maaike explicitly asked for "a simple view count" (`findings/quote-tracking-finding.md` L33-34). | If reps report they can't quickly distinguish hot from cold quotes using raw numbers alone, we add visual encoding (color/badges at the 3+ threshold) as a fast follow. |
| The table can absorb two new columns without layout degradation | **Assumption only.** No evidence on how the table renders on small screens or with long quote titles. Deals with 5-10 quotes already strain the page (`findings/quote-tracking-finding.md` L61, TKT-006: 15+ second load times). | If design review or QA finds the table overflows on common screen sizes, we consider a compact single-column format (e.g., "4x · 2h ago") or responsive hiding of Last Opened on narrow viewports. |
| Shipping visible wrong numbers is better than hidden correct ones | **Assumption with supporting logic.** The same wrong data already shows in the popover — we're not making it wronger. Making it visible creates concrete bug reports ("this says 0 but I know they viewed it") vs vague complaints ("the tracking doesn't work"). | If CS ticket volume about wrong view counts spikes post-launch and outweighs the triage value, we'd need to gate the columns behind a sync fix or add a "data may be incomplete" indicator. |

## 7. Cross-functional impact

| Team | Impact | Owner | Looped in? |
|---|---|---|---|
| Sales leadership | **Primary concern.** Sales managers and team leads get a new pipeline triage signal. They need to understand: (1) what view count means and what the 3+ threshold implies for close probability, (2) known limitations — the sync sometimes undercounts, no per-recipient tracking, view = anyone who opened the URL including the rep themselves, (3) how to coach reps on using view count as one signal among many, not a single source of truth. Anneke de Vries at NorthPath is onboarding 12 new Brussels reps — this lands during that ramp. | | |
| CS / Support | The stage label (Online/Viewed/Offline) is being removed. CS agents need to know what replaced it and how the new columns work. Risk: if visible wrong counts increase "my view count is wrong" tickets, CS needs a playbook. Mitigation: the same wrong data was already in the popover — the failure mode isn't new, just more visible. | | |
| Engineering | The new columns read from the same CloudSign event data path that feeds the popover. Key questions for eng: (1) can this data be fetched at the table level without per-row calls? (2) what's the performance impact on deals with 10+ quotes, given existing load time concerns (TKT-006: 15+ seconds)? (3) is the data path the popover uses already part of the quotation list response, or does it require an additional fetch? | | |
| Marketing | Minimal impact. No customer-facing messaging needed unless this is positioned as a product update. Could be a lightweight release note. | | |
| Legal / Privacy | No new data collection. CloudSign already tracks views — we're surfacing existing data in a new location. No privacy or compliance change. | | |

## 8. Rollout

**Launch sequence:**
1. **Internal dogfood** — enable for Teamleader internal accounts. Validate that view counts match the popover data, table renders cleanly on real deals with varying quote counts, and no performance regression on deals with 10+ quotes.
2. **Mid-market cohort** — roll to a cohort of mid-market customers where multi-quote deals are most common. These are the users where the triage value is highest and where we'll get the strongest signal on whether inline data changes behavior. Monitor popover click rates and qualitative feedback.
3. **GA** — enable for all accounts. Coordinate with CS on the stage label removal (what replaced "Online/Viewed/Offline" and how to explain it) and sales leadership on coaching guidance.

**Rollback story:** Feature flag controls whether the Views and Last Opened columns appear and whether the stage label is shown. Rollback = flip the flag. The popover and all existing functionality are untouched, so rollback restores the exact previous experience with no data loss.

**Day-one monitoring:**
- Popover click rate (Amplitude: `cloudsign_activity_clicked` per quote) — expecting a drop, which is success
- Deal page load time — watching for performance regression from fetching view counts at the table level, especially on deals with 10+ quotes
- CS ticket volume mentioning "views," "view count," or "tracking" — watching for confusion about the new columns or spike in wrong-count reports
- Qualitative: reach out to 3-5 sales managers in the mid-market cohort after one week for direct feedback on pipeline review workflow

---

## Appendix: end-to-end walk

**Scenario: Lena, sales manager, coaches a rep on a multi-quote deal during a Tuesday pipeline review.**

Lena opens the deal page for "Renovatie kantoorpand" — a mid-market deal where her rep Jonas sent three quote options last week: a full-service package, a reduced scope, and a phased approach.

**What she sees on the Quotations table:**

```
Title              | Amount     | Views | Last opened | View calculation | Status
Full service       | €24.500,00 |   5   | 1h ago      | View calc        | Sent
Reduced scope      | €18.000,00 |   1   | 4d ago      | View calc        | Sent
Phased approach    | €21.200,00 |   0   | —           | View calc        | Sent
```

**What she decides in three seconds:** The buyer is engaging with the full-service package — 5 views, most recently an hour ago. The reduced scope got a single look four days ago. The phased approach has never been opened. Before Quote Vitals, Lena would have seen three identical "Sent" statuses and three "View activity" links — no signal without clicking each one.

**She clicks "View activity" on the full-service quote** to check the detail. The popover opens and shows five individual view timestamps spread across the past week, plus a download event yesterday. She doesn't need the popover to know this quote is hot — the "5" in the Views column already told her that — but the download event confirms the buyer is in decision mode.

**She coaches Jonas:** "The buyer's on the full-service package — 5 views and a download. Don't pitch the phased approach, they haven't even opened it. Call today and ask if they have questions on the full-service option."

**The messy part:** What if the phased approach actually was viewed on the buyer's iPad, but CloudSign didn't register it? The Views column shows 0. Jonas calls and the buyer says "Actually, I liked the phased approach — I read it last night." Jonas sees 0 views and is confused. This is the same failure that happens today (the popover would also show no activity), but now it's more visible — which means Jonas can report "the view count on Quote C is wrong" as a concrete bug, not a vague "the tracking doesn't work."

**What's different from today:** Without Quote Vitals, Lena's pipeline review of this deal would go: open deal → see three quotes, all "Sent" → click "View activity" on each one → wait for each popover → mentally compare the timestamps → decide. With Quote Vitals: open deal → see 5/1/0 → decide. The popover still exists for the drill-down, but the scan-level triage happens in the table.

## 9. Engineering clarifications (from /eng-review)

**Data path:** Where do the new columns get their data?
- **Resolved:** CloudSign engagement data is already included in the quotation list response that renders the table. The columns surface fields that are already there — primarily a frontend change.
- **Implication:** No new backend endpoints or data fetching needed. Frontend reads view count and last-viewed timestamp from the existing response payload. Eng should verify the exact field names and shape before starting.

**Zero vs dash semantics:** What does the Views column show for quotes with no views vs quotes not tracked by CloudSign?
- **Resolved:** `0` means "trackable but no views yet" (quote was sent via CloudSign). `—` means "not trackable" (quote not sent via CloudSign, or offline). The distinction tells the rep whether tracking is active.
- **Implication:** Frontend needs to check the CloudSign tracking status to decide between rendering `0` or `—`. The mock at L133-135 already reflects this: `0 | —` for sent-but-unviewed, `— | — offline` for untracked.

**Self-views:** View count includes rep self-views (reps clicking their own CloudSign link). Should these be filtered?
- **Resolved:** Acknowledged as a limitation, not filtered in v1. CloudSign doesn't track who viewed — just that the URL was opened — so filtering isn't possible without upstream changes.
- **Implication:** No engineering work needed. The limitation should be communicated to sales leadership during rollout coaching (see §7, Sales leadership row).

**Mobile scope:** Does the Quotations table exist in the Teamleader iOS/Android apps?
- **Resolved:** Unknown — needs eng to verify before committing to mobile scope. If the table exists on mobile, two extra columns on a narrow screen may require responsive handling.
- **Implication:** Eng spike needed: check whether the native apps render the Quotations table. If yes, decide whether to hide the new columns on mobile or adapt the layout. If no, add "native mobile apps" to the non-goals list (§5).

