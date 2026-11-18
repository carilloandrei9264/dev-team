# Flat Material

Flat surfaces, tonal color, and clear elevation rules from Material Design 3; the natural choice for Android and for products that should feel native to Google platforms.

## Signature traits

- Color roles (primary, on-primary, surface, container, outline) instead of ad hoc colors.
- Surfaces separated by tone more than by shadow.
- Large rounded shapes (12 to 28px) and pill-shaped buttons.
- State layers and ripples on interaction.
- Roboto or another Google typeface.

## Fits

- Android apps and Android-first web apps.
- Admin tools and products where familiarity beats personality.

## Avoid when

- Brands that need strong individual character, unless you customize shape and type.

## Tokens

```css
:root {
  /* color */
  --bg: #F4FBF9;
  --surface: #E6F0EC;
  --text: #161D1C;
  --muted: #3F4947;
  --primary: #006A60;
  --on-primary: #FFFFFF;
  --accent: #7A5260;
  --focus: #006A60;
  /* shape, depth, type */
  --radius: 16px;
  --shadow: none;
  --font-display: "Roboto", "Segoe UI", system-ui, sans-serif;
  --font-body: "Roboto", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --outline: #6F7977;
}
```

Fonts (Google Fonts names): Roboto (Google Sans is not freely available; use Roboto or Inter). Load only the weights you use, and keep the fallback stack.

These tokens approximate Material 3 roles. For a real product, generate a full light and dark scheme with Material Theme Builder, and for Android apps also follow the Android reference (`../android.md`).

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.5 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 500; line-height: 1.2; margin: 0 0 0.5em; }
.card { background: var(--surface); border-radius: var(--radius); padding: 1.25rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: 999px;
  padding: 0.7rem 1.5rem; min-height: 48px; font: 500 1rem var(--font-body); cursor: pointer; }
.button:hover { box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3); }
.input { background: var(--bg); color: var(--text); border: 1px solid var(--outline); border-radius: 4px;
  padding: 0.8rem 1rem; min-height: 48px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
```

## Accessibility traps

- **Low-contrast tonal surfaces.** Container and surface tones can be too close to separate regions or show a field boundary. Fix: keep text on its on-surface role at 4.5:1 and give inputs an outline role that reaches 3:1 against its surface.
- **Small touch targets.** Compact density shrinks buttons below the minimum. Fix: keep 48dp (48px on web) for anything tappable.
- **Dynamic color overriding contrast.** Wallpaper-derived schemes can produce weak pairs. Fix: re-measure the generated scheme and keep a fixed fallback.

## Pairs with

- Works with: corporate-trust, bento-grid.
- Do not mix with: neo-brutalism, retro-pixel.
