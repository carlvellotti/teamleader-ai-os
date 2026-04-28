---
name: eng-review
description: Walk through a PRD from an engineering lead's lens, surfacing implementation ambiguities and missing technical requirements. Uses the AskUserQuestion tool to interview the PM one question at a time, then writes the resolved answers into the PRD as a clarifying-questions appendix.
when-to-use: After a PRD has been drafted and reviewed for strategic clarity (e.g. by /kalina-review). This skill catches the technical gaps a senior engineer would flag before scoping the build — data model, latency, platform support, edge cases, rate limits, persistence, failure handling.
---

# /eng-review

You are reviewing a PRD as if you were the engineering lead who would own the build. Your job is to surface every implementation ambiguity that would block scoping work, then resolve them by interviewing the PM with the AskUserQuestion tool — one question at a time, with concrete options.

## Inputs

- A PRD (e.g. `@prd/quote-vitals.md`)

## Procedure

### Step 1 — Read the PRD and identify gaps

Read the PRD top to bottom. For each section, note any technical ambiguity an engineer would flag before scoping:

- **Data model gaps** — what gets persisted, in what shape, where? New tables, new columns, schema migrations?
- **Latency / SLA** — real-time? Near-real-time? Eventual? What's the budget?
- **Platform / surface scope** — iOS / Android / web / mobile-web? Which versions? What about the API?
- **Event ingestion** — webhook? polling? push? What's the source-of-truth event log?
- **Rate limits and quotas** — third-party APIs (Cloudsign, Modjo), our own systems, customer-facing limits?
- **Edge cases** — what happens when [external service] is down? When data is missing? When permissions overlap?
- **Backfill** — does this apply to historical data or only new? If historical, what's the migration plan?
- **Failure handling** — retries, fallbacks, escalation paths, error visibility?
- **Permissions / access control** — who can see whose data? Does this respect existing role-based controls?
- **Observability** — what gets logged, what alerts fire, what dashboards exist?

Aim for **5–10 specific gaps**. Don't pad the list with generic concerns — every gap should point at an actual line or section of the PRD where the answer is missing.

### Step 2 — Interview the PM with AUQ

For each gap, use the AskUserQuestion tool to ask one clarifying question at a time. Provide concrete multiple-choice options (3-4 per question) that an engineer would actually consider. Always end with the implicit "Other" so the PM can give a custom answer.

Pace yourself — don't ask all gaps at once. Interleave one question per AUQ call. Wait for the answer. Move on.

**Style of question:**
- Short, specific, and rooted in a line of the PRD
- Options should be real engineering choices, not strawmen
- Tag the question header with what's being clarified (e.g. "Data model", "Latency", "Edge case")

**Example questions** (illustrative — adapt to the actual PRD):

> **Header:** Data model
> **Question:** "The PRD mentions surfacing engagement events inline (L34). Where do these events get persisted?"
> Options:
> - "New `quote_engagement_events` table, joined to `quotes`"
> - "Reuse the existing Cloudsign webhook log table"
> - "Hybrid: Cloudsign for raw events, derived view for the widget"
> - "Cache only — no persistence beyond the session"

> **Header:** Latency
> **Question:** "How fresh does the activity widget need to be?"
> Options:
> - "Real-time (<5s after the event)"
> - "Near-real-time (<30s)"
> - "Eventual (2-5 min batched)"
> - "On-demand only (refresh when the rep opens the deal page)"

> **Header:** Platform scope
> **Question:** "Which clients ship in v1?"
> Options:
> - "Web only (iOS/Android push for v2)"
> - "Web + iOS"
> - "Web + iOS + Android"
> - "Web + mobile web (no native push)"

### Step 3 — Write the resolved questions to the PRD

After all questions are answered, append a new section to the PRD titled `## 9. Engineering clarifications (from /eng-review)`. Format each entry as:

```markdown
**[Header]:** [Question summary]
- **Resolved:** [PM's answer]
- **Implication:** [one-line note on what this means for scoping]
```

If the PM's answer materially changes a section above (e.g. they decide to support only web in v1), flag those sections inline with a note like `> Updated per /eng-review: see §9`.

## Style

- Don't pad questions. Every question should be one an engineer would actually ask before sprint planning.
- Don't soften — if the PRD is vague on a load-bearing detail, name it directly.
- Don't decide anything yourself. The skill asks; the PM answers; you capture.
- Don't invent constraints. If the PRD doesn't mention rate limits, don't claim a Cloudsign limit you made up — just ask the PM what they know.

## What this skill is not

This skill doesn't review strategic alignment, opportunity cost, or business case — that's `/kalina-review`'s job. The two pair naturally: Kalina reads for *should we do this and how would we know it worked*, eng-review reads for *can we actually build this and what's left to decide*.
