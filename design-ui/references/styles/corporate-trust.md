# Corporate trust

Familiar patterns, restrained color, and data that is easy to read.

## Signature traits

- Blue or teal primary on a soft neutral background.
- Moderate corner radius (6 to 8px) with 1px borders or very light shadows.
- Sans-serif type with a clear hierarchy.
- Plain, honest imagery, or none.
- Dense tables and forms handled carefully, with consistent components.

## Fits

- Finance, insurance, legal, healthcare administration.
- B2B software, dashboards, and internal tools.

## Avoid when

- Brands that must feel playful or edgy.
- When safe becomes the only idea: add one distinctive detail (an illustration style, a color, a tone of voice) so it does not look like every other SaaS site.

## Tokens

```css
:root {
  /* color */
  --bg: #F6F8FC;
  --surface: #FFFFFF;
  --text: #14213D;
  --muted: #475569;
  --primary: #1D4ED8;
  --on-primary: #FFFFFF;
  --accent: #0F766E;
  --focus: #1D4ED8;
  /* shape, depth, type */
  --radius: 8px;
  --shadow: 0 1px 2px rgba(20, 33, 61, 0.08), 0 4px 12px rgba(20, 33, 61, 0.06);
  --font-display: "Manrope", "Segoe UI", system-ui, sans-serif;
  --font-body: "Manrope", "Segoe UI", system-ui, sans-serif;
}
```

Fonts (Google Fonts names): Manrope (IBM Plex Sans or Source Sans 3 also work). Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.2; margin: 0 0 0.5em; }
.card { background: var(--surface); border: 1px solid rgba(20, 33, 61, 0.12); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: var(--radius);
  padding: 0.7rem 1.25rem; min-height: 44px; font: 600 1rem var(--font-body); cursor: pointer; }
.button:hover { filter: brightness(1.12); }
.input { background: var(--surface); color: var(--text); border: 1px solid var(--muted); border-radius: var(--radius);
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
```

## Accessibility traps

- **Blue-on-blue links and badges.** Several similar blues make links and badges hard to tell apart. Fix: measure each pair, give links 4.5:1, and add a non-color cue such as an underline.
- **Dense tables that are hard to scan.** Small text and tight rows tire the eye. Fix: use 14 to 16px text, row padding of at least 12px, right-aligned numbers, a sticky header, and visible focus on row actions.
- **Status shown by color alone.** Red and green badges fail for color-blind users. Fix: add an icon and a text label to every status.

## Pairs with

- Works with: flat-material, bento-grid, minimal-swiss.
- Do not mix with: neon-cyber, retro-pixel, playful-memphis.
