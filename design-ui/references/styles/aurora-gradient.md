# Aurora gradient

Soft, blurred color fields behind clean white cards: a light, modern look with a sense of atmosphere.

## Signature traits

- A pale base with large blurred gradient blobs in two or three hues.
- Clean white or near-white cards that carry all the text.
- A modern geometric sans with generous spacing.
- Soft shadows and large radii.
- Optional fine grain to reduce banding.

## Fits

- Product launch pages, startup and AI products, event pages, hero sections.
- Creative tools that want a friendly, airy mood.

## Avoid when

- Dense data screens.
- When it is your only idea: soft purple-and-pink gradients are the most common generic look.

## Tokens

```css
:root {
  /* color */
  --bg: #F5FBFF;
  --surface: #FFFFFF;
  --text: #0B1B2B;
  --muted: #4A5D70;
  --primary: #0B6BCB;
  --on-primary: #FFFFFF;
  --accent: #D63A73;
  --focus: #0B6BCB;
  /* shape, depth, type */
  --radius: 20px;
  --shadow: 0 10px 30px rgba(11, 27, 43, 0.10);
  --font-display: "Sora", "Segoe UI", system-ui, sans-serif;
  --font-body: "Outfit", "Segoe UI", system-ui, sans-serif;
}
```

Fonts (Google Fonts names): Sora for headings, Outfit for body. Load only the weights you use, and keep the fallback stack.

Tie the gradient hues to the product (for example greens for a plant app) instead of the default purple-pink.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
body::before { content: ""; position: fixed; inset: 0; z-index: -1;
  background:
    radial-gradient(55% 45% at 12% 8%, rgba(11, 107, 203, 0.22), transparent 70%),
    radial-gradient(45% 40% at 88% 15%, rgba(214, 58, 115, 0.18), transparent 70%),
    radial-gradient(55% 45% at 50% 105%, rgba(15, 160, 140, 0.20), transparent 70%); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.15; margin: 0 0 0.5em; }
.card { background: var(--surface); border: 1px solid rgba(11, 27, 43, 0.08); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 999px;
  padding: 0.75rem 1.5rem; min-height: 44px; font: 600 1rem var(--font-body); cursor: pointer; }
.button:hover { filter: brightness(1.1); }
.input { background: var(--surface); color: var(--text); border: 1px solid var(--muted); border-radius: 14px;
  padding: 0.7rem 0.9rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Text directly on the gradient.** The gradient changes contrast from one spot to the next. Fix: put text on solid cards, or measure the worst spot and darken it with an overlay.
- **Gradient text.** Clipped gradient text can fall below the contrast limit at one end. Fix: make every gradient stop at least 4.5:1 (3:1 for headings of 24px and bold), and set a solid fallback color.
- **Large blurred layers are heavy.** Animated or many blurred layers drain phones. Fix: use one fixed, static CSS gradient layer, no animated blur, or a compressed pre-rendered image.
- **Looks generic.** Default purple-pink gradients are everywhere. Fix: derive the hues from the product and change shape and type to match.

## Pairs with

- Works with: bento-grid, minimal-swiss, glassmorphism, corporate-trust (lighter).
- Do not mix with: neumorphism, neo-brutalism, retro-pixel.
