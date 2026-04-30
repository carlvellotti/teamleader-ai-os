# Kalina review — Quote Vitals

**PRD:** `prd/quote-vitals.md`
**Reviewed:** 2026-04-30

---

## 1. What changes in the world if we ship this — and how would we notice?

**Lines reviewed:** L27-44

The success metric is a popover click rate drop (L29): "A drop in click rate means the table is doing its job." The baselines are solid — 0.35 global, 0.15 junior, 0.53 senior, all sourced. The guardrail is smart: L37 says if popover clicks drop but deal-page time also drops, the feature isn't delivering value.

But the metric measures whether reps *stopped clicking the popover*, not whether reps *started making better decisions*. A click rate drop tells you the UI change worked as an information architecture fix. It doesn't tell you whether the information changed behavior. The indirect indicators (L39-42) gesture at this — "fewer reps maintaining parallel spreadsheets," "fewer complaints about Offline confusion" — but those are qualitative and have no target.

The PRD's own evidence says view count predicts close rate at 80% for 3+ views. If reps can now see that number, the hypothesis is they'll prioritize differently. But there's no metric tracking whether prioritization actually changes — follow-up timing, deal velocity on high-view quotes, junior rep win rate convergence.

**Question:** L29 says success is a popover click drop — but that measures whether reps *read the column*, not whether they *acted on it*. What's the behavioral metric that tells you reps are actually triaging differently? Follow-up speed on 3+ view quotes? Junior win rate narrowing? If the click rate drops but deal outcomes don't change, did this work?

---

## 2. What's the actual business case, and why now over something else?

**Lines reviewed:** L46-61

The decision section (L48-50) is clear on what we're building and the trade-off on sync. The alternatives considered (L57-61) are concrete and honestly dismissed. But there's no "why now" anywhere in the PRD. There's no mention of what the team is *not* doing to do this. There's no opportunity cost.

The problem is real and well-evidenced. But the same problem existed six months ago and will exist six months from now. What makes this the thing to spend engineering time on right now — instead of the sync fix, instead of something else entirely?

L100 mentions Anneke de Vries at NorthPath onboarding 12 Brussels reps. That's a concrete timing signal — but it's buried in cross-functional impact, not positioned as the strategic rationale.

**Question:** Why this quarter? L100 mentions NorthPath's Brussels expansion as a timing signal — is that the trigger? If so, name it in Section 4. If not, what would happen if we shipped this in Q4 instead of now? The PRD argues for the *what* but never for the *when*.

---

## 3. Did you actually talk to anyone — and what would change the call?

**Lines reviewed:** L87-94

This is strong. Four assumptions, each with an evidence grade (strong, mixed, assumption only, assumption with supporting logic), and each with a specific falsifiability condition. L91 is the best row — it names the mixed evidence honestly ("consistent with a discoverability problem... but seniors who click most also maintain shadow spreadsheets, suggesting distrust compounds") and gives a concrete 4-6 week timeline to validate.

The evidence base across the PRD is well-sourced — Amplitude data, Zendesk tickets, Modjo calls, Planhat accounts, all with line references. This isn't hand-waved.

One gap: the PRD cites James Hartley (L21, TKT-008) describing exactly the columns we're building. Has anyone gone back to James or the NorthPath team to show them this direction and validate it's what they meant? "Customer described the solution" is not the same as "customer validated our interpretation of their request."

**Question:** L21 cites James Hartley describing "a Views column, a Last Opened column." Have you shown this direction to James or any of the accounts in the finding to confirm the interpretation? He asked for icons for downloads/feedback too — we're explicitly deferring those (L77). Does he know that, and is the stripped-down version still valuable to him?

---

## 4. Did we put user first?

**Lines reviewed:** L123-147

The end-to-end walk is good. Lena's scenario (L125-146) hits the right beats: multi-quote deal, mixed engagement, a coaching moment, and — critically — the messy part where CloudSign sync fails and the buyer says they viewed a quote that shows 0 (L144). That's the hardest edge case for this feature and the PRD walks straight into it.

One thing the walk doesn't cover: L21 says the primary user is a sales manager scanning *across deals* in a pipeline review. But the walk (L127) opens a single deal page. The job-to-be-done is "scan 30+ deals in a stand-up" — but Quote Vitals only shows engagement data *after* you've opened a deal and scrolled to the Quotations table. The manager still has to open each deal one by one. The feature helps *within* a deal. It doesn't help the manager decide *which deal to open*.

**Question:** L25 says the job is "during a pipeline review, look at the Quotations table and instantly answer: which quotes are hot?" But the manager has to open each deal individually to see the table. For a 30-deal pipeline review, that's 30 page loads. Does this actually change the workflow, or does it just make each page load more useful? If the real triage happens at the deal-list level (not the deal-page level), does the table-only scope (L73) cut off the primary use case?

---

## 5. Is the scope honest — MVP vs later, and what's actually in 'done'?

**Lines reviewed:** L63-85

The MVP line is clean. The non-goals are specific and each has a rationale — not just "we ran out of room." L73 is the best non-goal I've seen in a while: it names the exact challenge that will come ("stakeholders will ask 'can we show this on the pipeline board too?'") and pre-commits to the answer.

Definition of done (L80-85) is tight but missing one thing: there's nothing about the feature flag or rollout mechanics. L113 describes a feature flag and phased rollout, but the definition of done doesn't include "feature flag implemented and tested" or "internal dogfood completed." If done = "columns visible on the table" but doesn't include the rollout infrastructure, the team might ship the UI before the flag exists.

L84 says "Offline/untracked quotes display a dash, not a zero." Good. But what about the column header behavior — does "Views" show for all deals, or only deals where at least one quote has been sent via CloudSign? A deal with 5 quotes all created offline would have 5 dashes. Is that useful or just noise?

**Question:** L84 says offline quotes show a dash. If a deal has five quotes and none were sent via CloudSign, do we show the Views and Last Opened columns with five dashes? Or do the columns only appear when at least one quote is trackable? The PRD needs to decide this — it's a design edge case that affects how the table looks for a large portion of deals.

---

## 6. Who else gets affected, and does anyone know?

**Lines reviewed:** L96-104

The impacts are specific. Sales leadership (L100) gets the most detailed treatment — three numbered items, a named account (NorthPath), a timing concern (Brussels ramp). CS (L101) names the specific risk (wrong-count ticket spike) and mitigation. Engineering (L102) lists three concrete questions that need answers.

Every row in the Owner and Looped in? columns is blank.

This is a draft, so maybe that's expected. But L100 describes impacts on Anneke de Vries's Brussels onboarding — that's happening now or soon. If this lands during that ramp and nobody told Anneke, we've surprised a €195k ARR account with a UI change during their most sensitive adoption window.

**Question:** L98-104 — every Owner and Looped in? cell is empty. When does that get filled? Specifically: has Anneke de Vries at NorthPath (L100) been told this change is coming during her Brussels expansion? If the answer is "not yet," that's a blocker for the mid-market cohort rollout (L110), not a nice-to-have.

---

## 7. Is there actually a decision here?

**Lines reviewed:** L46-61

This PRD has a point of view. L48 commits to the approach. L50 names what we're not building and why. L57-61 lists four alternatives and dismisses each with a specific reason. L52-55 names the trade-offs without hedging.

No "we might consider." No "one approach could be." No TBD on load-bearing decisions. The spec is doing the deciding.

This section is solid.

**Question:** None. The decision is made and committed.

---

## Summary

- **Pass:** 4 criteria (Problem evidence, Risks/assumptions, MVP scope, Decision commitment)
- **Flag:** 3 criteria (Success metric doesn't measure behavior change, no "why now," user walk doesn't test the cross-deal scan workflow)
- **Hardest question:** L25 says the job is pipeline triage across 30+ deals, but Quote Vitals only shows data after you've opened a single deal. Does the table-only scope (L73) cut off the primary user's actual workflow — and if so, is the real primary user the individual rep, not the sales manager?
