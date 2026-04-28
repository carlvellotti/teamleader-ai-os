# PRD review standards

The team's canonical PRD review lens is **Kalina's seven criteria**. Any review skill (`/kalina-review`, `/eng-review`, `/design-review`, etc.) should produce structured, line-referenced feedback against a clearly-named lens.

## Kalina's seven criteria

1. **What changes in the world if we ship this — and how would we notice?** Outcome over output.
2. **What's the actual business case, and why now over something else?** Strategic bet, named.
3. **Did you actually talk to anyone — and what would change the call?** Confidence sources.
4. **Did we put user first?** Inside-out specs get pushed back.
5. **Is the scope honest — MVP vs later, and what's actually in 'done'?** Real MVP line.
6. **Who else gets affected, and does anyone know?** Cross-functional impact.
7. **Is there actually a decision here?** Specs that gesture without committing.

Full versions live in `personas/kalina.md` along with her background and the kinds of pushback she'd give.

## Review output shape

Every review skill should produce output that is:

- **Structured** — one section per criterion (or per applicable criterion)
- **Line-referenced** — point at specific PRD content with `L42` or `L101-110` style references
- **Specific in pushback** — concrete questions, not generic advice. "Be more thoughtful" is not feedback. "The success metric on L23 is conversion rate — over what window, and against what baseline?" is feedback.
- **Verdict-bearing** — distinguish PASS / PARTIAL / FAIL with rationale per criterion

## Other reviewer lenses (forward-looking)

- `personas/eng-lead.md` — implementation cost and risk
- `personas/design-lead.md` — design system consistency and accessibility
- `personas/sales.md` — customer-facing narrative and objection handling
- `personas/cs.md` — day-one launch readiness and rollback story

The pattern is the same: encode a role's lens, run it against the work, get structured feedback.
