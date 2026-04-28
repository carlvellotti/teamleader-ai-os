# File naming

Use **kebab-case** for all filenames in this repo (`quote-tracking-finding.md`, `competitive-pull/SKILL.md`, `account-summary.md`).

Exceptions: `CLAUDE.md` and `README.md` are conventional all-caps and stay that way.

## Where this applies

- Skills: `.claude/skills/{kebab-name}/SKILL.md`
- Findings, PRDs, codebooks, all generated artifacts
- Folder names inside `data/`, `findings/`, `context/`, `prototypes/`
- Date-stamped folders use ISO format: `data/modjo/2026-04-15/`

## What it doesn't apply to

- External file formats with their own conventions (`SKILL.md` per the Anthropic spec, `package.json`, etc.)
- Source data files where the original system used a different convention

When generating a path for a new file, follow this rule unless explicitly instructed otherwise.
