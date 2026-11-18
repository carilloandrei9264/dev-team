# Editorial

Magazine and newspaper design on screen: big serif headlines, readable text, rules, captions, and confident photography.

## Signature traits

- A display serif for headlines at large sizes and a readable text face for body.
- Strong contrast in scale between headline, deck, and body.
- Thin rules, columns, captions, and pull quotes as structure.
- A paper-toned background and a restrained palette with one ink color.
- Generous margins and image crops chosen on purpose.

## Fits

- Blogs, magazines, newsletters, long-form stories.
- Portfolios for writers and photographers, restaurants, cultural organizations.

## Avoid when

- Dense dashboards and tools.
- Transactional flows where speed matters more than mood.

## Tokens

```css
:root {
  /* color */
  --bg: #FBF7F0;
  --surface: #FFFFFF;
  --text: #1B1B1B;
  --muted: #5A5348;
  --primary: #8C1C13;
  --on-primary: #FFFFFF;
  --accent: #A66A00;
  --focus: #8C1C13;
  /* shape, depth, type */
  --radius: 0;
  --shadow: none;
  --font-display: "Playfair Display", Georgia, "Times New Roman", serif;
  --font-body: "Source Serif 4", Georgia, "Times New Roman", serif;
  /* style extras */
  --measure: 68ch;
}
```

Fonts (Google Fonts names): Playfair Display for headlines, Source Serif 4 for body (Fraunces and Newsreader are good alternatives). Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1.125rem/1.7 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.1; letter-spacing: -0.01em; margin: 0 0 0.5em; }
h1 { font-size: clamp(2.5rem, 7vw, 4.5rem); }
p { max-width: var(--measure); }
.card { background: var(--surface); border-top: 3px double var(--text); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: var(--radius);
  padding: 0.75rem 1.5rem; min-height: 44px; font: 600 0.8125rem var(--font-body); letter-spacing: 0.12em;
  text-transform: uppercase; cursor: pointer; }
.button:hover { background: var(--text); }
.input { background: var(--surface); color: var(--text); border: 0; border-bottom: 2px solid var(--text);
  border-radius: var(--radius); padding: 0.7rem 0.2rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Long lines in wide columns.** Big screens stretch body text to unreadable lengths. Fix: cap body text at 60 to 75 characters with `max-width: var(--measure)`.
- **Display serif at small sizes.** Fine hairlines in display faces break up below about 28px. Fix: use the display face only for large headlines and a text-optimized face for body.
- **Font weight bloat.** Several families and weights slow the first paint. Fix: load at most two families and three weights, with `font-display: swap`.
- **Justified text with gaps.** Justified text on narrow columns creates uneven spacing. Fix: left-align, or justify only wide columns with `hyphens: auto`.

## Pairs with

- Works with: minimal-swiss, organic-natural, bento-grid (for a magazine front page).
- Do not mix with: neon-cyber, retro-pixel, claymorphism.
