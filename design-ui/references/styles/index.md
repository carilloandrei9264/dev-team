# Visual style catalog

A menu of visual styles for `design-ui`. Each style is one file with the same shape: signature traits, when it fits, when to avoid it, ready-to-use tokens, starter CSS, accessibility traps with fixes, and what it pairs with.

## How to use it

1. **Decide from the product first.** Who is it for, what should it feel like, where will it be used (see section 2 of `design-ui`). Never pick a style because it is fashionable.
2. **Pick one surface style** from the table. Add at most one layout style (`bento-grid`) on top. Do not combine two surface styles.
3. **Read only that style's file.** Copy its tokens into the project's CSS variables, and record the style name and the final tokens in `DESIGN.md`.
4. **Retune before building.** The starter palettes are neutral samples that pass contrast checks. Do not ship them unchanged: adjust hue, type, and shape to this product, then measure contrast again.
5. **Accessibility outranks style.** If a style's look conflicts with 4.5:1 text contrast, 3:1 control boundaries, 44px targets, a visible focus ring, or reduced motion, change the look, not the rule. The "Accessibility traps" in each file say how.

## The styles

| Style | Mood | Good for | Avoid for | Accessibility risk | Performance cost |
|-------|------|----------|-----------|--------------------|------------------|
| [Minimal Swiss](minimal-swiss.md) | Precise, calm, confident | Portfolios, docs, tools, studios | Kids, wellness, anything that needs warmth | low | low |
| [Corporate trust](corporate-trust.md) | Calm, dependable, clear | Finance, B2B, dashboards, admin | Playful or edgy brands | low | low |
| [Flat Material](flat-material.md) | Familiar, tidy, native | Android apps, familiar tools | Brands needing a strong identity | low | low |
| [Glassmorphism](glassmorphism.md) | Airy, modern, layered | Overlays, dashboards over rich backdrops | Text-heavy pages, low-end devices | high | medium |
| [Neumorphism (soft UI)](neumorphism.md) | Soft, tactile, quiet | A few big controls (smart home, timer) | Forms, text pages, accessibility-critical products | high | low |
| [Claymorphism](claymorphism.md) | Friendly, puffy, playful | Kids, education, casual apps, onboarding | Dense data, enterprise, premium or technical brands | medium | low |
| [Neo-brutalism](neo-brutalism.md) | Bold, loud, honest | Studios, indie products, bold brands | Formal, financial, long reading | low | low |
| [Bento grid](bento-grid.md) (layout) | Organized, modern, modular | Feature overviews, dashboards, portfolios (layout) | Long reading, ordered steps, checkout | low | low |
| [Editorial](editorial.md) | Literary, refined, image-led | Blogs, magazines, long reads, cultural sites | Dashboards, transactional flows | low | low |
| [Organic and natural](organic-natural.md) | Warm, calm, grounded | Wellness, food, plants, outdoors, craft | High-tech, fintech, dense data | medium | low |
| [Playful Memphis](playful-memphis.md) | Loud, joyful, energetic | Music, events, kids, creative campaigns | Serious, data-heavy, calm or premium brands | medium | low |
| [Retro pixel](retro-pixel.md) | Nostalgic, game-like, chunky | Games, nostalgia, community sites | Serious products, long reading | medium | low |
| [Neon cyber](neon-cyber.md) | Electric, nocturnal, futuristic | Gaming, nightlife, tech events | Long reading, health, kids, trust-heavy finance | high | medium |
| [Aurora gradient](aurora-gradient.md) | Fresh, luminous, optimistic | Launch pages, startups, hero sections | Dense data; as a default with no concept | medium | medium |
| [Terminal mono](terminal-mono.md) | Technical, focused, no-nonsense | Developer tools, docs, technical blogs | General consumers, long prose, warm brands | medium | low |

Accessibility risk is how easily the style produces a failing result if used carelessly (high means read its traps before starting). Performance cost is mostly blur, glow, and large gradient layers.

## Pick by situation

| Situation | First choice | Second choice |
|-----------|--------------|---------------|
| Bank, insurance, B2B dashboard, admin tool | corporate-trust | flat-material |
| Developer tool, CLI, API docs | terminal-mono | minimal-swiss |
| Portfolio for a designer or photographer | minimal-swiss | editorial |
| Blog, magazine, newsletter, long reads | editorial | minimal-swiss |
| Kids, education, friendly onboarding | claymorphism | playful-memphis |
| Indie product, creative studio, bold brand | neo-brutalism | playful-memphis |
| Wellness, food, plants, outdoors, craft | organic-natural | editorial |
| Music, festival, events | playful-memphis | aurora-gradient |
| Gaming, nightlife, esports | neon-cyber | retro-pixel |
| Retro games, nostalgia | retro-pixel | neon-cyber |
| Product or AI launch page | aurora-gradient | glassmorphism |
| Weather, music, or finance widgets over rich imagery | glassmorphism | aurora-gradient |
| A few big physical-style controls (timer, smart home) | neumorphism, as a decorative layer | claymorphism |
| Android app, or a product that should feel native to Google platforms | flat-material | corporate-trust |
| Feature overview, dashboard layout, "about me" page | bento-grid on top of any surface style | |

## The token contract

Every style defines the same tokens, so changing style means swapping one block of CSS variables and the components keep working. Build with `var(--token)`, never with raw values.

| Token | Meaning | Rule |
|-------|---------|------|
| `--bg` | page background | `--text` and `--muted` on it reach 4.5:1 |
| `--surface` | cards and panels | `--text` and `--muted` on it reach 4.5:1 |
| `--text` | main text | |
| `--muted` | secondary text | 4.5:1 on `--bg` and `--surface` |
| `--primary` | main action fill | `--on-primary` on it reaches 4.5:1 |
| `--on-primary` | text and icons on `--primary` | |
| `--accent` | decoration: shapes, highlights, shadows | not for body text; several accents measure below 4.5:1 |
| `--focus` | keyboard focus ring | 3:1 against `--bg` and `--surface` |
| `--radius`, `--shadow` | shape and depth | |
| `--font-display`, `--font-body` | type, with fallbacks | at most two families |

A style may add extra tokens (for example `--glass`). Every starter CSS defines `.card`, `.button`, `.input`, and `:focus-visible`, and uses only `var()` tokens, with no raw color values.

## Combining styles

- One surface style plus at most one layout style. `bento-grid` is the only layout style so far.
- Borrow single techniques, not whole styles: for example the soft shadow from `organic-natural` on an `editorial` page is fine; glass panels on a neo-brutalist page is not.
- Each file lists what it works with and what to avoid mixing.

## When the style you need is not listed

Pick the closest file, copy its structure, and write the new style in the same shape: traits, fits, avoid, tokens that pass the contract, starter CSS, traps with fixes, pairings. Add a row to the table above. Skeuomorphic, cottagecore, and Y2K are not covered yet.
