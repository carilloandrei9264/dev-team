# Neon cyber

Near-black backgrounds with vivid neon accents, thin glowing lines, and a heads-up-display feel.

## Signature traits

- Near-black background with off-white text.
- One or two neon accents (cyan, magenta, lime), never more.
- Glow built from shadows, used on borders and headlines only.
- Techy display type and thin grid or HUD lines.
- Angular details and small labels in uppercase.

## Fits

- Gaming, esports, nightlife, music and tech events.
- Sci-fi and crypto-style products.

## Avoid when

- Long reading, health, children, trust-heavy finance.
- Anything where eye comfort matters.

## Tokens

```css
:root {
  /* color */
  --bg: #0A0A12;
  --surface: #14141F;
  --text: #E8F0FF;
  --muted: #9AA6C7;
  --primary: #00E5F0;
  --on-primary: #04121A;
  --accent: #FF2BD6;
  --focus: #00E5F0;
  /* shape, depth, type */
  --radius: 2px;
  --shadow: 0 0 0 1px rgba(0, 229, 240, 0.35), 0 0 24px rgba(0, 229, 240, 0.18);
  --font-display: "Orbitron", "Segoe UI", system-ui, sans-serif;
  --font-body: "Exo 2", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --glow: 0 0 24px rgba(0, 229, 240, 0.25);
}
```

Fonts (Google Fonts names): Orbitron for headings, Exo 2 for body. Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.7 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; letter-spacing: 0.04em; line-height: 1.2; margin: 0 0 0.6em; }
h1 { text-shadow: 0 0 14px rgba(0, 229, 240, 0.55); }
.card { background: var(--surface); border: 1px solid var(--primary); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: var(--radius);
  box-shadow: var(--glow); padding: 0.7rem 1.5rem; min-height: 44px; font: 700 0.9rem var(--font-display);
  letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer; }
.button:hover { box-shadow: 0 0 32px rgba(0, 229, 240, 0.5); }
.input { background: var(--bg); color: var(--text); border: 1px solid var(--muted); border-radius: var(--radius);
  padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Glow on body text.** A glow blurs letter edges and lowers contrast. Fix: apply glow only to headlines, borders, and buttons; body text stays solid.
- **Halation on dark backgrounds.** Bright text on near-black glares for some readers, especially with astigmatism. Fix: use off-white body text (not pure neon), at least 16px, line height 1.6 or more, and offer a light theme for long reading.
- **Angled corners that clip the focus ring.** `clip-path` also cuts off outlines. Fix: avoid `clip-path` on focusable elements, or draw the focus ring on a wrapper.
- **Blinking and flashing.** Flashing more than three times a second can trigger seizures. Fix: keep effects static and respect `prefers-reduced-motion`.
- **Neon colors vibrating together.** Two saturated colors next to each other strain the eye. Fix: one neon per section.

## Pairs with

- Works with: retro-pixel, terminal-mono, glassmorphism (dark).
- Do not mix with: organic-natural, editorial, corporate-trust.
