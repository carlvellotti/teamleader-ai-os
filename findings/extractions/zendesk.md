# Zendesk — Structured Extraction
Date: 2026-04-30

## Ticket: TKT-001 — Outlook-agenda synchronisatie werkt niet meer sinds vorige week
### Key Claims
- **Claim**: Outlook calendar sync has been broken for all users since the previous Tuesday, causing missed appointments for planners.
  - **Quote**: "Sinds vorige week dinsdag synchroniseert onze Outlook-agenda niet meer met Teamleader Focus. Afspraken die we in Teamleader aanmaken verschijnen niet meer in Outlook, en omgekeerd."
  - **Source**: TKT-001, initial ticket body (Pieter Van Damme, admin, Bouwgroep Janssens)
- **Claim**: The team already tried removing and re-adding the integration without success.
  - **Quote**: "We hebben al geprobeerd de koppeling te verwijderen en opnieuw in te stellen, maar het probleem blijft. Alle gebruikers in ons team hebben hetzelfde probleem."
  - **Source**: TKT-001, initial ticket body
- **Claim**: The broken sync has real operational consequences — planners are missing site appointments.
  - **Quote**: "Onze planners missen afspraken en dat zorgt voor verwarring op de werf."
  - **Source**: TKT-001, initial ticket body

### Stated Preferences vs. Described Behaviors
- No gap identified. The stated need (working calendar sync) aligns with described behavior (reliance on bidirectional sync for scheduling site work).

### Confidence Indicators
- Definitive language throughout. "niet meer" (no longer), "Alle gebruikers" (all users). No hedging. High confidence in the claim — this is a clear breakage report, not a preference statement.

---

## Ticket: TKT-002 — How to restrict deal visibility so reps only see their own team's deals?
### Key Claims
- **Claim**: After restructuring into three regional teams, they need team-level deal visibility, but the permissions system only supports individual-level restrictions.
  - **Quote**: "I've looked through the permissions settings but I can only find options to restrict at the individual user level, not at the team level. Is there a way to configure team-based deal visibility, or do I need to set this up rep by rep?"
  - **Source**: TKT-002, initial ticket body (Sarah Whitfield, admin, Greenfield Solutions)
- **Claim**: Current open visibility causes confusion during pipeline reviews.
  - **Quote**: "Right now everyone can see every deal in the system and it's causing confusion during pipeline reviews."
  - **Source**: TKT-002, initial ticket body
- **Claim**: Manual per-user configuration is impractical at their scale (40 reps).
  - **Quote**: "We have about 40 active reps across the three teams so doing it individually would be quite painful."
  - **Source**: TKT-002, initial ticket body

### Stated Preferences vs. Described Behaviors
- No significant gap. The stated need (team-scoped visibility) is directly tied to the described behavior (pipeline reviews where cross-team deal visibility causes confusion).

### Confidence Indicators
- Definitive framing: "I can only find options to restrict at the individual user level" — a clear statement of a missing capability. "it's causing confusion" — present tense, active problem, not hypothetical.

---

## Ticket: TKT-003 — Quote PDF renders broken on mobile - customer opened it 3 times
### Key Claims
- **Claim**: CloudSign quote PDF renders broken on mobile — text overlaps pricing table, logo is stretched, no horizontal scroll for full line items.
  - **Quote**: "The text overlaps the pricing table, the logo is stretched, and she can't scroll horizontally to see the full line items."
  - **Source**: TKT-003, initial ticket body (Markus Bauer, rep, Dresdner Haustechnik GmbH)
- **Claim**: The rep used the activity popover to see that the customer opened the quote 3 times, confirming engagement despite the broken rendering.
  - **Quote**: "I can see in the activity popover that she opened the quote 3 times — so she clearly tried to make it work before giving up and calling me."
  - **Source**: TKT-003, initial ticket body
- **Claim**: The broken mobile rendering forced a fallback to walking the customer through numbers over the phone.
  - **Quote**: "I ended up having to walk her through the numbers over the phone, which defeats the whole purpose of sending a professional-looking quote."
  - **Source**: TKT-003, initial ticket body
- **Claim**: Their customer base primarily checks quotes on phones.
  - **Quote**: "Our customers are tradespeople who check everything on their phones. If the quotes don't display properly on mobile we have a real problem."
  - **Source**: TKT-003, initial ticket body

### Stated Preferences vs. Described Behaviors
- Notable observation: The rep actually used the activity popover effectively here — he checked view count to diagnose his customer's experience. This is an example of the engagement signal being useful when the rep thinks to look for it, but it required a customer calling in frustration before the rep checked. The engagement data (3 views, no signature) was a diagnostic tool after the fact, not a proactive alert.

### Confidence Indicators
- Definitive and specific. Concrete device details (iPhone 14, Safari), cross-checked on Android. "Our customers are tradespeople who check everything on their phones" is a strong generalization — could be overstated, but the underlying point (mobile matters for this segment) is backed by the specific incident.

---

## Ticket: TKT-004 — What does 'Offline' mean in the CloudSign activity column?
### Key Claims
- **Claim**: A new rep cannot understand what "Offline" means in the CloudSign activity label and got contradictory explanations from two colleagues.
  - **Quote**: "I asked two of my colleagues and they both said something different. One told me it means the quote was created but not sent via CloudSign, and the other said it just means the tracking isn't available."
  - **Source**: TKT-004, initial ticket body (Daan Vermeersch, rep, Limburg Installatietechniek)
- **Claim**: Colleagues' workaround for the confusing status labels is to ignore them entirely and call the customer directly.
  - **Quote**: "They both basically told me to just ignore the status and call the customer directly."
  - **Source**: TKT-004, initial ticket body
- **Claim**: The rep wants to understand the activity statuses so he can time follow-ups based on engagement.
  - **Quote**: "I'd like to actually understand what I'm looking at so I know when to follow up and when a customer has already engaged with a quote."
  - **Source**: TKT-004, initial ticket body

### Stated Preferences vs. Described Behaviors
- Critical gap: The rep's stated preference is to use engagement data to time follow-ups. But his colleagues' described behavior is to bypass the engagement data entirely ("just ignore the status and call the customer directly"). This suggests the engagement signal is so unclear that experienced reps have learned to disregard it, while new reps who want to use it can't understand it. The signal exists but has been abandoned by the people it's meant to serve.

### Confidence Indicators
- The new rep uses hedging: "I have no idea what that means" and "I'm trying to understand" — honest uncertainty, not a complaint. Colleagues' advice is reported as definitive: "they both basically told me to just ignore the status." The fact that two experienced reps gave contradictory definitions of "Offline" is a strong signal that the label is genuinely ambiguous in the product.

---

## Ticket: TKT-005 — Bulk-archive old quotes from 2024 — is there a way?
### Key Claims
- **Claim**: Hundreds of expired quotes from 2024 still show as "Open," cluttering the quote list and making current quotes hard to find.
  - **Quote**: "We have hundreds of old quotes from 2024 that are still showing up as 'Open' in our system. They're obviously expired and will never be accepted, but they clutter our quote list and make it harder to find current ones."
  - **Source**: TKT-005, initial ticket body (Claire Dumont, admin, Atelier Dumont SARL)
- **Claim**: No bulk action is available — the only option is to mark quotes as lost one by one.
  - **Quote**: "I tried selecting multiple quotes from the list view but there doesn't seem to be a bulk action option. The only thing I can do is go into each quote individually and mark it as lost, which would take forever."
  - **Source**: TKT-005, initial ticket body

### Stated Preferences vs. Described Behaviors
- No gap. The stated need and described behavior are consistent: they want to clean up stale data and found no way to do it efficiently.

### Confidence Indicators
- Definitive: "They're obviously expired and will never be accepted." The user has already tried the UI ("I tried selecting multiple quotes") and is ready to script a solution via API — signals a power user who has exhausted the UI options.

---

## Ticket: TKT-006 — Deal page takes 15+ seconds to load when there are many linked items
### Key Claims
- **Claim**: Deal pages with many linked items (10+ quotes, 30+ tasks) take 15+ seconds to load, during which the page is partially rendered and non-interactive.
  - **Quote**: "For our bigger deals that have 10+ quotes and 30+ tasks, the page takes 15 seconds or more to fully render. During that time the page is partially loaded and I can't click on anything."
  - **Source**: TKT-006, initial ticket body (Thomas Richter, rep, Nordlicht Digital GmbH)
- **Claim**: Smaller deals load fine — the performance degrades proportionally with linked records.
  - **Quote**: "Smaller deals with just 1-2 quotes load fine. It seems like the more linked records there are, the worse it gets."
  - **Source**: TKT-006, initial ticket body
- **Claim**: The slow loading disrupts real-time client calls.
  - **Quote**: "It's really slowing down our workflow because we spend a lot of time on these larger deal pages during client calls."
  - **Source**: TKT-006, initial ticket body

### Stated Preferences vs. Described Behaviors
- Relevant to the engagement signal investigation: reps with 10+ quotes per deal are the exact segment most affected by the buried engagement signal. If the deal page already takes 15 seconds to load, adding a per-quote popover click for engagement data on top of that compounds the friction. The performance problem and the buried-signal problem intersect for high-volume deal pages.

### Confidence Indicators
- Definitive and precise. Specific measurements (15 seconds, 10+ quotes, 30+ tasks, 100 Mbps connection). Corroborated by colleagues ("My colleagues confirm the same experience"). Chrome and Firefox tested. This is a well-documented, reproducible report.

---

## Ticket: TKT-007 — CloudSign signature completed but deal still shows 'Sent' — status disconnect
### Key Claims
- **Claim**: A CloudSign document was signed (confirmed in CloudSign portal with timestamp and signature), but the Teamleader deal page still shows the quote status as "Sent" after 48 hours.
  - **Quote**: "The Status column for that quote still shows 'Sent' — it never updated to 'Accepted' even though the signature is complete."
  - **Source**: TKT-007, initial ticket body (Antoine Lefebvre, rep, MaisonVert Paysagistes)
- **Claim**: The activity label shows "Offline" for a document that was clearly opened and signed online — a contradictory signal.
  - **Quote**: "The activity label next to 'View activity' shows 'Offline' which makes no sense at all since the customer obviously opened and signed the document online."
  - **Source**: TKT-007, initial ticket body
- **Claim**: The sync failure corrupts pipeline metrics — the deal should show as won but is stuck in "Sent."
  - **Quote**: "This means my pipeline metrics are wrong — this deal should be showing as won but it's stuck in the sent stage."
  - **Source**: TKT-007, initial ticket body
- **Claim**: Manual status override is possible but defeats the purpose of the integration.
  - **Quote**: "I can manually change the status but that defeats the purpose of having CloudSign integration."
  - **Source**: TKT-007, initial ticket body

### Stated Preferences vs. Described Behaviors
- Key gap: The rep's stated preference is for automated sync between CloudSign and the deal page. The described behavior is manual verification by logging into the CloudSign portal directly ("I confirmed this by logging into the CloudSign portal directly") — a workaround that shows the rep doesn't trust the Teamleader status and has developed a cross-system verification habit. The status column in Teamleader is not a source of truth; it's something the rep checks against a different system.

### Confidence Indicators
- Extremely definitive. "makes no sense at all," "my pipeline metrics are wrong," "defeats the purpose." The rep waited 48 hours before reporting, ruling out a temporary delay. Cross-verified against the CloudSign portal. This is a concrete bug report with verifiable claims, not a preference statement.

---

## Ticket: TKT-008 — Feature request: show inline engagement metrics in the Quotations table instead of hiding them in a popover
### Key Claims
- **Claim**: The useful engagement data (view count, last opened, downloads, feedback) is buried in a popover behind the "View activity" click and not visible at scan level.
  - **Quote**: "the actually useful engagement data — how many times the quote was viewed, when it was last opened, whether it was downloaded, and whether any feedback was left — is all buried inside a popover that only appears when you click 'View activity.'"
  - **Source**: TKT-008, initial ticket body (James Hartley, admin/Head of Sales Operations, Meridian Property Group)
- **Claim**: For reps managing 30+ active deals, the click-per-quote interaction model is impractical for prioritizing follow-ups.
  - **Quote**: "When I'm managing 30+ active deals and trying to prioritize follow-ups, I need to see at a glance which quotes are hot (viewed 5 times in the last 2 days) versus cold (sent a week ago, never opened). Currently that requires clicking into every single quote's activity popover one by one."
  - **Source**: TKT-008, initial ticket body
- **Claim**: Specific request for inline columns — Views count, Last opened timestamp, and icons for downloads/feedback.
  - **Quote**: "A 'Views' column showing the view count directly in the table... A 'Last opened' column showing something like '2 days ago' or 'Apr 12'... Maybe a small icon if the document was downloaded or if feedback was submitted"
  - **Source**: TKT-008, initial ticket body
- **Claim**: This impacts team-level workflows — pipeline reviews and morning stand-ups.
  - **Quote**: "This would save our reps significant time during pipeline reviews and morning stand-ups."
  - **Source**: TKT-008, initial ticket body

### Stated Preferences vs. Described Behaviors
- The stated preference is clear: inline engagement metrics at scan level. The described behavior confirms the pain: clicking into every popover one by one across 30+ deals. No gap between preference and behavior here — they are consistent. Notably, this is a Head of Sales Operations speaking on behalf of the team workflow, not just an individual rep. The request is framed around team rituals (stand-ups, pipeline reviews) rather than individual rep convenience.

### Confidence Indicators
- Highly definitive. "I need to see at a glance" — no hedging. Specific quantities (30+ deals, "viewed 5 times in the last 2 days"). The only hedging is "Maybe a small icon" for the download/feedback indicator — suggesting the views and last-opened columns are the core ask, and the icon is a nice-to-have. The offer to "jump on a call to walk through our workflow" signals genuine investment in the problem, not a casual suggestion.
