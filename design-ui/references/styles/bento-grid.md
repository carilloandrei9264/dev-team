# Bento grid

A layout pattern more than a look: rounded tiles of different sizes, each holding one idea, packed into a tidy grid.

## Signature traits

- Tiles span one or two columns and rows, with one clearly largest hero tile.
- Consistent gap (12 to 24px) and corner radius across all tiles.
- Each tile has one idea: a number, an image, a quote, a feature.
- Tiles may use different background tones from the palette.
- Collapses to a single column on small screens.

## Fits

- Feature overviews, product landing pages, dashboards.
- Portfolio and about-me pages.

## Avoid when

- Long-form reading and step-by-step instructions, where order matters.
- Checkout and forms.

## Tokens

```css
:root {
  /* color */
  --bg: #F0F0EC;
  --surface: #FFFFFF;
  --text: #1A1A1A;
  --muted: #555555;
  --primary: #2F5BEA;
  --on-primary: #FFFFFF;
  --accent: #E8590C;
  --focus: #2F5BEA;
  /* shape, depth, type */
  --radius: 24px;
  --shadow: none;
  --font-display: "DM Sans", "Segoe UI", system-ui, sans-serif;
  --font-body: "DM Sans", "Segoe UI", system-ui, sans-serif;
}
```

Fonts (Google Fonts names): DM Sans (any clean sans works; the layout carries the style). Load only the weights you use, and keep the fallback stack.

This is a layout style. Combine it with one surface style (minimal-swiss, neo-brutalism, corporate-trust, aurora-gradient) instead of using it alone.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; padding: 1rem; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.15; margin: 0 0 0.5em; }
.bento { display: grid; gap: 1rem; grid-template-columns: repeat(4, 1fr); grid-auto-rows: minmax(140px, auto); }
.bento .wide { grid-column: span 2; }
.bento .tall { grid-row: span 2; }
.card { background: var(--surface); border-radius: var(--radius); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 999px;
  padding: 0.7rem 1.25rem; min-height: 44px; font: 600 1rem var(--font-body); cursor: pointer; }
.input { background: var(--bg); color: var(--text); border: 1px solid var(--muted); border-radius: 12px;
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
@media (max-width: 700px) { .bento { grid-template-columns: 1fr; } .bento .wide, .bento .tall { grid-column: auto; grid-row: auto; } }
```

## Accessibility traps

- **Visual order differs from reading order.** `order` or `grid-auto-flow: dense` can put tiles in an order that screen readers and keyboards do not follow. Fix: write tiles in reading order in the HTML, avoid `dense`, and place with `grid-template-areas` that follow the DOM.
- **Too many equal tiles.** Nine tiles of the same weight give no entry point. Fix: one hero tile, six to eight tiles at most.
- **Text overflow in small tiles.** Real copy is longer than sample copy. Fix: use `minmax()` row heights and test worst-case content.
- **Spans leave gaps on phones.** Multi-column spans do not fit a narrow screen. Fix: collapse to one column below about 700px, as the starter does.

## Pairs with

- Works with: any surface style: minimal-swiss, neo-brutalism, corporate-trust, aurora-gradient, glassmorphism.
- Do not mix with: a second layout style (keep one layout idea per page).
