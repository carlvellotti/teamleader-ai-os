# Teamleader AI OS

Shared workflow layer for the Teamleader product team. If you're new to this repo, this is the front door — read this first before doing anything else.

## What we make

- **Teamleader Focus** — our flagship CRM + project + invoicing tool. SMB and mid-market customers across NL, BE, DE, FR, UK. Mixed-language product surface (primary: Dutch, secondary: English).
- **Quotations** — the part of the deal page where reps send quotes to customers. Includes the e-signature flow ("Cloudsign activity") and the engagement signal ("View activity" link with status).

The current product focus: **the buried engagement signal on the Quotations table**. CloudSign already tracks real engagement — view count, downloads, buyer feedback, signature status — but it's hidden behind per-row popovers ("View activity" click) and disconnected from the Status column reps scan. Reps send multiple quote options per deal and can't quickly triage which ones the buyer is engaging with. The team is investigating, deciding the fix, and prototyping it through this repo.

CloudSign tracks five stages: Made available online → Viewed → Feedback → Signed (plus an Offline/not-tracked state). It does NOT track dwell time, scroll depth, per-recipient opens, or device info. There are no quotation-level webhooks — engagement data is only available via the activities feed.

## Customer types we sell to

- **SMB reps** — solo or 2-rep teams. High quote volume, small deals. Often working in mixed Dutch/English.
- **Mid-market AEs** — 3-10 person sales teams. Bigger deals, more sophisticated workflows. Heaviest source of feedback in Modjo and Zendesk.
- **Enterprise accounts** — pilot programs and larger contracts. CSM-managed (Planhat). Lower in count, higher in revenue.

## Where we hear from customers

- **Modjo** — sales + CS calls. Each call has an AI-generated summary + a full transcript. **Mixed Dutch and English.** Trust the transcript, not the summary, for verbatim quotes — the AI summarization sometimes paraphrases or reorders.
- **Zendesk** — support tickets from reps and customers.
- **Planhat** — CSM notes from enterprise accounts.
- **Amplitude** — product usage events: quote sends, views, downloads, deal outcomes. Event-level data exported as CSV. PMs can export directly from Amplitude charts without needing the data team.

When you investigate a question across these sources, extract independently from each one (sub-agents) before synthesizing. Voice-averaging is one of the failure modes of qual analysis.

## Tools we wire to

- **GitHub** — this repo
- **Modjo** — no native MCP. We wrap the API as a skill: see `.claude/skills/modjo-pull/`.
- **Figma Dev Mode MCP** — used in prototyping (Segment 4). The Quotations file lives at: `https://www.figma.com/design/Jnt3WDFcanR9QISziry3Ht/Quotations`
- **Amplitude** — currently CSV exports rather than live MCP. See `data/amplitude/`.

## Rules to follow

- **File naming** — kebab-case for all generated files. See `.claude/rules/file-naming.md`. Exceptions: `CLAUDE.md` and `README.md`.
- **PRD review** — Kalina's seven criteria are the canonical lens. See `.claude/rules/review-standards.md` and `personas/kalina.md`.
- **Quote provenance** — every quote in a finding or PRD should be traceable to a primary source (raw transcript, raw ticket). Modjo's AI summary is *not* a primary source — it's a secondary summary that can hallucinate.

## Where things live

| Folder | What it is |
|---|---|
| `.claude/skills/` | Reusable workflows (slash commands) |
| `.claude/rules/` | Team standards |
| `personas/` | Role-based review profiles |
| `templates/` | Reusable doc shapes |
| `examples/` | Worked references |
| `data/` | Customer feedback fixtures |
| `design-system/` | Ahoy tokens (Figma fallback) |
| `workspace/` | Personal scratch (gitignored) |
| `findings/` | Created during research work |
| `prd/` | Created during PRD work |
| `context/codebooks/` | Created during research codification |
| `prototypes/` | Created during prototyping |
