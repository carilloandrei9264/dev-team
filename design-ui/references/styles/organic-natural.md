# Organic and natural

Earthy color, soft irregular shapes, and hand-made touches that feel grown rather than manufactured.

## Signature traits

- Earth palette: leaf green, clay, sand, cream, deep forest.
- Soft, slightly irregular radii and blob shapes instead of perfect rectangles.
- Hand-drawn lines, botanical or line-art illustrations, light paper grain.
- Rounded humanist type or a soft serif.
- Gentle shadows, natural photography, a calm pace.

## Fits

- Wellness, food, plants and gardening, outdoors.
- Eco and sustainability brands, craft shops, journaling and habit apps.

## Avoid when

- High-tech, fintech, and enterprise brands.
- Claiming to be natural when the product is not (it reads as greenwashing).
- Dense data screens.

## Tokens

```css
:root {
  /* color */
  --bg: #F6F1E7;
  --surface: #FBF8F1;
  --text: #26301F;
  --muted: #55604A;
  --primary: #3F6B3A;
  --on-primary: #FFFFFF;
  --accent: #B8612B;
  --focus: #3F6B3A;
  /* shape, depth, type */
  --radius: 28px 44px 30px 40px;
  --shadow: 0 10px 30px rgba(63, 107, 58, 0.14);
  --font-display: "Fraunces", Georgia, serif;
  --font-body: "Nunito", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --leaf: #6F9E5F;
}
```

Fonts (Google Fonts names): Fraunces for headings, Nunito for body. Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1.0625rem/1.65 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 600; line-height: 1.15; margin: 0 0 0.5em; }
.card { background: var(--surface); border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.75rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 999px;
  padding: 0.75rem 1.75rem; min-height: 46px; font: 700 1rem var(--font-body); cursor: pointer; }
.button:hover { background: var(--text); }
.input { background: var(--bg); color: var(--text); border: 2px solid var(--muted); border-radius: 16px 22px 16px 22px;
  padding: 0.7rem 1rem; min-height: 46px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Sage and pastel text.** Muted greens and beiges read as calm and measure as weak contrast. Fix: use the deep green text token (about 12:1) and keep the muted token at 4.5:1 or better; re-measure after tuning any color.
- **Decoration that weighs a lot.** Raster grain and big illustrations slow pages. Fix: use small inline SVGs, compress images, avoid full-page grain images, and mark decorative shapes `aria-hidden`.
- **Irregular radii that do not line up.** Every element with a different curve looks messy. Fix: define two or three radius tokens and reuse them.
- **Green meaning good.** Status by color alone fails for color-blind users. Fix: add an icon and a label to every status.

## Pairs with

- Works with: editorial, claymorphism (softer), bento-grid.
- Do not mix with: neon-cyber, glassmorphism, terminal-mono.
