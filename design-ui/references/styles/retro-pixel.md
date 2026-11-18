# Retro pixel

Eight- and sixteen-bit video game styling: pixel type, stepped borders, and a tight palette.

## Signature traits

- Pixel font for headings and labels only.
- Stepped, blur-free borders and shadows built from solid blocks.
- A limited palette on a dark base with one bright highlight.
- Crisp scaling of pixel art with `image-rendering: pixelated`.
- Chunky buttons that visibly press down.

## Fits

- Games, game developer portfolios, retro tools.
- Nostalgic campaigns and community sites.

## Avoid when

- Serious products and long reading.
- Anything that needs quick scanning of lots of text.

## Tokens

```css
:root {
  /* color */
  --bg: #1A1033;
  --surface: #2A1B4D;
  --text: #F8F4E3;
  --muted: #C9BFE8;
  --primary: #FFD23F;
  --on-primary: #1A1033;
  --accent: #4ADE80;
  --focus: #FFD23F;
  /* shape, depth, type */
  --radius: 0;
  --shadow: 4px 4px 0 #000000;
  --font-display: "Press Start 2P", "Courier New", monospace;
  --font-body: "IBM Plex Mono", "Courier New", monospace;
  /* style extras */
  --pixel: 4px;
}
```

Fonts (Google Fonts names): Press Start 2P for headings (400 only), IBM Plex Mono for body. Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.7 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 400; line-height: 1.5; margin: 0 0 0.75em; }
h1 { font-size: clamp(1.25rem, 4vw, 2rem); }
h2 { font-size: 1rem; }
.card { background: var(--surface); border: var(--pixel) solid var(--text); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: var(--pixel) solid var(--text); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 0.7rem 1.25rem; min-height: 44px; font: 400 0.875rem var(--font-display); cursor: pointer; }
.button:active { transform: translate(4px, 4px); box-shadow: none; }
.input { background: var(--bg); color: var(--text); border: var(--pixel) solid var(--muted); border-radius: var(--radius);
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
img, canvas { image-rendering: pixelated; }
:focus-visible { outline: var(--pixel) solid var(--focus); outline-offset: 2px; }
```

## Accessibility traps

- **Pixel font for body text.** Press Start 2P is hard to read beyond a few words. Fix: use it for headings and labels at 14px or more and set body in a readable monospace at 16px or more.
- **Blurry sprites.** Browsers smooth scaled images by default. Fix: set `image-rendering: pixelated` and scale by whole numbers.
- **Flicker and scanline effects.** They cause discomfort and can trigger seizures. Fix: keep the page static, avoid flashing more than three times a second, and respect `prefers-reduced-motion`.
- **Dark purple chrome with weak contrast.** Dark-on-dark borders disappear. Fix: measure borders and muted text, as the token set already does.

## Pairs with

- Works with: neon-cyber (dark), playful-memphis, terminal-mono.
- Do not mix with: corporate-trust, editorial, glassmorphism.
