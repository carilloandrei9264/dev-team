# Playful Memphis

Eighties Memphis energy: clashing bright colors, squiggles, triangles, dots, and tilted shapes.

## Signature traits

- Bold, clashing colors with thick dark outlines.
- Geometric decoration: circles, triangles, zigzags, dots, squiggles.
- Patterns used as accents, not as backgrounds behind text.
- Slight tilts on cards and shapes.
- Chunky rounded type.

## Fits

- Music, events, festivals, kids brands.
- Creative campaigns and onboarding with personality.

## Avoid when

- Serious or data-heavy products.
- Long reading.
- Brands that need to feel calm or premium.

## Tokens

```css
:root {
  /* color */
  --bg: #FFFBEB;
  --surface: #FFFFFF;
  --text: #1F1B4D;
  --muted: #4B4780;
  --primary: #D0125E;
  --on-primary: #FFFFFF;
  --accent: #00A896;
  --focus: #D0125E;
  /* shape, depth, type */
  --radius: 20px;
  --shadow: 8px 8px 0 #00A896;
  --font-display: "Rubik", "Trebuchet MS", system-ui, sans-serif;
  --font-body: "DM Sans", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --accent-2: #FFD23F;
  --ink: #1F1B4D;
}
```

Fonts (Google Fonts names): Rubik for headings (weight 800), DM Sans for body. Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 800; line-height: 1.1; margin: 0 0 0.5em; }
.card { position: relative; background: var(--surface); border: 3px solid var(--ink); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 1.5rem; transform: rotate(-1deg); }
.card::before { content: ""; position: absolute; top: -16px; right: 24px; width: 32px; height: 32px;
  border-radius: 50%; background: var(--accent-2); border: 3px solid var(--ink); }
.button { background: var(--primary); color: var(--on-primary); border: 3px solid var(--ink); border-radius: 999px;
  padding: 0.7rem 1.5rem; min-height: 44px; font: 700 1rem var(--font-body); cursor: pointer; }
.button:hover { background: var(--ink); }
.input { background: var(--surface); color: var(--text); border: 3px solid var(--ink); border-radius: 14px;
  padding: 0.7rem 0.9rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { .card { transform: none; } }
```

## Accessibility traps

- **Busy patterns behind text.** Dots and zigzags under copy break up the letters. Fix: keep patterns in margins and hero backgrounds and set text on solid surfaces.
- **Tilted text blocks.** Rotated paragraphs are harder to read and misbehave when zoomed. Fix: tilt decorative shapes and cards by 2 degrees at most, never long text, and turn it off for reduced motion.
- **Too many colors, no hierarchy.** Five bright colors compete. Fix: one primary, two supporting colors, and one job per color.
- **Accent colors as text.** The teal and yellow accents measure below 4.5:1 on light backgrounds. Fix: use accents for shapes and shadows only; text stays on the dark ink token.

## Pairs with

- Works with: claymorphism, neo-brutalism (shared boldness), bento-grid.
- Do not mix with: corporate-trust, minimal-swiss, editorial.
