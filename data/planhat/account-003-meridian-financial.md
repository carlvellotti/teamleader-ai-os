# Account: Meridian Financial Services

**Tier:** Enterprise
**CSM:** Sophie Laurent
**ARR:** €310,000
**Seats:** 62
**Renewal:** 2027-02-28
**Health:** Green

---

## 2026-04-22 — Annual Compliance Review with Jean-Paul Mercier (Head of Compliance)

Annual compliance review with Jean-Paul and two members of his audit team. This year's meeting had a new agenda item: quote activity logging for regulatory purposes. Under their updated MiFID II operational procedures, Meridian needs to demonstrate a complete client interaction trail for any financial product quote above fifty thousand euros. That includes proving when a client first viewed the quote, how many times they accessed it, and when they formally accepted.

Jean-Paul walked me through an incident from Q4 2025. They sent a structured product quote to a wealth management client. The client viewed the quote, called their advisor to discuss terms, and eventually signed. When Meridian's compliance team pulled the deal page records for a routine regulatory audit, the View activity popover showed the quote status as "Offline" for the entire period before signature. No "Viewed" stage, no "Online" timestamp — just Offline, then jumped straight to Signed.

The problem: the client's own IT team confirmed (via email server logs and browser history provided during the audit) that the quote PDF was opened three times over two days. CloudSign's own event log — which Jean-Paul's team accessed separately through the CloudSign admin panel — had all three opens recorded with timestamps. But none of that propagated to the deal page activity panel.

Jean-Paul said the regulator accepted their explanation this time because they could produce the CloudSign event log as supplementary evidence. But he called it "an unacceptable gap" and said if it happens again they'll need to build a manual reconciliation process — or find a platform that surfaces complete activity data natively.

## 2026-04-10 — Internal audit findings (shared by Jean-Paul)

Jean-Paul sent over a summary from their Q1 internal audit. His team reviewed all deals above fifty thousand euros from 2025 and found three instances where the deal page activity data conflicted with CloudSign's own event timestamps. In all three cases, CloudSign recorded opens that never appeared in the View activity popover on the deal page. Two showed "Offline" throughout; one showed a single "Viewed" event but missed two subsequent opens that occurred from a different device.

Jean-Paul's team has now added a manual step to their compliance checklist: cross-reference deal page activity with CloudSign admin logs for any quote in scope. He estimated this adds 15-20 minutes per audited deal. With roughly 40 deals per quarter in scope, that's 10-13 hours of manual reconciliation work per quarter that shouldn't be necessary.
