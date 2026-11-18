# Glassmorphism

Frosted, translucent panels floating over a colorful backdrop; depth comes from blur, not from shadows.

## Signature traits

- Translucent panels with a background blur (`backdrop-filter`).
- A thin, light border on each panel to catch the edge.
- A colorful or gradient backdrop behind the glass; without it the effect disappears.
- Soft shadow, generous radius, light type on a dark base.
- One or two glass layers at most.

## Fits

- Dashboards and widgets over rich backdrops (weather, music, finance overviews).
- Hero sections and overlays where depth helps orientation.

## Avoid when

- Text-heavy pages: reading over a blurred, shifting background tires users.
- Low-power devices and long scrolling lists (blur is costly).
- Products that need maximum legibility (public services, health).

## Tokens

```css
:root {
  /* color */
  --bg: #0B1220;
  --surface: #1B2740;
  --text: #F5F7FF;
  --muted: #B8C3DE;
  --primary: #7DD3FC;
  --on-primary: #08111F;
  --accent: #F0ABFC;
  --focus: #7DD3FC;
  /* shape, depth, type */
  --radius: 20px;
  --shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
  --font-display: "Plus Jakarta Sans", "Segoe UI", system-ui, sans-serif;
  --font-body: "Plus Jakarta Sans", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --glass: rgba(27, 39, 64, 0.55);
  --glass-border: rgba(255, 255, 255, 0.28);
  --blur: 16px;
}
```

Fonts (Google Fonts names): Plus Jakarta Sans (DM Sans or Outfit also work). Load only the weights you use, and keep the fallback stack.

`--glass` is the `--surface` color made translucent. It stays dark on purpose: a white-tinted panel gets lighter wherever a bright color sits behind it and drags light text below the contrast limit. `--surface` is the solid fallback, and contrast is measured against it.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; min-height: 100vh; color: var(--text); font: 400 1rem/1.6 var(--font-body);
  background:
    radial-gradient(40% 35% at 15% 10%, rgba(125, 211, 252, 0.35), transparent 70%),
    radial-gradient(35% 30% at 90% 85%, rgba(240, 171, 252, 0.30), transparent 70%),
    var(--bg); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.2; margin: 0 0 0.5em; }
.card { background: var(--surface); background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.5rem;
  -webkit-backdrop-filter: blur(var(--blur)) saturate(140%); backdrop-filter: blur(var(--blur)) saturate(140%); }
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) { .card { background: var(--surface); } }
@media (prefers-reduced-transparency: reduce) { .card { background: var(--surface); -webkit-backdrop-filter: none; backdrop-filter: none; } }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 12px;
  padding: 0.7rem 1.25rem; min-height: 44px; font: 600 1rem var(--font-body); cursor: pointer; }
.input { background: rgba(255, 255, 255, 0.08); color: var(--text); border: 1px solid var(--glass-border);
  border-radius: 12px; padding: 0.7rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Text over a changing background.** Contrast depends on what sits behind the glass, which changes with content and scroll. Fix: keep the panel tint dark and fairly opaque (about 55%), measure the lightest spot behind it, and keep a solid fallback color.
- **No fallback when blur is unsupported.** Without `backdrop-filter` the panel becomes see-through text over a busy backdrop. Fix: keep the `@supports not` rule so the panel turns solid.
- **Blur is expensive.** Many blurred layers or large areas drop frame rates and drain batteries on phones. Fix: limit to one or two layers, keep blur at 8 to 20px, never animate the blur radius.
- **Faint borders disappear.** A 1px translucent edge is the only boundary of the panel and of inputs. Fix: keep input borders at 3:1 or give inputs a more opaque fill.
- **Users who reduce transparency.** Some operating systems offer a reduced-transparency setting. Fix: where supported, honor `prefers-reduced-transparency` by switching panels to the solid `--surface`.

## Pairs with

- Works with: aurora-gradient (backdrop), neon-cyber (dark), bento-grid (tiles as glass).
- Do not mix with: neumorphism, neo-brutalism, editorial.
