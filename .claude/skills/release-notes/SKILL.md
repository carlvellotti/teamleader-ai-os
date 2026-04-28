---
name: release-notes
description: Turn a feature passport into customer-facing release notes — headline, what shipped, what changes in the customer's workflow, links.
when-to-use: When a feature is shipping and you need to draft customer-facing release comms from the passport. Output is markdown plus a tweet-length headline.
---

# /release-notes

## Inputs

- A feature passport (e.g. `@passports/quote-vitals.md`)
- Optional: tone modifier (`professional` | `playful` | `technical`). Defaults to `professional`.

## Procedure

Read the passport. Extract:

1. The customer-facing headline (one sentence, under 100 characters)
2. What shipped — 3 to 5 bullets in customer-language, not internal-language
3. What changes in the customer's workflow — specific scenarios, not abstract benefits
4. Links — changelog entry, demo video, docs

Draft a markdown file at `release-notes/{feature-slug}-{date}.md` with sections:

- **Headline**
- **TL;DR** (one paragraph)
- **What's new** (bullets)
- **How it changes your workflow** (scenarios)
- **Resources**

## Style

- Customer-language only. No internal jargon, no PRD vocabulary, no phrasing that requires inside knowledge of the team.
- Specific scenarios beat abstract benefits. *"Send a quote and see when it's been viewed in the deal page"* beats *"improved quote engagement visibility."*
- Open with the workflow change, not the feature mechanics.
- Link to changelog, demo, and docs at the bottom.

## Notes

Generate-type skill — produces customer-facing copy from internal context. Reusable for any feature. The passport is the source of truth; the release note is its public-facing shape.
