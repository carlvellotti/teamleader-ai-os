# CloudSign Capabilities — What Teamleader's Quote Tracking Actually Does

Date: 2026-04-30
Purpose: Capability inventory before writing a spec against CloudSign's engagement data.

---

## 1. Engagement States (the lifecycle)

CloudSign tracks quotations through a linear stage progression. A quote moves forward through these states and does not regress:

| Stage | What triggers it | Visible in UI as |
|-------|-----------------|------------------|
| **Offline** | Quote created but not sent via CloudSign, or tracking failed | Status label "Offline" |
| **Made available online** | Quote sent through CloudSign (generates a shared URL) | Status label "Online" or "Sent" |
| **Viewed** | Recipient opens the CloudSign URL | Status label "Viewed" |
| **Feedback** | Recipient leaves feedback via the CloudSign interface | Status label "Feedback" |
| **Signed** | Recipient e-signs the document | Status label "Signed" |

**Key nuance: "Offline" is overloaded.** It means both "not sent via CloudSign" (intentional) and "sent via CloudSign but tracking failed" (bug). Our internal data shows reps and even experienced colleagues can't agree on what it means (Zendesk TKT-004). This ambiguity is a root cause of distrust.

**The states are quote-level, not recipient-level.** CloudSign generates a single shared URL per quote. There is no per-recipient tracking — if a quote is sent to three stakeholders, one "Viewed" event covers all of them. This matches our finding that Eric's claim about per-stakeholder tracking (call-006) was incorrect.

---

## 2. Metrics CloudSign Surfaces

### What it tracks

| Metric | Available? | Where visible | Notes |
|--------|-----------|---------------|-------|
| **View count** | Yes | Activity popover ("View activity" click) | Increments each time the CloudSign URL is opened. Our Amplitude data shows this is the strongest close predictor (80% at 3+ views). |
| **View timestamps** | Yes | Activity popover | When each view occurred. Shows as individual activity entries. |
| **Download event** | Yes | Activity popover | Whether the recipient downloaded the PDF. 85.7% close rate when downloaded, but rare (7/54 viewed quotes). |
| **Feedback event** | Yes | Activity popover | Whether the recipient submitted feedback through CloudSign. 83.3% close rate, also rare (6/54). |
| **Signature status** | Yes | Activity popover + status label | Whether the document was e-signed. |
| **Current stage** | Yes | Status column on Quotations table | The highest stage reached (Offline → Online → Viewed → Feedback → Signed). |

### What it does NOT track

| Metric | Status | Implication for spec |
|--------|--------|---------------------|
| **Dwell time / time-on-page** | Not tracked | Can't distinguish a 2-second bounce from a 20-minute read. View count is a proxy but imperfect. |
| **Scroll depth** | Not tracked | Can't tell if the buyer read page 1 of 8 or all 8. |
| **Per-recipient opens** | Not tracked | Single shared URL — no way to attribute views to specific stakeholders in a multi-recipient send. |
| **Device / browser info** | Not tracked | Can't see if the buyer viewed on mobile vs desktop. Relevant because mobile/iPad views frequently fail to register (calls 001, 004). |
| **Email open tracking** | Not tracked | CloudSign tracks the document URL, not the delivery email. No read receipts. |
| **Link click heatmaps** | Not tracked | No visibility into which sections of the quote received attention. |
| **Forwarding / sharing** | Not tracked | Can't detect if the buyer forwarded the CloudSign link to a colleague or decision-maker. |
| **Comparison behavior** | Not tracked | In multi-quote deals, can't see if buyer opened quotes side-by-side or in what order. |

### What's tracked but buried

The core problem from our finding: **view count, download, and feedback data exist in CloudSign's activity log but are only surfaced through a per-quote "View activity" popover click.** The Quotations table's scan-level view shows only the stage label (Online/Viewed/Offline), which:

- Collapses rich engagement data into a single word
- Treats "viewed once" and "viewed seven times" identically
- Shows "Offline" for both "not sent online" and "tracking failed"

Usage data confirms reps have largely stopped clicking: 0.35 clicks per quote globally, 0.15 for junior reps (Amplitude analysis, `findings/quote-behavior.md`).

---

## 3. API and Webhooks

### Teamleader API — Quotation endpoints

Teamleader Focus exposes a REST API (documented at `developer.teamleader.eu`) with quotation-related endpoints:

| Endpoint | What it does |
|----------|-------------|
| `quotations.list` | List quotations, filterable by deal |
| `quotations.info` | Get quotation details (amount, status, dates) |
| `quotations.create` | Create a new quotation |
| `quotations.send` | Send a quotation (triggers CloudSign if configured) |
| `quotations.update` | Update quotation metadata |
| `quotations.download` | Download the PDF |

### Webhook events for quotations

Teamleader supports webhooks via `webhooks.register`. Quotation-related events:

| Event | Fires when |
|-------|-----------|
| `quotation.created` | A quotation is created |
| `quotation.updated` | A quotation is updated |
| `quotation.sent` | A quotation is sent |
| `quotation.accepted` | A quotation is accepted/signed |
| `quotation.rejected` | A quotation is rejected |
| `quotation.deleted` | A quotation is deleted |

### What's missing from the API

**There are no webhook events for CloudSign engagement activity.** Specifically:

- No `quotation.viewed` event
- No `quotation.downloaded` (by recipient) event
- No `quotation.feedback_received` event
- No activity/event stream endpoint for CloudSign data

The engagement data that drives our finding — view counts, download events, feedback events — **is not available via the API or webhooks.** It lives only in the CloudSign activity log, accessible through the UI popover. This means:

1. **No external integrations can consume engagement data.** A CRM overlay, Slack bot, or dashboard that wants to show "quote X was viewed 4 times" cannot get that data programmatically.
2. **No real-time notifications.** A rep can't get a push alert when a buyer opens their quote. They have to manually check the popover.
3. **The "activities" endpoint (`activities.list`) returns deal-level activity** (calls, meetings, emails, notes) but does not include CloudSign engagement events in its response.

### Implication for spec

Any solution that wants to surface engagement data inline on the deal page must either:
- **Read from CloudSign's internal event store** (backend change — needs engineering investigation into how CloudSign stores and syncs events to the Teamleader deal page)
- **Add new API endpoints/webhooks** for engagement events (larger scope — would also unlock third-party integrations)

The current sync mechanism (CloudSign event store → deal page activity panel) already has reliability issues (the "Offline" false negatives). Fixing the sync is prerequisite to surfacing engagement data anywhere new.

---

## 4. CloudSign as a Product

CloudSign is Teamleader's integrated e-signature and document tracking feature, not a standalone third-party product. Key characteristics:

- **Built into Teamleader Focus** — not a separate SaaS. No standalone CloudSign login or dashboard.
- **Shared URL model** — each quote gets one URL. All recipients see the same link. No per-recipient tracking URLs.
- **Lightweight tracking** — designed for "did they see it / sign it" confirmation, not full document analytics (unlike dedicated tools like DocSend, PandaDoc, or Proposify).
- **E-signature** — the primary value prop. Tracking is secondary/ancillary.

### Competitive context

Dedicated proposal tools track significantly more:

| Feature | CloudSign | DocSend | PandaDoc | Proposify |
|---------|-----------|---------|----------|-----------|
| View count | Yes | Yes | Yes | Yes |
| Time per page | No | Yes | Yes | Yes |
| Per-recipient tracking | No | Yes | Yes | Yes |
| Device info | No | Yes | Limited | Limited |
| Forwarding detection | No | Yes | No | No |
| Real-time notifications | No | Yes | Yes | Yes |
| Webhooks for views | No | Yes | Yes | Yes |
| Inline deal-page metrics | No | N/A | N/A | N/A |

CloudSign is not trying to be DocSend. But the data it *does* track (view count) is highly predictive (80% close at 3+) and worth surfacing properly.

---

## 5. Summary: What We Can Build Against

**Data we have and can use (if sync is fixed):**
- View count per quote — strongest predictor, available in CloudSign event log
- View timestamps — useful for "last opened" display
- Download events — rare but strong confirming signal
- Feedback events — rare but strong confirming signal
- Signature status — already partially surfaced (but sometimes stale per TKT-007)

**Data we don't have and can't fake:**
- Per-recipient attribution (would require product change: unique URLs per recipient)
- Dwell time / scroll depth (would require CloudSign document viewer instrumentation)
- Real-time push notifications (would require new webhook events)

**The spec should scope to what CloudSign already tracks but fails to surface — not to what it doesn't track at all.** The view count alone, reliably synced and shown inline, would transform the rep workflow. The "nice to have" metrics (dwell time, per-recipient) would require significant CloudSign-side engineering and should be deferred.

---

## Sources

- Internal: `findings/quote-tracking-finding.md`, `findings/quote-behavior.md` (Amplitude analysis)
- Internal: Zendesk tickets TKT-004, TKT-007, TKT-008; Modjo calls 001-008; Planhat accounts 001-004
- External: Teamleader developer documentation (`developer.teamleader.eu`)
- External: Teamleader support center / help articles on CloudSign and quotations
- External: Competitive comparison with DocSend, PandaDoc, Proposify feature documentation
