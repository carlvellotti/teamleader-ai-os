---
name: modjo-pull
description: Pull Modjo call summaries and full transcripts for a date range and topic, structured for downstream investigation.
when-to-use: Any time you need fresh customer-call evidence for an investigation. Skip the manual export — this skill keeps the structure consistent across pulls so codebooks and findings don't break.
---

# /modjo-pull

Wraps the Modjo API. Modjo doesn't have a native MCP server; this skill calls the API directly and saves results in a consistent shape.

## Inputs

- `date_range`: ISO 8601 date range (e.g. `2026-04-01:2026-04-15`)
- `topic`: free-text topic filter passed to the Modjo search endpoint (e.g. "quote tracking")

## Authentication

Reads `MODJO_API_TOKEN` from the local `.env` file. **This token is not committed to the repo** — set it locally before running.

## Procedure

1. POST to `https://api.modjo.ai/v1/calls/search` with `{ from, to, query }`.
2. For each match, fetch `/calls/{id}` and `/calls/{id}/transcript`.
3. Save each call as `data/modjo/{date}/{call-id}.json` with:
   - `summary` — Modjo's AI summary
   - `transcript` — full transcript with speaker turns and timestamps
   - `participants` — array of `{ name, role, company }`
   - `date` — ISO datetime
   - `language` — `nl` | `en` | `mixed`
4. Write a `data/modjo/{date}/manifest.json` listing what was pulled.

## Notes

- **Trust the transcript, not the summary** for verbatim quotes. Modjo's summarization paraphrases — sometimes substantively. The summary is a navigational aid; the transcript is the source of truth.
- Mixed Dutch/English is normal. Don't translate at pull time — translation happens at extraction so we keep the original alongside the translation.
- In workshop contexts the data is pre-pulled into `data/modjo/2026-04-15/`. Only re-run this skill if you need fresher calls.

## API-over-MCP pattern

This is the pattern to reach for when a tool doesn't have a native MCP. Wrap the API as a skill, save results to a consistent path under `data/`, and treat the skill as if it were an MCP. From the user's perspective the experience is identical — `/modjo-pull` just works. Other candidates for the same treatment: tools where MCPs are still maturing, or where the team needs auth scoped to the repo rather than to a desktop session.
