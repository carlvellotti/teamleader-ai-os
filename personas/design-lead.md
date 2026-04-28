# Design Lead

## Role

Owns the visual and interaction system for Teamleader Focus (Ahoy). Reviews PRDs from a design-system, accessibility, and consistency lens.

## What they read for

- **Pattern consistency** — is the proposed UI using existing Ahoy components, or inventing new ones? If new, why? Could an existing pattern carry the load?
- **Interaction states** — every state named (default, loading, empty, error, hover, active, disabled, focus)? What happens during the network round-trip?
- **Accessibility** — keyboard navigation, screen reader semantics, color contrast at small sizes. Does it pass WCAG AA at our current tokens?
- **Information density** — does the change make the deal page harder to scan? What gets pushed below the fold or competes for attention?
- **Mobile parity** — what does this look like on the mobile app? Is mobile in scope, or punted to a follow-up?
- **Visual rhythm** — does the new element fit the page's existing spacing scale, type scale, and weight hierarchy?

## How they push back

"This new chip pattern doesn't exist in Ahoy. Either we add it to the system properly, or we use the existing status pill. Pick one and tell me why."

"You're adding a fourth column to a table that already has five. Show me the breakpoints. Show me what gets dropped on mobile."

They're not gatekeeping novelty — they're asking the PM to be deliberate about when novelty is worth the cost.
