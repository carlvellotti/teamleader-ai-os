# teamleader-ai-os

Team OS for the **Teamleader x Full Stack PM workshop** — April 30, 2026.

This repo is the shared working layer your team builds skills, context, and artifacts in. Every segment of the workshop pushes work here.

Workshop hub: <https://fullstackpm.com/teamleader>

## What's in here

- **`CLAUDE.md`** — root index. Start here. Tells Claude what kind of work happens in this repo and where things live.
- **`.claude/skills/`** — reusable workflows you run with `/skill-name`. Currently includes `/modjo-pull` (reference), `/release-notes` (reference), `/draft-prd` (interactive PRD walker).
- **`.claude/rules/`** — team standards (file naming, PRD review standards).
- **`personas/`** — role-based reviewers (Kalina, eng lead, design lead, Sales, CS). The kind of people whose review you'd want to pre-run before the meeting.
- **`templates/`** — reusable doc templates. Currently: a generic PRD template.
- **`examples/`** — worked references — a sample PRD that `/kalina-review` runs against during the workshop.
- **`data/`** — synthetic Modjo / Zendesk / Planhat / Looker fixtures used in Segment 2 (Research). Fictional but engineered to converge on the workshop finding.
- **`design-system/`** — pre-extracted Ahoy tokens. Fallback for Segment 4 if the Figma MCP isn't available.
- **`workspace/`** — gitignored personal scratch. Whatever you build here stays on your machine.

The workshop creates new directories during the day: `findings/`, `prd/`, `prototypes/`, `context/codebooks/`.

## Setup

```bash
git clone https://github.com/carlvellotti/teamleader-ai-os
cd teamleader-ai-os
claude
```

Then ask Claude to walk you through the repo. From that point everything runs from the prompts in the workshop pages.

## License

Workshop materials. The synthetic data in `data/` is fictional and intended only for the workshop exercise.
