# Claymorphism

Chunky, inflated shapes that look like soft clay, with a pastel palette and gentle inner highlights.

## Signature traits

- Large radii (24 to 40px) and rounded, bubbly shapes.
- Two shadows: a soft outer drop and inner highlights and shades that make shapes look inflated.
- Saturated pastels with dark text.
- Chunky rounded type.
- 3D-looking blobs and rounded icons as illustrations.

## Fits

- Kids and education products, onboarding, casual apps.
- Friendly consumer products and wellness check-ins.

## Avoid when

- Serious or dense data (finance, enterprise tables).
- Brands that need to feel premium or technical.

## Tokens

```css
:root {
  /* color */
  --bg: #FFF1E0;
  --surface: #FFFFFF;
  --text: #2A2150;
  --muted: #5A5080;
  --primary: #6D4AFF;
  --on-primary: #FFFFFF;
  --accent: #FF8A5B;
  --focus: #6D4AFF;
  /* shape, depth, type */
  --radius: 28px;
  --shadow: 12px 12px 24px rgba(109, 74, 255, 0.18);
  --font-display: "Fredoka", "Trebuchet MS", system-ui, sans-serif;
  --font-body: "Nunito", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --inner-light: rgba(255, 255, 255, 0.75);
  --inner-dark: rgba(60, 30, 120, 0.12);
}
```

Fonts (Google Fonts names): Fredoka for headings, Nunito for body. Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 600; line-height: 1.15; margin: 0 0 0.5em; }
.card { background: var(--surface); border-radius: var(--radius); padding: 1.5rem;
  box-shadow: var(--shadow), inset 6px 6px 12px var(--inner-light), inset -6px -6px 12px var(--inner-dark); }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 999px;
  box-shadow: 6px 6px 14px rgba(109, 74, 255, 0.35), inset 3px 3px 6px rgba(255, 255, 255, 0.35);
  padding: 0.8rem 1.75rem; min-height: 48px; font: 700 1rem var(--font-body); cursor: pointer; }
.button:active { transform: translateY(2px); }
.input { background: var(--bg); color: var(--text); border: 2px solid var(--muted); border-radius: 18px;
  padding: 0.75rem 1rem; min-height: 48px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Pastel text.** White or pastel type on pastel shapes fails contrast. Fix: use the dark text token (about 13:1) on every pastel; never white on a pastel fill.
- **Inner shadows blur small text.** The inflated look reduces clarity at small sizes. Fix: keep inputs flat with a solid border, as in the starter.
- **Everything is round, so nothing says clickable.** Rounded blobs look alike. Fix: make actions pills with a label, at least 44px tall, and keep decorative shapes non-interactive.
- **Heavy shadows on long lists.** Many large blurred shadows slow scrolling on low-end phones. Fix: limit big shadows to hero cards and keep list items light.

## Pairs with

- Works with: playful-memphis (more color), organic-natural (calmer), bento-grid.
- Do not mix with: neo-brutalism, glassmorphism, corporate-trust.
