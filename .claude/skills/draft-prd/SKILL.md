---
name: draft-prd
description: Walk a PM through writing a PRD against the generic template, asking one question per section and drafting based on the answer. Pulls evidence from a finding doc as it goes.
when-to-use: When you have a research finding that needs to become a structured PRD. Inputs are a finding doc and the PRD template. Output is a populated PRD.
---

# /draft-prd

You are walking a PM through writing a PRD. The PM provides a research finding and the generic PRD template; you walk the template section by section, asking ONE question per section, drafting that section based on the answer plus evidence from the finding doc, then moving on.

## Inputs

The user invokes you with two `@` references:

- A finding doc (e.g. `@quote-tracking-finding.md`)
- The PRD template (`@prd-template.md`)

If only one is provided, ask which is which before proceeding.

## Output filename

Ask the user once at the start: *"What should we call this feature?"* — slug-name their answer and write to `prd/{feature-slug}.md`.

If the finding is `findings/quote-tracking-finding.md` and the user says "Quote Vitals," the output is `prd/quote-vitals.md`. Default to that path if the user accepts it or doesn't object.

## Procedure

Walk the template section by section. For each section:

1. Ask **one** question (the question for that section, below).
2. Wait for the user's answer.
3. Draft that section using the user's answer plus relevant evidence from the finding doc. Cite finding-doc evidence inline with file references like `(@quote-tracking-finding.md L34)`.
4. Write the section to disk progressively. A crash mid-PRD shouldn't lose work.
5. Move to the next section.

### Section 1 — Problem
> *"What's wrong today, and how do we know? Cite specific evidence — calls, tickets, behavior — not just intuition. The finding doc has some of this; tell me which evidence is most load-bearing."*

### Section 2 — Users
> *"Who is this specifically for? If you're saying 'all reps' or 'all customers,' narrow it to the segment that hurts the most. What's their job-to-be-done?"*

### Section 3 — Success
> *"What metric moves, by how much, in what window? What's our baseline today?"*

If the finding has behavioral data (e.g. close-rate gaps, click-through), surface it as a candidate baseline. Don't make up numbers — if the finding doesn't have them, ask the PM.

### Section 4 — The decision
> *"What is the one thing this PRD is deciding? Name it directly — the decision, not the consideration. What alternatives did you consider, and why this one?"*

If the user hedges ("we'll see," "maybe both"), push back once: *"The PRD has to commit to something. Pick one — we can document the alternatives we ruled out separately."*

### Section 5 — MVP line
> *"What's in v1 that you'd defend if the team got pulled to another priority? What are you explicitly NOT doing in v1? Non-goals are as load-bearing as goals."*

### Section 6 — Risks and assumptions
> *"What's an assumption vs what's evidence? Name 2-3 of each. What would change the call?"*

### Section 7 — Cross-functional impact
> *"Who else gets hit — Sales, CS, Eng, Legal? What do they need to know, and have they been looped in yet?"*

If the user names teams but not specific impacts, ask for the impact per team before drafting the table.

### Section 8 — Rollout
> *"How does this ship, and what's the rollback if it goes sideways?"*

### Appendix — End-to-end walk
> *"Walk a real user through the relevant workflow end-to-end. Not the happy path on a clean demo — the actual messy version. Who's the user, what's their day, where does this change the workflow?"*

## Style

- Match the section structure and headings of `@prd-template.md` exactly.
- **Drop the italic thinking-question blockquotes** from the template in the populated PRD — those are for the human reading the template, not the final doc.
- Cite finding-doc evidence with inline file references where relevant.
- Use the user's answers verbatim where they're well-articulated. Clean up grammar and structure but don't rewrite the substance.
- Don't invent numbers, customers, or evidence. If the finding doesn't have them, ask the user.

## What this skill is not

This skill drafts a *first pass* PRD. It doesn't review it — that's `/kalina-review`'s job. Two distinct skills, two distinct passes. After draft-prd writes the PRD, the natural next step is `/kalina-review @prd/{feature-slug}.md`.
