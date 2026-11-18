# Minimal Swiss

Typography, grid, and whitespace do all the work; almost no decoration.

## Signature traits

- Strict grid, generous whitespace, strong left alignment.
- One neo-grotesque typeface in a few sizes and weights; hierarchy comes from scale and weight, not from color.
- Mostly black and white with one sharp accent used sparingly.
- Hairline rules instead of boxes and shadows; square corners.
- Photography or one bold graphic as the only imagery.

## Fits

- Portfolios, studios, documentation, and tools where the content is the product.
- Brands that want to feel serious and confident.

## Avoid when

- Audiences that expect warmth or play (kids, wellness, food).
- Brands with nothing distinctive to say: minimalism over weak content just looks empty.

## Tokens

```css
:root {
  /* color */
  --bg: #FFFFFF;
  --surface: #F4F4F2;
  --text: #111111;
  --muted: #595959;
  --primary: #111111;
  --on-primary: #FFFFFF;
  --accent: #D6001C;
  --focus: #D6001C;
  /* shape, depth, type */
  --radius: 0;
  --shadow: none;
  --font-display: "Work Sans", "Helvetica Neue", Arial, sans-serif;
  --font-body: "Work Sans", "Helvetica Neue", Arial, sans-serif;
  /* style extras */
  --rule: 1px solid #111111;
}
```

Fonts (Google Fonts names): Work Sans (Inter, Archivo, or Helvetica Neue also work). Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin: 0 0 0.5em; }
h1 { font-size: clamp(2.25rem, 6vw, 4rem); }
.card { background: var(--surface); border-top: var(--rule); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: var(--radius);
  padding: 0.75rem 1.25rem; min-height: 44px; font: 600 1rem var(--font-body); cursor: pointer; }
.button:hover { background: var(--accent); }
.input { background: var(--bg); color: var(--text); border: var(--rule); border-radius: var(--radius);
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Light-gray text.** Pale gray on white looks elegant and fails contrast. Fix: keep muted text at 4.5:1 or better (the token here measures about 7:1) and never go lighter for body copy.
- **Hierarchy collapses without decoration.** When everything is the same size, nothing leads. Fix: use a clear type scale (for example 14, 16, 24, 40, 72) and one primary action per view.
- **Tiny type for elegance.** Small, light type is hard to read. Fix: body at 16px or larger, line length 45 to 75 characters.

## Pairs with

- Works with: bento-grid (Swiss-style tiles), editorial type, corporate-trust (calmer).
- Do not mix with: glassmorphism, neumorphism (their effects fight the restraint).
