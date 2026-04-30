# Proposed Codes — Cross-Source Qualitative Analysis
Date: 2026-04-30
Sources: modjo.md, zendesk.md, planhat.md

---

## 1. "Offline means nothing"
**Definition:** The "Offline" status label produces false negatives so frequently that experienced users treat it as meaningless — quotes confirmed viewed by customers still show "Offline" on the deal page.

**Example quotes:**
- "Bij mij staan alle drie de offertes als 'Offline.' Ik kan niet zien welke je hebt geopend en welke niet." — Anna, rep (modjo.md, call-007)
- "The activity label next to 'View activity' shows 'Offline' which makes no sense at all since the customer obviously opened and signed the document online." — Antoine, rep (zendesk.md, TKT-007)
- "If reps can't trust what they see on the deal page, they stop looking at it. Then they stop using the system for pipeline decisions." — Henrik Larsson, CRO (planhat.md, Global Industries)

**Frequency:** 3/3 sources

---

## 2. "I just call everyone after two days"
**Definition:** Reps have replaced signal-based follow-up with calendar-based follow-up — calling every customer on a fixed schedule because the engagement data can't be trusted for prioritization.

**Example quotes:**
- "I always call about 48 hours after sending a quote. It's become a habit because, honestly, the tracking in our system isn't always reliable." — Pieter, rep (modjo.md, call-003)
- "They both basically told me to just ignore the status and call the customer directly." — Daan, new rep reporting colleagues' advice (zendesk.md, TKT-004)
- "My NL reps know to ignore 'Offline' and call anyway." — Anneke de Vries, CRO (planhat.md, NorthPath)

**Frequency:** 3/3 sources

---

## 3. "That spreadsheet shouldn't need to exist"
**Definition:** Reps and ops teams have built parallel tracking systems outside the product — personal spreadsheets, CloudSign portal logins, manual cross-referencing — to compensate for data that doesn't surface on the deal page.

**Example quotes:**
- "Our best AE keeps a separate spreadsheet because he doesn't trust it. That spreadsheet shouldn't need to exist." — Marcia Engstrom, VP Sales Ops, written survey (planhat.md, Axis SaaS)
- "I confirmed this by logging into the CloudSign portal directly." — Antoine, rep (zendesk.md, TKT-007)
- Jean-Paul's compliance team added a manual step: cross-reference deal page activity with CloudSign admin logs for every in-scope quote — 10-13 hours of reconciliation per quarter (planhat.md, Meridian)

**Frequency:** 2/3 sources (Zendesk, Planhat)

---

## 4. "Which quote did they actually read?"
**Definition:** In multi-quote deals, reps send 2-3 options but the system can't differentiate engagement across variants — there's no way to see which option the buyer prefers without asking them directly.

**Example quotes:**
- "Dus als ik niet had verteld dat ik optie B het beste vind, had je dat niet geweten?" — Dennis, customer (modjo.md, call-007)
- "Nee, precies. Ik had het moeten raden of gewoon alledrie opnieuw moeten doorlopen aan de telefoon." — Anna, rep (modjo.md, call-007)
- "I want to know that the buyer opened the premium quote four times and the standard quote once. That tells me where to steer the conversation. Right now I have to click View activity on each row, one by one, and mentally compare." — Anneke de Vries, CRO (planhat.md, NorthPath)

**Frequency:** 2/3 sources (Modjo, Planhat)

---

## 5. "From my side it looks like we're being ignored"
**Definition:** The tracking failure creates a two-sided trust breakdown — the customer thinks the rep is ignoring their engagement, while the rep thinks the customer hasn't looked. Warm deals go cold in the gap.

**Example quotes:**
- "It's a bit frustrating because from my side it looks like we're being ignored, but apparently from your side it looks like I haven't engaged at all." — Rachel, customer (modjo.md, call-002)
- "I did, but nobody followed up with me. I assumed Pieter could see that I'd opened it and would reach out, but I never heard anything. So I just sort of left it." — Rachel, customer (modjo.md, call-002)
- In a six-figure renewal, the buyer (Priya) proactively reached out because the rep had not followed up — the activity column implied zero engagement. The deal closed only because the buyer saved it. (planhat.md, Global Industries)

**Frequency:** 2/3 sources (Modjo, Planhat)

---

## 6. "They told me to just ignore it"
**Definition:** Institutional knowledge about the panel's unreliability transfers informally from experienced reps to new hires — creating a two-tier system where veterans bypass the tool and newcomers either trust bad data or inherit the workaround on day one.

**Example quotes:**
- "I asked two of my colleagues and they both said something different... They both basically told me to just ignore the status and call the customer directly." — Daan, new rep (zendesk.md, TKT-004)
- "call anyway, don't trust the panel" — Marcia Engstrom, VP Sales Ops, coaching new hires (planhat.md, Axis SaaS)
- "My NL reps know to ignore 'Offline' and call anyway. But if I onboard 12 new people in Brussels and they see 'Offline' on a quote, they're going to assume the customer hasn't engaged. They'll wait." — Anneke de Vries, CRO (planhat.md, NorthPath)

**Frequency:** 3/3 sources (Zendesk, Planhat explicitly; Modjo implicitly through universal workaround behavior)

---

## 7. "Just show me a view count"
**Definition:** When reps articulate what they actually want, they converge on the same signal: a simple view count per quote, visible without clicking. Not dwell time, not scroll depth — just "has this been opened, and how many times."

**Example quotes:**
- "Honestly, I wish I could just see a simple view count — like, 'this quote has been opened four times.' That would tell me so much about how engaged someone is. Instead I'm kind of guessing." — Maaike, rep (modjo.md, call-004)
- "A 'Views' column showing the view count directly in the table... A 'Last opened' column showing something like '2 days ago' or 'Apr 12'" — James Hartley, Head of Sales Ops (zendesk.md, TKT-008)
- "I want to know that the buyer opened the premium quote four times and the standard quote once." — Anneke de Vries, CRO (planhat.md, NorthPath)

**Frequency:** 3/3 sources

---

## 8. "All buried in a popover"
**Definition:** Even when engagement data is accurate, it's hidden behind a per-quote "View activity" click — invisible at the scan level where reps actually triage their pipeline. The information architecture buries the signal regardless of data quality.

**Example quotes:**
- "There's a 'View activity' link I can click for more detail, but even that doesn't show anything useful when the tracking doesn't pick up the view." — Maaike, rep (modjo.md, call-004)
- "the actually useful engagement data — how many times the quote was viewed, when it was last opened, whether it was downloaded, and whether any feedback was left — is all buried inside a popover that only appears when you click 'View activity.'" — James Hartley, Head of Sales Ops (zendesk.md, TKT-008)
- Only 23% of NorthPath reps click View activity more than once per week, despite 89% weekly deal management and 94% quote creation usage (planhat.md, NorthPath)

**Frequency:** 3/3 sources

---

## 9. "Is there something wrong with your tracking?"
**Definition:** Customers notice and question the tracking failure from their side — they expected their engagement to be visible to the rep and are surprised when it isn't. The product's reliability problem is externally visible.

**Example quotes:**
- "Maar ik heb het echt geopend. Via de link in de email. Allebei de keren op mijn laptop. Is er iets mis met jullie tracking?" — Claire, customer (modjo.md, call-008)
- "Dus als ik niet had verteld dat ik optie B het beste vind, had je dat niet geweten?" — Dennis, customer (modjo.md, call-007)
- "Tja, dat is wel een beetje zonde. Als jullie dat wel konden zien, had je meteen geweten dat je op optie B moest focussen." — Dennis, customer (modjo.md, call-007)

**Frequency:** 2/3 sources (Modjo, Planhat — Global Industries via Henrik relaying buyer feedback)

---

## 10. "The link is per-recipient" (it's not)
**Definition:** Reps misunderstand what CloudSign can and can't track — some believe it generates per-recipient links or per-stakeholder breakdowns. When they discover it doesn't, the gap between expected and actual capability compounds the trust problem.

**Example quotes:**
- "Well, the way CloudSign works is that the link is per-recipient. So when you forward it, each person who clicks it should generate their own tracking event." — Eric, rep (modjo.md, call-006; factually incorrect per product docs)
- "the activity view just shows me generic stages — 'Online,' 'Viewed,' things like that. It doesn't break it down by person in a way that's easy to read." — Eric, rep (modjo.md, call-006)
- Two experienced colleagues gave a new rep contradictory definitions of what "Offline" means (zendesk.md, TKT-004)

**Frequency:** 2/3 sources (Modjo, Zendesk)

---

## 11. "An unacceptable gap"
**Definition:** For regulated industries, the disconnect between CloudSign event logs and deal page activity data creates a compliance risk — not just a workflow inconvenience but a potential audit failure requiring manual reconciliation.

**Example quotes:**
- Jean-Paul called the gap between CloudSign event logs and deal page activity data "an unacceptable gap" and warned they may need "a platform that surfaces complete activity data natively." (planhat.md, Meridian)
- Internal audit found three deals where CloudSign recorded opens that never appeared on the deal page. Manual reconciliation: 10-13 hours per quarter. (planhat.md, Meridian)
- "This means my pipeline metrics are wrong — this deal should be showing as won but it's stuck in the sent stage." — Antoine, rep (zendesk.md, TKT-007)

**Frequency:** 2/3 sources (Zendesk, Planhat — but deep signal from one enterprise account with explicit churn threat)
