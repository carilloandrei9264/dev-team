# Neo-brutalism

Thick black outlines, hard offset shadows, flat saturated color, and visible structure.

## Signature traits

- 2 to 4px solid black borders on everything that matters.
- Hard offset shadows with no blur (for example 6px 6px 0 black).
- Flat, saturated fills: yellow, pink, mint, blue.
- Bold grotesque or monospace type, tight and large.
- Playful movement on hover: elements shift into their shadow.
- Raw web variant: default fonts, plain links, no shadows.

## Fits

- Creative studios, indie products, portfolios, event sites.
- Brands that want attitude, especially for younger audiences.

## Avoid when

- Banking, healthcare, legal, or other formal contexts.
- Long reading, where loud outlines tire the eye.

## Tokens

```css
:root {
  /* color */
  --bg: #FFF6D6;
  --surface: #FFFFFF;
  --text: #000000;
  --muted: #333333;
  --primary: #FFD400;
  --on-primary: #000000;
  --accent: #FF4D8D;
  --focus: #000000;
  /* shape, depth, type */
  --radius: 6px;
  --shadow: 6px 6px 0 #000000;
  --font-display: "Space Grotesk", "Arial Black", system-ui, sans-serif;
  --font-body: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --ink: #000000;
  --border: 3px solid #000000;
}
```

Fonts (Google Fonts names): Space Grotesk (Archivo Black for display; Space Mono for labels). Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 500 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.05; margin: 0 0 0.5em; }
h1 { font-size: clamp(2.5rem, 7vw, 4.5rem); }
.card { background: var(--surface); border: var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: var(--border); border-radius: var(--radius);
  box-shadow: 4px 4px 0 var(--ink); padding: 0.7rem 1.25rem; min-height: 44px; font: 700 1rem var(--font-body); cursor: pointer;
  transition: transform 0.1s, box-shadow 0.1s; }
.button:hover, .button:focus-visible { transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.button:active { transform: translate(4px, 4px); box-shadow: 0 0 0 var(--ink); }
.input { background: var(--surface); color: var(--text); border: var(--border); border-radius: var(--radius);
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { .button { transition: none; } }
```

## Accessibility traps

- **Everything shouts, so nothing leads.** With heavy borders and bright fills everywhere there is no hierarchy. Fix: use one saturated block per section and keep the rest neutral.
- **Movement as the only hover cue.** Keyboard users never see a hover shift. Fix: apply the same shift on `:focus-visible` and keep the outline, as the starter does.
- **Hard shadows clipped by containers.** `overflow: hidden` cuts off the offset shadow. Fix: leave margin at least as large as the shadow, or move the clip.
- **Yellow as text color.** Yellow on white or cream is nearly unreadable. Fix: use yellow only as a fill with black text.

## Pairs with

- Works with: bento-grid, playful-memphis (more shapes), terminal-mono.
- Do not mix with: glassmorphism, neumorphism, corporate-trust.
