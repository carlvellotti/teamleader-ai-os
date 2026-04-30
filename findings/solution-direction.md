# Solution Direction: Inline Engagement Data on the Quotations Table

Date: 2026-04-30
Status: Direction decided, not yet spec'd
Inputs: `findings/quote-tracking-finding.md`, `findings/cloudsign-capabilities.md`, deal page screenshot

---

## The Problem

CloudSign tracks engagement data that strongly predicts deal close — view count alone moves from 33% close rate (0-1 views) to 80% (3+ views) and correctly predicts the winning quote in 7/7 multi-quote deals. But this data is buried behind a per-quote "View activity" popover that reps have largely stopped clicking (0.35 clicks per quote globally, 0.15 for junior reps). The scan-level Quotations table shows only a stage label (Online/Viewed/Offline) that collapses all engagement into a single word and is distrusted because of sync failures.

Reps triage 30+ deals in stand-ups. They need engagement signal at the scan level — not behind a click.

---

## The Proposed Change

Add two new columns to the Quotations table on the deal page, positioned after Amount:

| Column | Content | Format |
|--------|---------|--------|
| **Views** | Total view count from CloudSign | Integer (e.g., `4`). Dash (`—`) for offline/untracked quotes. |
| **Last opened** | Timestamp of most recent view | Relative time (e.g., `2h ago`, `3d ago`). Dash for never-viewed. |

The table layout becomes:

```
Title          | Amount     | Views | Last opened | View calculation | Status
Design         | €18.200,99 |   4   | 2h ago      | View calc        | Accepted
Development    | €15.300,00 |   1   | 3d ago      | View calc        | Sent
Product mgmt   | €10.600,00 |   0   | —           | View calc        | Sent
Spike research | €15.300,00 |   2   | 1d ago      | View calc        | Sent
Spike research | €15.300,00 |   —   | — offline   | View calc        | Open
```

### What stays

- **"View activity" link and popover** — stays as the detail drill-down. Clicking it still opens the full CloudSign activity timeline (each view timestamp, download events, feedback, signature status). The popover becomes the "show me everything" view; the columns are the "show me what matters" view.

### What goes

- **The stage label** (Online/Viewed/Offline) next to "View activity" — removed. The Views and Last opened columns carry this information more precisely. A view count of `4` says more than "Viewed"; a dash with "offline" says the same thing without the ambiguity.

### Workflow change

A rep scanning the Quotations table can now:
1. **Spot hot quotes instantly** — a view count of 4+ jumps out without clicking anything
2. **Spot stale quotes** — "Last opened: 12d ago" on a quote with 3 views means a warm lead went cold
3. **Triage multi-quote deals** — in a deal with 3 options, the one with 5 views vs 1 view is the one the buyer is considering
4. **Do all of this during a stand-up** without opening popovers or switching context

No sorting, filtering, or visual heat encoding in v1. The numbers speak for themselves.

---

## Which CloudSign Data Gets Surfaced and How

### In the new columns (scan level)

| Data point | Source | Notes |
|------------|--------|-------|
| View count | CloudSign event log → deal page sync | Integer count of URL opens |
| Last view timestamp | CloudSign event log → deal page sync | Most recent view, displayed as relative time |

### In the existing popover (detail level, unchanged)

| Data point | Already there today |
|------------|-------------------|
| Full view timeline with timestamps | Yes |
| Download events | Yes |
| Feedback events | Yes |
| Signature status and timestamp | Yes |

### Not surfaced (not available in CloudSign)

| Data point | Why not |
|------------|---------|
| Per-recipient attribution | CloudSign uses a single shared URL — no way to attribute views to individual stakeholders |
| Dwell time / scroll depth | CloudSign document viewer doesn't instrument this |
| Device / browser info | Not tracked by CloudSign |

---

## What's In v1 vs Later

### v1 (this spec)

- Two new columns: Views (integer) and Last opened (relative timestamp)
- Remove the stage label (Online/Viewed/Offline) from its current position
- Keep the "View activity" popover as-is for detail drill-down
- Ship against the current CloudSign sync, accepting known imperfections

### Later (not blocked, not promised)

- **Sync reliability fix** — investigate and fix the CloudSign → deal page event sync that causes "Offline" false negatives on iPad, mobile, and Firefox. v1 creates visibility into the problem (wrong counts are more noticeable than wrong labels) which creates pressure to fix it.
- **Real-time notifications** — push alerts when a buyer opens a quote. Would require new webhook events in the API (currently zero quotation webhook events exist in the API).
- **New API endpoints** — exposing CloudSign engagement data programmatically. Would unlock Zapier/Make triggers, dashboards, and third-party integrations. The API currently has quotation CRUD but no engagement data endpoints.
- **Dwell time / scroll depth** — would require instrumenting the CloudSign document viewer. Different engineering surface entirely.
- **Download/feedback icons** — small inline indicators for downloads (85.7% close) and feedback (83.3% close). Rare events but strong signals. Could be added to the table row without new columns.
- **Sortable columns** — clicking the Views header to sort quotes by engagement. Useful for deals with many quotes.

### Explicitly out of scope

- **Per-recipient tracking** — CloudSign generates one URL per quote. Attributing views to specific stakeholders would require a product change upstream (unique URLs per recipient). This is a different problem with a different engineering surface and is walled off from this spec.

---

## Technical Constraints That Affect the Approach

### The sync problem

CloudSign records engagement events in its own event store. These events are supposed to propagate to the deal page activity panel, but the sync frequently fails — producing "Offline" false negatives where quotes that were viewed, downloaded, or even signed show no engagement on the deal page. The failure is device/browser-dependent (iPad, mobile, Firefox with privacy extensions) but unpredictable.

**v1 ships against this imperfect sync.** The bet: a visible wrong number (view count of 0 on a viewed quote) is better than a correct number hidden behind a popover nobody clicks. The visibility also makes the sync problem more measurable — when reps report "this says 0 views but I know they opened it," that's a concrete bug report, not a vague "the tracking doesn't work."

### No API for engagement data

The Teamleader API has zero quotation-level webhook events — not even `quotation.created`. The CloudSign engagement data (views, downloads, feedback) is not available through any API endpoint. The `events.*` endpoints return calendar events (meetings, calls, tasks), not CloudSign activity.

This means the new columns must read from the same internal data path that currently feeds the popover. No new backend data source is needed for v1, but the data path is the one with the sync reliability issue.

### Shared URL model

CloudSign generates a single URL per quote. When one quote from a deal is sent via CloudSign, all online quotes from that deal become available through the same link — the customer can toggle between them. This means:
- View counts are per-quote (the toggle still tracks which quote was viewed)
- But there's no per-recipient breakdown possible
- A "view" means "someone opened this quote's URL" — could be the intended recipient, a forwarded colleague, or the rep themselves checking the link

---

## Decision Log

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Primary metric | View count + last opened | View count is the strongest close predictor (80% at 3+). Last opened adds recency context. Downloads/feedback are rare and better left in the popover. |
| Placement | New dedicated columns after Amount | Structured and scannable. Dedicated columns are clearer than replacing the stage label or tucking badges after the title. |
| Existing UI | Keep popover, remove stage label | The popover is still the right place for the full timeline. The stage label (Online/Viewed/Offline) is redundant with the new columns and distrusted by reps. |
| Workflow | Triage at a glance (no sorting/heat) | Let the raw numbers do the work. 3+ views is obviously different from 0 without color coding. Sorting and visual encoding can come later if needed. |
| Sync dependency | Ship UI first, accept imperfection | The sync problem exists today — it just hides behind the popover. Surfacing counts makes the problem visible and measurable, creating pressure to fix it. Gating on a sync fix delays the value. |
| Out of scope | Per-recipient tracking only | The shared URL model makes per-recipient tracking a fundamentally different problem. Everything else (notifications, API, dwell time) is deferred but not walled off. |

---

## Sources

- `findings/quote-tracking-finding.md` — the research finding this solution addresses
- `findings/cloudsign-capabilities.md` — CloudSign capability inventory
- `findings/quote-behavior.md` — Amplitude analysis (view count → close rate data)
- Deal page screenshot — current Quotations table layout with CloudSign popover
