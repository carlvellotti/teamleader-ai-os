# Quote Verification — coded-report.md
Date: 2026-04-30
Verified against: data/modjo/2026-04-15/*.json, data/zendesk/tkt-*.json, data/planhat/account-*.md

---

## Summary

| Status | Count |
|--------|-------|
| VERIFIED | 18 |
| VERIFIED (truncated) | 2 |
| VERIFIED (spliced) | 1 |
| PARAPHRASE | 2 |
| NOT FOUND | 0 |

**All 23 items trace back to a source.** No fabricated quotes. Two items are narrative summaries (not presented as direct quotes) and verified for factual accuracy.

**3 Modjo AI summary divergences found** — all inflate view counts. No quotes in the coded report are affected (all were correctly pulled from transcripts), but the divergences are flagged below.

---

## Code 1: "Offline means nothing"

**Quote 1:** "If reps can't trust what they see on the deal page, they stop looking at it. Then they stop using the system for pipeline decisions."
- **Attributed to:** Henrik Larsson, CRO — planhat.md, Global Industries
- **Source:** account-001-globalindustries.md, 2026-04-14 QBR narrative
- **Status:** VERIFIED — exact match. CSM attributes the quote directly to Henrik. Note: this is CSM-recorded, not transcribed. Provenance is one step removed from a primary transcript.

**Quote 2:** "Bij mij staan alle drie de offertes als 'Offline.' Ik kan niet zien welke je hebt geopend en welke niet."
- **Attributed to:** Anna, rep — modjo.md, call-007
- **Source:** call-007-anna-dennis.json, transcript at 00:01:14
- **Status:** VERIFIED — exact substring. Anna's full utterance is: "Oké, dat is heel helder. Ik moet eerlijk zeggen — ik kon dat niet uit het systeem halen. Bij mij staan alle drie de offertes als 'Offline.' Ik kan niet zien welke je hebt geopend en welke niet." The quoted portion starts mid-utterance but every word matches.

**Quote 3:** "The activity label next to 'View activity' shows 'Offline' which makes no sense at all since the customer obviously opened and signed the document online."
- **Attributed to:** Antoine, rep — zendesk.md, TKT-007
- **Source:** tkt-007.json, ticket body
- **Status:** VERIFIED — exact match.

---

## Code 2: "I just call everyone after two days"

**Quote 1:** "I always call about 48 hours after sending a quote. It's become a habit because, honestly, the tracking in our system isn't always reliable."
- **Attributed to:** Pieter, rep — modjo.md, call-003
- **Source:** call-003-pieter-jan.json, transcript at 00:00:36
- **Status:** VERIFIED — exact substring. Full utterance starts with "Top. I should mention —" before the quoted portion. Quoted words are verbatim.

**Quote 2:** "My NL reps know to ignore 'Offline' and call anyway. But if I onboard 12 new people in Brussels and they see 'Offline' on a quote, they're going to assume the customer hasn't engaged. They'll wait. We'll lose deal velocity in the first quarter."
- **Attributed to:** Anneke de Vries, CRO — planhat.md, NorthPath
- **Source:** account-004-northpath-logistics.md, 2026-04-17 expansion scoping call
- **Status:** VERIFIED (truncated) — the words included are verbatim, but the source continues: "...and then I'll have an adoption problem." The truncation drops a meaningful consequence. Note: the full quote IS used in Code 6, Quote 2.

**Quote 3:** "If I know someone's read it three times, I know they're interested and I can be more direct. But right now it's a black box."
- **Attributed to:** Maaike, rep — modjo.md, call-004
- **Source:** call-004-maaike-thomas.json, transcript at 00:01:36
- **Status:** VERIFIED — exact substring. Full utterance continues with "Anyway — since you did read it, what did you think?" Quoted portion is verbatim.

---

## Code 3: "That spreadsheet shouldn't need to exist"

**Quote 1:** "The activity panel on quotes. My team needs to know when a prospect opens a quote so they can time their follow-up. The data exists somewhere in CloudSign but it doesn't reliably surface on the deal page. We see 'Offline' for quotes we know were opened. Our best AE keeps a separate spreadsheet because he doesn't trust it. That spreadsheet shouldn't need to exist."
- **Attributed to:** Marcia Engstrom, VP Sales Ops, written survey — planhat.md, Axis SaaS
- **Source:** account-002-axis-saas.md, 2026-03-19 quarterly friction survey (blockquoted as verbatim written response)
- **Status:** VERIFIED — exact match. This is the highest-provenance quote in the entire Planhat data set: a written survey response, not CSM paraphrase.

**Quote 2:** "I confirmed this by logging into the CloudSign portal directly... I can manually change the status but that defeats the purpose of having CloudSign integration."
- **Attributed to:** Antoine, rep — zendesk.md, TKT-007
- **Source:** tkt-007.json, ticket body
- **Status:** VERIFIED (spliced) — both halves are verbatim from the same ticket, but the "..." bridges non-contiguous sentences. Full source between the halves: "...where the document clearly shows as signed with a timestamp and the client's signature. However, when I go back to the deal page in Teamleader Focus, two things are wrong: [numbered list]. So now I have a deal where CloudSign knows the quote is signed, but Teamleader still thinks it's just 'Sent' and 'Offline.' [more detail] I've waited 48 hours hoping it would sync, but nothing has changed. I can manually change the status..." The splice skips ~6 sentences. Meaning preserved, but the gap is substantial.

**Quote 3:** Jean-Paul's compliance team cross-references deal page activity with CloudSign admin logs for every in-scope quote — 15-20 min per deal, ~40 deals/quarter = 10-13 hours of manual reconciliation per quarter.
- **Attributed to:** planhat.md, Meridian (no quotation marks — presented as factual summary)
- **Source:** account-003-meridian-financial.md, 2026-04-10 internal audit findings
- **Status:** PARAPHRASE — this is a narrative summary, not a direct quote. The numbers are accurate: source says "15-20 minutes per audited deal," "roughly 40 deals per quarter," and "10-13 hours of manual reconciliation work per quarter." The coded report compresses three sentences into one and drops "that shouldn't be necessary" from the end. Factually sound.

---

## Code 4: "Which quote did they actually read?"

**Quote 1:** "Dus als ik niet had verteld dat ik optie B het beste vind, had je dat niet geweten?"
- **Attributed to:** Dennis, customer — modjo.md, call-007
- **Source:** call-007-anna-dennis.json, transcript at 00:01:28
- **Status:** VERIFIED — exact substring. Full utterance starts with "Serieus?" before the quoted portion. Quoted words are verbatim.

**Quote 2:** "Nee, precies. Ik had het moeten raden of gewoon alledrie opnieuw moeten doorlopen aan de telefoon."
- **Attributed to:** Anna, rep — modjo.md, call-007
- **Source:** call-007-anna-dennis.json, transcript at 00:01:35
- **Status:** VERIFIED — exact substring. Full utterance continues: "Dat is ook een beetje waarom ik bel — ik wilde gewoon direct van jou horen waar je interesse ligt."

**Quote 3:** "I want to know that the buyer opened the premium quote four times and the standard quote once. That tells me where to steer the conversation. Right now I have to click View activity on each row, one by one, and mentally compare."
- **Attributed to:** Anneke de Vries, CRO — planhat.md, NorthPath
- **Source:** account-004-northpath-logistics.md, 2026-04-17 expansion scoping call
- **Status:** VERIFIED — exact match.

---

## Code 5: "From my side it looks like we're being ignored"

**Quote 1:** "It's a bit frustrating because from my side it looks like we're being ignored, but apparently from your side it looks like I haven't engaged at all."
- **Attributed to:** Rachel, customer — modjo.md, call-002
- **Source:** call-002-david-rachel.json, transcript at 00:01:30
- **Status:** VERIFIED — exact substring. Full utterance starts with "Please do." Quoted portion is verbatim.

**Quote 2:** "I did, but nobody followed up with me. I assumed Pieter could see that I'd opened it and would reach out, but I never heard anything. So I just sort of left it."
- **Attributed to:** Rachel, customer — modjo.md, call-002
- **Source:** call-002-david-rachel.json, transcript at 00:00:46
- **Status:** VERIFIED — exact match of full utterance at that timestamp.

**Quote 3:** In a six-figure APAC renewal, the buyer (Priya) confirmed reading the quote via email ("I've read through the whole thing, looks good") but the deal page showed "Offline."
- **Attributed to:** planhat.md, Global Industries (narrative summary with embedded quote)
- **Source:** account-001-globalindustries.md, 2026-04-14 QBR narrative
- **Status:** PARAPHRASE — the embedded quote "I've read through the whole thing, looks good" is verified against the source. However, the coded report says "via email" while the source says Priya "messaged him" — different channel. Also: the source provenance is third-hand (CSM Maya Chen recording Henrik Larsson relaying Priya's message). The coded report doesn't flag this provenance chain.

---

## Code 6: "They told me to just ignore it"

**Quote 1:** "I asked two of my colleagues and they both said something different. One told me it means the quote was created but not sent via CloudSign, and the other said it just means the tracking isn't available. They both basically told me to just ignore the status and call the customer directly."
- **Attributed to:** Daan, new rep — zendesk.md, TKT-004
- **Source:** tkt-004.json, ticket body
- **Status:** VERIFIED — exact match.

**Quote 2:** "But if I onboard 12 new people in Brussels and they see 'Offline' on a quote, they're going to assume the customer hasn't engaged. They'll wait. We'll lose deal velocity in the first quarter and then I'll have an adoption problem."
- **Attributed to:** Anneke de Vries, CRO — planhat.md, NorthPath
- **Source:** account-004-northpath-logistics.md, 2026-04-17 expansion scoping call
- **Status:** VERIFIED — exact match. (This is the full version of the same quote truncated in Code 2, Quote 2.)

**Quote 3:** "En Claire — als je hem opent en er staat weer 'Offline' bij mij, weet ik nu in ieder geval dat dat niets zegt."
- **Attributed to:** Tom, rep — modjo.md, call-008
- **Source:** call-008-tom-claire.json, transcript at 00:02:23
- **Status:** VERIFIED — exact substring. Full utterance starts with "Top. Ik heb het morgen bij je."

---

## Code 7: "Just show me a view count"

**Quote 1:** "Honestly, I wish I could just see a simple view count — like, 'this quote has been opened four times.' That would tell me so much about how engaged someone is. Instead I'm kind of guessing."
- **Attributed to:** Maaike, rep — modjo.md, call-004
- **Source:** call-004-maaike-thomas.json, transcript at 00:01:12
- **Status:** VERIFIED — exact substring. Full utterance starts with "It really is."

**Quote 2:** "When I'm managing 30+ active deals and trying to prioritize follow-ups, I need to see at a glance which quotes are hot (viewed 5 times in the last 2 days) versus cold (sent a week ago, never opened). Currently that requires clicking into every single quote's activity popover one by one."
- **Attributed to:** James Hartley, Head of Sales Ops — zendesk.md, TKT-008
- **Source:** tkt-008.json, ticket body
- **Status:** VERIFIED — exact match.

**Quote 3:** "I want to know that the buyer opened the premium quote four times and the standard quote once. That tells me where to steer the conversation."
- **Attributed to:** Anneke de Vries, CRO — planhat.md, NorthPath
- **Source:** account-004-northpath-logistics.md, 2026-04-17 expansion scoping call
- **Status:** VERIFIED (truncated) — the quoted words are verbatim but the source continues: "Right now I have to click View activity on each row, one by one, and mentally compare." Truncation drops the behavioral detail but preserves the core claim.

---

## Code 8: "All buried in a popover"

**Quote 1:** "the actually useful engagement data — how many times the quote was viewed, when it was last opened, whether it was downloaded, and whether any feedback was left — is all buried inside a popover that only appears when you click 'View activity.'"
- **Attributed to:** James Hartley, Head of Sales Ops — zendesk.md, TKT-008
- **Source:** tkt-008.json, ticket body
- **Status:** VERIFIED — exact substring. Source sentence starts with "But the actually useful..." The quote drops the leading "But."

**Quote 2:** Only 23% of NorthPath reps click View activity more than once per week, despite 89% weekly active on deal management and 94% on quote creation.
- **Attributed to:** planhat.md, NorthPath (no quotation marks — presented as a stat)
- **Source:** account-004-northpath-logistics.md, 2026-04-03 pre-expansion readiness check
- **Status:** VERIFIED — all three numbers (23%, 89%, 94%) match the source exactly. The framing ("despite") is editorial repackaging of the source's observation that quote activity panel engagement is "notably low" relative to other metrics. Accurate summary.

**Quote 3:** "There's a 'View activity' link I can click for more detail, but even that doesn't show anything useful when the tracking doesn't pick up the view."
- **Attributed to:** Maaike, rep — modjo.md, call-004
- **Source:** call-004-maaike-thomas.json, transcript at 00:00:55
- **Status:** VERIFIED — exact substring. Full utterance starts with "Exactly. On my screen it just says 'Offline.'"

---

## Modjo AI Summary vs. Transcript Divergences

Three calls have AI summaries that **inflate the view count** compared to what the customer actually said in the transcript. None of the coded report quotes are affected (all were correctly sourced from transcripts), but these divergences matter if anyone downstream uses the summaries as a shortcut.

### Call 001 (Sara / Marcus)
- **Summary says:** "Marcus geeft aan dat hij de offerte **drie keer** heeft bekeken op zijn iPad"
- **Transcript says:** "Ik heb hem **twee keer** doorgelezen eigenlijk. De eerste keer op mijn iPad dinsdag, en toen nog een keer woensdag" (00:00:34)
- **Divergence:** Summary says 3 views. Transcript says 2. The summary also says all views were on iPad; the transcript only mentions iPad for the first view.

### Call 002 (David / Rachel)
- **Summary says:** "Rachel mentions she reviewed the renewal quote **three times** last week"
- **Transcript says:** "Read the whole thing **twice**, actually" (00:00:26) and "I opened it on my laptop, at my desk. **Twice.**" (00:01:10)
- **Divergence:** Summary says 3 views. Transcript says 2, stated twice by the customer with emphasis.

### Call 008 (Tom / Claire)
- **Summary says:** "Claire bevestigt dat ze het document vandaag **drie keer** heeft geopend"
- **Transcript says:** "Ik heb hem **twee keer** gelezen" (00:00:28)
- **Divergence:** Summary says 3 views. Transcript says 2. Summary also says "vandaag" (today); transcript says "gisteren" (yesterday) for the first view and "this morning" for the second.

**Pattern:** All three summaries inflate 2 → 3. This is consistent enough to look systematic rather than random. The CLAUDE.md warning about Modjo summaries ("the AI summarization sometimes paraphrases or reorders") understates the issue — these aren't reorderings, they're factual errors in a numerically specific claim.

---

## Provenance Notes

All Planhat quotes carry an inherent provenance caveat: they are CSM-recorded notes, not transcripts. The chain is Customer → CSM memory/notes → Planhat file. The exceptions:

- **Marcia Engstrom's survey response** (Axis SaaS, Code 3 Quote 1): written by Marcia herself. Highest provenance in the Planhat set.
- **Priya's quote** (Global Industries, Code 5 Quote 3): third-hand. CSM (Maya Chen) → CRO (Henrik) → buyer (Priya). Lowest provenance in the entire data set.
- **Anneke de Vries's quotes** (NorthPath, Codes 2/4/6/7): CSM-attributed as direct quotes. Appear verbatim-flavored but are one step removed.
