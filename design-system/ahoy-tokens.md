# Ahoy Tokens — first extraction

Extracted via Figma MCP from the Teamleader Quotations file, deal page node `5579-877`, on April 28 2026. This is the artifact the workshop's Segment 4 produces live and commits to the team OS.

## What we got

### Colors

**Neutral (grays + white)**
- Neutral 100: `#FFFFFF`
- Neutral 200: `#F7F7FA`
- Neutral 300: `#E4E4E6`
- Neutral 400: `#C0C0C4`
- Neutral 500: `#82828C`

**Mint (Teamleader signature green/teal)**
- Mint 200: `#57D3D2`
- Mint 300: `#00B2B2`
- Mint 400: `#008A8C`

**Aqua (links / primary blue)**
- Aqua 400: `#0071F2`
- Aqua 500: `#004DA6`

**Ruby (errors / destructive)**
- Ruby 300: `#FF7040`
- Ruby 400: `#E84B17`
- Ruby 500: `#992600`

**Teal (dark navigation chrome)**
- Teal 100: `#F0F5FC`
- Teal 300: `#64788F`
- Teal 400: `#2A3B4D`
- Teal 500: `#1A1C20`

**Violet**
- Violet 100: `#F7F7FF`

### Typography

All Inter. Sizes in px / line-heights in px.

| Token | Family | Style | Size / LH | Notes |
|---|---|---|---|---|
| Heading 1 | Inter | SemiBold | 24 / 30 | page titles |
| Heading 4 | Inter | Bold | 12 / 18 | letter-spacing 0.6 — uppercase section labels |
| Heading 5 | Inter | SemiBold | 14 / 18 | card titles |
| Text Body | Inter | Regular | 14 / 21 | default paragraph |
| Text Body Compact | Inter | Regular | 14 / 18 | dense lists |
| Text Small | Inter | Regular | 12 / 18 | metadata / captions |
| UI Body | Inter | Medium | 14 / 18 | buttons, table headers |
| UI Small | Inter | Medium | 12 / 18 | small buttons / chips |
| Monospaced Body | Inter | Regular | 14 / 18 | (tagged "monospaced" but family is Inter) |

### Effects

- **Section divider (light):** inner shadow, `#E4E4E6`, offset 0/-1 — the 1px line between table rows and section bottoms
- **Section divider (medium):** inner shadow, `#C0C0C4`, offset 0/-1
- **Card shadow (Depths/Level 2):** drop shadow, `#2A3B4D` at 24% opacity, offset 0/2, blur 6
- **Segmented button outline:** 3-shadow combo using Neutral 400 — used on the Open/Won/Lost button group

## What we DIDN'T get

**No spacing or sizing tokens.** The Ahoy Figma file doesn't expose spacing as variables on this page — so when Claude builds the prototype, it'll have to eyeball spacing from the screenshot rather than pull canonical values. Worth surfacing as a workshop moment: this is exactly the "AI-code-ready" gap Simon flagged. The design system has solid color and type primitives, but the spacing scale lives in component-internal logic, not in shared tokens.

**No component definitions.** This is `get_variable_defs` only. To get the actual component structure (status pill, table row, kebab menu) we need `get_design_context` on smaller nodes — the full deal page node is too big and timed out.

## CSS variable form (ready to commit)

```css
:root {
  /* Neutral */
  --ahoy-neutral-100: #FFFFFF;
  --ahoy-neutral-200: #F7F7FA;
  --ahoy-neutral-300: #E4E4E6;
  --ahoy-neutral-400: #C0C0C4;
  --ahoy-neutral-500: #82828C;

  /* Mint */
  --ahoy-mint-200: #57D3D2;
  --ahoy-mint-300: #00B2B2;
  --ahoy-mint-400: #008A8C;

  /* Aqua */
  --ahoy-aqua-400: #0071F2;
  --ahoy-aqua-500: #004DA6;

  /* Ruby */
  --ahoy-ruby-300: #FF7040;
  --ahoy-ruby-400: #E84B17;
  --ahoy-ruby-500: #992600;

  /* Teal */
  --ahoy-teal-100: #F0F5FC;
  --ahoy-teal-300: #64788F;
  --ahoy-teal-400: #2A3B4D;
  --ahoy-teal-500: #1A1C20;

  /* Violet */
  --ahoy-violet-100: #F7F7FF;

  /* Type */
  --ahoy-font-family: "Inter", system-ui, sans-serif;

  /* Effects */
  --ahoy-divider-light: inset 0 -1px 0 #E4E4E6;
  --ahoy-divider-medium: inset 0 -1px 0 #C0C0C4;
  --ahoy-shadow-card: 0 2px 6px rgba(42, 59, 77, 0.24);
}
```

## Source node

- File: Quotations
- Node ID: `5579-877`
- URL: https://www.figma.com/design/Jnt3WDFcanR9QISziry3Ht/Quotations?node-id=5579-877
