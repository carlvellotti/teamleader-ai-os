# Finding: The Buried Engagement Signal on Quotations

**CloudSign captures the engagement signal that best predicts deal close — 3+ views → 80% close rate, winning quote prediction in 7/7 multi-quote deals — but the deal page either shows it wrong ("Offline" false negatives) or hides it behind a popover most reps have stopped clicking; the fix is reliable, inline view counts on the Quotations table.**

---

## Evidence by Source

### Modjo — Sales and CS calls
Source: `data/modjo/2026-04-15/` (8 calls) → Extraction: `findings/extractions/modjo.md`

7 of 8 calls contain direct evidence of the tracking failure. The pattern is consistent: a customer confirms they viewed the quote, the system shows "Offline," and the rep either calls blind or asks the customer directly.

**Tracking failure across devices.** iPad (call-001), mobile phone (call-004), Firefox with privacy extensions (call-008), standard laptop with no obvious cause (call-002). No device or browser is reliable.

**Reps have abandoned signal-based follow-up.** Pieter calls everyone after 48 hours regardless of system status. Sara commits to calling when she sends a revised quote. Anna, Tom, and Maaike call and ask the customer what they've read. None of them use the activity panel for prioritization.

> "I always call about 48 hours after sending a quote. It's become a habit because, honestly, the tracking in our system isn't always reliable."
> — Pieter, rep (call-003, transcript 00:00:36) · VERIFIED

**Multi-quote triage is blind.** Call-007 is the sharpest instance: three options sent, all show "Offline." The customer had read option B multiple times, glanced at A, never opened C. Without the customer volunteering this, the rep would have guessed.

> "Dus als ik niet had verteld dat ik optie B het beste vind, had je dat niet geweten?"
> — Dennis, customer (call-007, transcript 00:01:28) · VERIFIED

**The customer side sees the failure too.** Rachel (call-002) read the renewal quote twice, expected a follow-up, got nothing, and "just sort of left it." A warm renewal went cold because neither side could see the other's engagement.

> "It's a bit frustrating because from my side it looks like we're being ignored, but apparently from your side it looks like I haven't engaged at all."
> — Rachel, customer (call-002, transcript 00:01:30) · VERIFIED

**Reps converge on view count as the desired signal.**

> "Honestly, I wish I could just see a simple view count — like, 'this quote has been opened four times.' That would tell me so much about how engaged someone is. Instead I'm kind of guessing."
> — Maaike, rep (call-004, transcript 00:01:12) · VERIFIED

**Caution: Modjo AI summaries inflate view counts.** Calls 001, 002, and 008 all show the summary reporting 3 views where the transcript says 2. All quotes in this finding are sourced from transcripts, not summaries. See `findings/quote-verification.md`, Modjo AI Summary Divergences.

---

### Zendesk — Support tickets
Source: `data/zendesk/tkt-*.json` (8 tickets) → Extraction: `findings/extractions/zendesk.md`

4 of 8 tickets are directly relevant. The strongest signals:

**The status label is unintelligible to new reps.** TKT-004: a rep three weeks into the job asked what "Offline" means. Two experienced colleagues gave contradictory definitions. Both told him to ignore the status and call the customer.

> "I asked two of my colleagues and they both said something different. One told me it means the quote was created but not sent via CloudSign, and the other said it just means the tracking isn't available. They both basically told me to just ignore the status and call the customer directly."
> — Daan, new rep (tkt-004.json) · VERIFIED

**CloudSign signature status doesn't sync to the deal page.** TKT-007: a signed document still shows "Sent" and "Offline" after 48 hours. The rep logged into the CloudSign portal directly to verify. Pipeline metrics are wrong.

> "The activity label next to 'View activity' shows 'Offline' which makes no sense at all since the customer obviously opened and signed the document online."
> — Antoine, rep (tkt-007.json) · VERIFIED

**An explicit feature request for inline metrics.** TKT-008: a Head of Sales Operations managing 30+ active deals spells out exactly what the Quotations table should show — a Views column, a Last Opened column, and icons for downloads/feedback. Framed around team workflows (stand-ups, pipeline reviews), not individual convenience.

> "the actually useful engagement data — how many times the quote was viewed, when it was last opened, whether it was downloaded, and whether any feedback was left — is all buried inside a popover that only appears when you click 'View activity.'"
> — James Hartley, Head of Sales Ops (tkt-008.json) · VERIFIED

**Adjacent signal.** TKT-006: deal pages with 10+ quotes take 15+ seconds to load. For high-volume reps, the buried-signal problem compounds with performance friction on exactly the deals where triage matters most.

---

### Planhat — Enterprise CSM notes
Source: `data/planhat/account-*.md` (4 accounts) → Extraction: `findings/extractions/planhat.md`

All 4 enterprise accounts report the same failure. The Planhat data adds three dimensions not visible in Modjo or Zendesk: organizational trust erosion, parallel tracking systems, and regulatory risk.

**Trust erosion at scale.** Global Industries (€240k ARR, 85 seats): CRO Henrik Larsson escalated a six-figure APAC renewal where the buyer confirmed viewing the quote on mobile — but the deal page showed "Offline." The rep didn't follow up. The deal closed only because the buyer reached out.

> "If reps can't trust what they see on the deal page, they stop looking at it. Then they stop using the system for pipeline decisions."
> — Henrik Larsson, CRO (account-001-globalindustries.md, 2026-04-14 QBR) · VERIFIED, CSM-recorded

**Parallel systems.** Axis SaaS (€165k ARR, 48 seats, Yellow health): the top AE maintains a personal spreadsheet reconstructed from email read receipts and phone notes. Junior reps take the panel at face value and delay follow-ups. The VP Sales Ops coaches new hires to "call anyway, don't trust the panel."

> "The data exists somewhere in CloudSign but it doesn't reliably surface on the deal page. We see 'Offline' for quotes we know were opened. Our best AE keeps a separate spreadsheet because he doesn't trust it. That spreadsheet shouldn't need to exist."
> — Marcia Engstrom, VP Sales Ops, written survey response (account-002-axis-saas.md, 2026-03-19) · VERIFIED, highest-provenance Planhat quote

**Regulatory risk.** Meridian Financial (€310k ARR, 62 seats): MiFID II requires complete client interaction trails for quotes above €50k. Internal audit found three deals where CloudSign recorded opens that never appeared on the deal page. Manual reconciliation adds 10-13 hours per quarter. Implicit churn threat: Jean-Paul (Head of Compliance) warned they may need "a platform that surfaces complete activity data natively." (account-003-meridian-financial.md, 2026-04-22) · VERIFIED numbers, PARAPHRASE of narrative

**Adoption risk for expansion.** NorthPath Logistics (€195k ARR, 54 seats, expanding): the NL team has abandoned the activity panel (23% click rate vs 89% deal management usage). A Belgian expansion (12 new seats) risks training new reps on a degraded workflow from day one.

> "My NL reps know to ignore 'Offline' and call anyway. But if I onboard 12 new people in Brussels and they see 'Offline' on a quote, they're going to assume the customer hasn't engaged. They'll wait. We'll lose deal velocity in the first quarter and then I'll have an adoption problem."
> — Anneke de Vries, CRO (account-004-northpath-logistics.md, 2026-04-17) · VERIFIED

---

### Amplitude — Product usage events
Source: `data/amplitude/quote-events.csv` (72 quotes, 50 deals, Jan–Mar 2026) → Analysis: `findings/quote-behavior.md`

The quantitative data validates every major qualitative pattern and adds the decision-relevant numbers.

**View count predicts close rate.** The threshold is 3+ views.

| Views | Close Rate | n |
|-------|-----------|---|
| 0 | 33.3% | 18 |
| 1 | 29.4% | 17 |
| 2 | 41.7% | 12 |
| 3+ | **80.0%** | 25 |

One view is not meaningfully different from zero (29.4% vs 33.3%). The signal is in repeated engagement — coming back to the quote a third time or more.

**View count predicts the winning option in multi-quote deals.** In all 7 won multi-quote deals, the winning quote had the most views among its siblings. 7/7, no exceptions. This validates Code 4: Anna's customer Dennis opening option B "meerdere keren" while ignoring option C is the general pattern, not an anecdote.

**Downloads and feedback are strong but rare confirming signals.** Downloaded: 85.7% close (6/7). Feedback sent: 83.3% close (5/6). But with only 7 downloads and 6 feedback events across 54 viewed quotes, these confirm a hot deal — they don't help triage the pipeline.

**First-view timing is noise.** Within 24 hours: 50.0% close. After 24 hours: 57.5% close. Design should prioritize view count over recency.

**Senior reps check 3.5x more, juniors have almost stopped.** Reps with >10 months tenure: 0.53 clicks per quote. Reps ≤10 months: 0.15 clicks per quote. The panel's biggest failure is with junior reps — they check least, trust it most when they do, and have the lowest win rate (44% vs 64%).

**The reps who click most aren't the ones who trust the data.** Mark Devos has the highest click ratio (0.67) and keeps a personal spreadsheet. Pieter Janssens has the lowest (0.12) and calls everyone after 48 hours. Both have abandoned the tool as a decision input — they just cope differently.

---

## The Two Problems

The qualitative and quantitative evidence separates into two distinct problems that compound each other:

### Problem 1: Data reliability
CloudSign tracks engagement events (views, downloads, feedback, signatures) in its own event log. But these events frequently fail to propagate to the deal page activity panel. The result is "Offline" false negatives — quotes that were opened, read, sometimes signed, but show no engagement on the deal page.

The failure is device/browser-dependent (iPad, mobile, Firefox with privacy extensions, and sometimes standard laptops) but unpredictable enough that reps can't know which views will register and which won't.

**Codes:** "Offline means nothing" (3/3 sources), "I just call everyone after two days" (3/3), "That spreadsheet shouldn't need to exist" (2/3), "From my side it looks like we're being ignored" (2/3), "They told me to just ignore it" (3/3).

### Problem 2: Information architecture
Even when the data is accurate, it's hidden behind a per-quote "View activity" popover click. At the scan level — where reps triage 30+ active deals during stand-ups and pipeline reviews — the only visible signal is a status label (Online / Viewed / Offline) that reps have learned is meaningless.

NorthPath's adoption metrics quantify the result: 89% of reps use deal management weekly, 94% create quotes through the platform, but only 23% click View Activity more than once a week.

**Codes:** "Just show me a view count" (3/3 sources), "All buried in a popover" (3/3), "Which quote did they actually read?" (2/3).

---

## Implied Fix

The evidence converges on one design move: **surface view count per quote as an inline column on the Quotations table.** This addresses both problems:

- **Reliability**: requires fixing the CloudSign → deal page event sync so view data actually arrives. Without this, inline columns would show wrong numbers — worse than the current popover.
- **Architecture**: moves the most predictive signal (view count, 80% close rate at 3+) from behind a popover to the scan level where reps actually work.

Secondary signals (downloads, feedback) could be shown as small icons. "Last opened" is useful context but less predictive than view count. Per-recipient breakdown (Eric's incorrect claim in call-006) is a separate, larger problem — CloudSign uses a single shared URL, so per-stakeholder tracking would require a product change upstream.

---

## Verification and Provenance

All quotes in this document were verified against raw source files. Full verification audit: `findings/quote-verification.md`.

| Status | Count |
|--------|-------|
| VERIFIED (exact match in source) | 18 |
| VERIFIED (truncated — words exact, sentence cut short) | 2 |
| VERIFIED (spliced — two verbatim segments bridged with "...") | 1 |
| PARAPHRASE (meaning correct, wording compressed or reframed) | 2 |
| NOT FOUND | 0 |

**Provenance notes:**
- Modjo quotes are from raw transcripts, not AI summaries. Three summaries inflate view counts (2 → 3); no quotes in this finding are affected.
- Planhat quotes are CSM-recorded, not transcribed. One quote (Priya, Global Industries) is third-hand: CSM → CRO → buyer. Marcia Engstrom's survey response is a written first-person submission — highest provenance in the Planhat set.
- Zendesk quotes are verbatim from ticket bodies.

---

## How We Got Here

**Step 1: Independent extraction.** Three sub-agents ran in parallel, one per source (Modjo, Zendesk, Planhat). Each read every file in its source directory and produced a structured extraction — claims, verbatim quotes, stated-vs-described behavior gaps, and confidence indicators. No cross-source synthesis at this stage. → `findings/extractions/{modjo,zendesk,planhat}.md`

**Step 2: Inductive coding.** Read all three extractions cold. Identified 11 candidate codes from recurring patterns across sources. Narrowed to 8 final codes based on frequency (kept codes appearing in 2+ sources) and specificity (named codes after what reps actually said, not generic labels). → `findings/proposed-codes.md`

**Step 3: Code application.** Applied the 8 codes back to all three extractions. For each code: frequency count across sources, sentiment assessment, and the 2-3 strongest supporting quotes. → `findings/coded-report.md`

**Step 4: Quote verification.** A fresh-eyes validator read every quote in the coded report and traced it back to the original source file — raw transcript, ticket JSON, or Planhat markdown. Tagged each as VERIFIED, PARAPHRASE, or NOT FOUND. Flagged three Modjo AI summary divergences where view counts were inflated. → `findings/quote-verification.md`

**Step 5: Quantitative validation.** Analyzed Amplitude event data (72 quotes, 50 deals, Jan–Mar 2026) to test whether the qualitative patterns hold in the numbers. Computed close rates by view count, download/feedback signals, multi-quote winner prediction, rep click frequency by tenure, and click-to-close correlation. → `findings/quote-behavior.md`

**Step 6: Triangulation.** This document. Merged the coded qualitative themes, verified quotes, and behavioral numbers into a single finding. The qual and quant tell the same story: the engagement signal exists, it predicts deal outcomes, and the product buries it.

### Source file index

| File | What it contains |
|------|-----------------|
| `data/modjo/2026-04-15/*.json` | 8 call transcripts + AI summaries |
| `data/zendesk/tkt-*.json` | 8 support tickets |
| `data/planhat/account-*.md` | 4 enterprise CSM account notes |
| `data/amplitude/quote-events.csv` | 72 quotes, 50 deals, 324 events |
| `findings/extractions/{source}.md` | Per-source structured extractions |
| `findings/proposed-codes.md` | 11 candidate → 8 final codes |
| `findings/coded-report.md` | Codes applied with frequency and quotes |
| `findings/quote-verification.md` | Every quote traced to source |
| `findings/quote-behavior.md` | Amplitude analysis |
