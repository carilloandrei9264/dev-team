# Terminal mono

Monospace type, prompt symbols, and a command-line feel for people who live in terminals.

## Signature traits

- Monospace for everything or for all UI chrome.
- A dark background (or warm paper for a light variant) with one phosphor accent.
- Prompt symbols like `$` and `>` and box-drawing borders.
- Flat, with no shadows or gradients.
- Keyboard-first patterns, command palettes, copy buttons.

## Fits

- Developer tools, CLIs, API docs.
- Security and hacker blogs, technical portfolios.

## Avoid when

- General consumers.
- Long non-technical reading (monospace slows it).
- Marketing that needs warmth.

## Tokens

```css
:root {
  /* color */
  --bg: #0B0F0B;
  --surface: #121812;
  --text: #C8F7C5;
  --muted: #8FB38C;
  --primary: #4ADE80;
  --on-primary: #04140A;
  --accent: #FFB000;
  --focus: #FFB000;
  /* shape, depth, type */
  --radius: 2px;
  --shadow: none;
  --font-display: "JetBrains Mono", "Fira Code", Consolas, monospace;
  --font-body: "JetBrains Mono", "Fira Code", Consolas, monospace;
}
```

Fonts (Google Fonts names): JetBrains Mono (IBM Plex Mono and Fira Code also work). Load only the weights you use, and keep the fallback stack.

## Starter CSS

Uses only the tokens above and defines the shared classes `.card`, `.button`, and `.input`, plus a visible focus ring. Retune before shipping.

```css
body { margin: 0; background: var(--bg); color: var(--text); font: 400 0.95rem/1.7 var(--font-body); }
h1, h2 { font-family: var(--font-display); font-weight: 700; line-height: 1.3; margin: 0 0 0.6em; }
h2::before { content: "$ "; color: var(--accent); }
.card { background: var(--surface); border: 1px solid var(--muted); border-radius: var(--radius); padding: 1.25rem; }
.button { background: transparent; color: var(--primary); border: 1px solid var(--primary); border-radius: var(--radius);
  padding: 0.6rem 1.1rem; min-height: 44px; font: 600 0.95rem var(--font-body); cursor: pointer; }
.button:hover { background: var(--primary); color: var(--on-primary); }
.input { background: var(--bg); color: var(--text); border: 1px solid var(--muted); border-radius: var(--radius);
  padding: 0.65rem 0.8rem; min-height: 44px; font: inherit; }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
```

## Accessibility traps

- **Dim green on black.** The classic dark-green terminal palette fails contrast. Fix: use the measured tokens (muted about 8:1) and avoid pure `#00FF00` for body text.
- **Monospace for long paragraphs.** Fixed-width letters slow reading. Fix: use mono for UI, code, and headings; use a proportional font for long prose, or cap lines at 70 characters.
- **A fake terminal that is an image or not selectable.** Users cannot copy commands or use assistive tech. Fix: use real text, keep it selectable, and add copy buttons to commands.
- **Blinking cursors.** Constant blinking distracts and can bother some users. Fix: keep it static or respect `prefers-reduced-motion`.

## Pairs with

- Works with: neon-cyber, retro-pixel, minimal-swiss (light variant).
- Do not mix with: organic-natural, claymorphism, playful-memphis.
