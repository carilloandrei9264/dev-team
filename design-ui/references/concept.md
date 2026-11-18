# Idea to design concept

Goal: a design that could only belong to this product, derived from the idea itself instead of from a template. Do this before choosing a style from `styles/index.md`.

## Contents
1. When to use it
2. The six steps
3. Guardrails: usability beats theme
4. The DESIGN.md concept template
5. Worked examples

## 1. When to use it

- A new project, or the user gives only an idea ("a simple website for tracking plant growth").
- The user says the result looks generic.
- Skip it when the project already has a brand, design system, or approved pages: extend those instead.
- Keep it proportionate. For a small site this is a few minutes of thinking and about fifteen lines in DESIGN.md, not a workshop.

## 2. The six steps

1. **Read the idea.** Write one line each for the *subject* (what it is about), the *user* (who, when, on what device), the *core action* (one verb: log, order, read, compare), and the *feeling* (three words, for example calm, proud, curious). If something is missing, assume it and say so in one line. Ask at most one question, and only if the answer would change the design.
2. **Collect the domain's vocabulary.** List five to eight concrete things from the subject's real world: objects, materials, shapes, colors, textures, rhythms, and the words people use. Be specific: "terracotta pot, sprout, leaf veins, tree rings, watering can", not "nature". Look for structure the subject already has: growth over time, stages, cycles, counting, layers.
3. **Pick one central metaphor.** One idea that links the product's data to an image: "growth is a stem that gets taller", "the menu is a roast chart", "each client is a ledger page". The metaphor must carry information (progress, status, history), not just decorate. If you cannot say what it shows about the data, pick another.
4. **Translate it into design decisions** with the table below. Everything the user sees should trace back to the vocabulary or the metaphor.
5. **Choose the surface style.** Match the feeling and the metaphor to a style in `styles/index.md` and read its "Avoid for" column. Then retune its tokens: hue from the domain's real colors, type character, radius. Never ship the starter tokens unchanged.
6. **Write it down and check it.** Fill in the concept template below in DESIGN.md, then run the guardrails. The next session reads this file instead of guessing.

| Decision | Ask | Plant tracker |
|----------|-----|---------------|
| Palette | Which two or three real colors does the subject have? Which one is the primary? | leaf green primary, terracotta accent, cream and soil neutrals |
| Type | What is the character: handmade, precise, loud, quiet, technical? | a soft serif for headings (warmth, growth), a rounded sans for data |
| Shape | Which shapes does the domain have: round, angular, layered, irregular? | leaf-like asymmetric corners, round pill buttons |
| Imagery | What can be drawn simply and tells the story? How heavy may it be? | a small inline-SVG sprig as logo and as progress mark; no stock photos |
| Data display | How can a chart or progress bar become the metaphor? | height over time drawn as a stem that grows; weekly growth as rings |
| Components and states | Which states can wear the theme: empty, success, loading, milestones? | empty is a seed, a new measurement adds a leaf, a milestone is a bloom badge |
| Motion | What moves in the real world, and what does the movement mean? | a slow grow when a value increases; nothing else moves |
| Microcopy | What would a person in this domain say? Keep labels plain. | "Add plant", "Log growth"; empty state: "No plants yet. Start with a seed." |

## 3. Guardrails: usability beats theme

- **Theme the decoration, not the function.** Color, shape, illustration, empty and success states, and copy carry the concept. Navigation, forms, labels, and data tables stay plain and conventional.
- **Do not rename core actions into cute words.** "Log growth" is fine; "Sprinkle some sunshine" is not. Every icon-only control gets a text label or an accessible name.
- **One metaphor and at most one repeated motif.** Leaves, rain, sun, and soil icons on one page is clutter, not a concept.
- **It must still work without the art.** If an illustration fails to load, the page stays clear.
- **Keep decoration light and quiet.** Small inline SVG, `aria-hidden="true"` on purely decorative shapes, no heavy images, and respect `prefers-reduced-motion`.
- **Re-measure after retuning.** 4.5:1 for text, 3:1 for the focus ring and control boundaries. Changing hue changes contrast.
- **Do not imply what the product cannot back.** A "natural" look for a product that is not, or a clinical look for a non-medical app, misleads people.
- **Swap test.** If you could replace the subject (plants with invoices) and keep every decision, the concept is generic. Go back to step 2.

## 4. The DESIGN.md concept template

```markdown
# DESIGN

## Concept
- **Idea:** [subject, user, core action]
- **Feeling:** [three words]
- **Metaphor:** [one sentence, and what it shows about the data]
- **Vocabulary:** [five to eight domain things]

## Style
**Style:** [catalog name, retuned]. **Why:** [one line, from the feeling and the metaphor]

## Tokens
[the final :root block, contrast measured]

## Signature parts
- [component or state that wears the concept, and what it shows]

## Stays plain
- [navigation, forms, labels, data tables]

## Avoid
- [clichés, effects, or styles ruled out]
```

## 5. Worked examples

Each example shows the output of the six steps for a different kind of product. The palettes pass the same contrast limits as the style catalog.

### Plant growth tracker

**Idea:** a simple site where one person logs how their houseplants grow. Core action: log a measurement.
**Feeling:** calm, patient, proud.
**Metaphor:** growth is a stem that gets taller. Each plant's history is a stem drawn to its measured height, and weeks are rings.
**Style:** organic-natural, retuned: warmer cream, deeper leaf green, one terracotta accent.

```css
:root {
  --bg: #F3EFE4; --surface: #FFFDF7; --text: #22301F; --muted: #56604A;
  --primary: #2F6B3B; --on-primary: #FFFFFF; --accent: #C4622D; --focus: #2F6B3B;
  --radius: 28px 44px 30px 40px;
  --font-display: "Fraunces", Georgia, serif; --font-body: "Nunito", system-ui, sans-serif;
}
```

**Signature parts:** a small sprig as the logo mark; plant cards that draw a stem to the latest height; a seed in the empty state; a leaf that appears after each logged measurement; a bloom badge at milestones such as 20 cm.
**Stays plain:** the add-plant form (visible labels, number input with its unit), the measurement table, navigation, error messages.
**Avoid:** stock plant photos, rain and sun icons everywhere, a gradient hero, "bloom" or "water" as button labels.

### Coffee roaster's order page

**Idea:** a small roastery sells beans online. Core action: choose a bag and order it.
**Feeling:** warm, crafted, unhurried.
**Metaphor:** the roast profile. Each coffee is shown the way a roaster describes it: a short curve from green to dark and a label like the one on the bag.
**Style:** editorial, on a cream-and-brown paper tone with bag-label typography.

```css
:root {
  --bg: #F5EDE0; --surface: #FFFAF2; --text: #2A1B12; --muted: #5E4A3C;
  --primary: #6B2D14; --on-primary: #FFF7EC; --accent: #C98A2B; --focus: #6B2D14;
  --radius: 0;
  --font-display: "Playfair Display", Georgia, serif; --font-body: "Source Serif 4", Georgia, serif;
}
```

**Signature parts:** the roast level as a tiny curve plus a five-step scale; tasting notes set like a bag label; origin in small caps with a rule; a "roasted on" date stamp.
**Stays plain:** the product list, quantity and grind selectors, cart, and checkout.
**Avoid:** rustic wood textures, coffee-bean clip art, script fonts.

### Bedtime reading app for kids

**Idea:** parents and children read short stories together before sleep. Core action: start tonight's story.
**Feeling:** sleepy, safe, gentle.
**Metaphor:** the night sky. Each finished story lights a star, and weekly progress is a row of stars.
**Style:** claymorphism, night variant: an indigo base, puffy shapes, and one moon-yellow primary.

```css
:root {
  --bg: #22204F; --surface: #2E2B66; --text: #FFF6DD; --muted: #CFCBF0;
  --primary: #FFD66B; --on-primary: #2A2200; --accent: #7FD6C2; --focus: #FFD66B;
  --radius: 28px;
  --font-display: "Fredoka", "Trebuchet MS", sans-serif; --font-body: "Nunito", system-ui, sans-serif;
}
```

**Signature parts:** a row of stars for stories read this week; a moon-shaped "Start story" button; soft puffy cards; an optional sleep timer that dims the screen.
**Stays plain:** the story text at a large size, the parent controls (text size, timer), and navigation.
**Avoid:** flashing animation, autoplay, small text, and pure white screens at night.

### Freelancer invoice tracker

**Idea:** freelancers see which invoices are paid, due, or late. Core action: mark an invoice as paid.
**Feeling:** orderly, trustworthy, quiet.
**Metaphor:** the ledger page: columns, ruled lines, and a red margin line for anything overdue.
**Style:** corporate-trust, on ledger-paper tones with an ink-blue primary.

```css
:root {
  --bg: #F4F1EA; --surface: #FFFFFF; --text: #1D2433; --muted: #4B5565;
  --primary: #1F4E79; --on-primary: #FFFFFF; --accent: #B0413E; --focus: #1F4E79;
  --radius: 6px;
  --font-display: "Manrope", "Segoe UI", sans-serif; --font-body: "Manrope", "Segoe UI", sans-serif;
}
```

**Signature parts:** ruled rows like a ledger; a red margin mark plus the word "Overdue" on late invoices (never color alone); amounts in a right-aligned tabular-number column; a "PAID" stamp on settled invoices.
**Stays plain:** the table, filters, forms, and date and money formats.
**Avoid:** playful illustrations, leather textures, status shown by red and green alone.
