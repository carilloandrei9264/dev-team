# Neumorphism (soft UI)

Elements look gently pushed out of, or pressed into, a surface of the same color, using one light and one dark shadow.

## Signature traits

- Background and elements share one muted color.
- A light shadow on one side and a dark shadow on the other create raised and pressed states.
- Very soft, low-contrast, mostly monochrome palette.
- Large radii and few elements per screen.
- Controls look like physical buttons, knobs, and switches.

## Fits

- Single-purpose control panels with a few big controls (smart home, music player, calculator, timer).
- Concept screens where the mood matters more than information density.

## Avoid when

- Forms, text-heavy pages, tables, and anything that needs clear affordance.
- Public, health, government, or other accessibility-critical products.

## Tokens

```css
:root {
  /* color */
  --bg: #E0E5EC;
  --surface: #E0E5EC;
  --text: #1F2937;
  --muted: #4B5563;
  --primary: #3B4FC4;
  --on-primary: #FFFFFF;
  --accent: #C2410C;
  --focus: #3B4FC4;
  /* shape, depth, type */
  --radius: 20px;
  --shadow: 8px 8px 16px #A3B1C6, -8px -8px 16px #FFFFFF;
  --font-display: "Nunito Sans", "Segoe UI", system-ui, sans-serif;
  --font-body: "Nunito Sans", "Segoe UI", system-ui, sans-serif;
  /* style extras */
  --shadow-light: #FFFFFF;
  --shadow-dark: #A3B1C6;
  --edge: #5B6472;
}
```

Fonts (Google Fonts names): Nunito Sans (Poppins or DM Sans also work). Load only the weights you use, and keep the fallback stack.

Treat this style as a decorative layer for a few controls, not a whole-product style. `--edge` and the filled primary button are what keep it usable.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 1rem/1.6 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.2; margin: 0 0 0.5em; }
.card { background: var(--surface); border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.5rem; }
.button { background: var(--primary); color: var(--on-primary); border: 0; border-radius: var(--radius);
  box-shadow: 4px 4px 8px var(--shadow-dark), -4px -4px 8px var(--shadow-light);
  padding: 0.7rem 1.5rem; min-height: 44px; font: 700 1rem var(--font-body); cursor: pointer; }
.button:active { box-shadow: inset 3px 3px 6px rgba(0, 0, 0, 0.35); }
.input { background: var(--bg); color: var(--text); border: 2px solid var(--edge); border-radius: 14px;
  box-shadow: inset 4px 4px 8px var(--shadow-dark), inset -4px -4px 8px var(--shadow-light);
  padding: 0.7rem 0.9rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

## Accessibility traps

- **Controls with no visible boundary.** A raised shape on the same color fails the 3:1 contrast needed for interface components. Fix: give inputs and secondary controls a 2px `--edge` border (measured above 3:1) and fill the primary button with a solid color.
- **Raised versus pressed is hard to tell.** The state difference is a faint shadow change. Fix: pair every state change with a color, icon, or text change (a tick, an On label).
- **Invisible focus.** Shadows hide the default focus ring. Fix: always add the `:focus-visible` outline.
- **Dark mode breaks the trick.** The light shadow has nothing to lighten on a dark surface. Fix: define separate shadow tokens for dark, or do not use this style in dark mode.

## Pairs with

- Works with: claymorphism (softer, more colorful cousin), minimal-swiss.
- Do not mix with: glassmorphism, neo-brutalism, neon-cyber.
