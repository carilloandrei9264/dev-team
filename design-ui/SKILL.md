---
name: design-ui
description: UI and UX design for websites, web apps, and app screens, covering visual direction, layout, typography, color, spacing, user flows, accessibility, responsive behavior, and interaction states. Use whenever the user asks for a design, layout, look and feel, landing page, dashboard, mockup, wireframe, "make it look better", "it looks generic", usability, or accessibility, and before building any new page or screen. Use even if they only say "build a page" with no mention of design.
---

# design-ui

Goal: interfaces that are easy to use first, and that look like they were made for this product and audience rather than from a template.

Respect what exists. If the project already has a brand, design system, or approved pages, extend them. Never restyle approved work unasked.

## 1. UX before pixels

1. **Who and what.** Name the user and the one task they most need to complete. The design serves that task.
2. **Map the flow.** List the screens or steps from entry to goal. Remove steps that do not earn their place. Every extra click costs users.
3. **Information hierarchy.** On each screen decide the one primary action, the secondary actions, and what can be hidden or moved. One primary button per view.
4. **Content first.** Use real or realistic copy, not lorem ipsum, since layouts break on real text.
5. **Sketch before styling.** For a new screen, give a quick text wireframe (boxes and labels) and confirm it with the user when the layout is unclear.

## 2. Visual direction (new projects)

Choose a direction deliberately and write it in a short `DESIGN.md`: mood in three words, palette, type, spacing scale, corner radius, and what to avoid.

- **Type:** at most two typefaces. A readable body size (16px minimum), clear scale for headings, line length around 45 to 75 characters, comfortable line height.
- **Color:** one primary, one accent, neutrals, plus semantic colors for success, warning, error. Store them as tokens (CSS variables), not scattered hex values. Check contrast with a measurement: 4.5:1 for body text, 3:1 for large text and UI controls.
- **Spacing:** pick a scale (for example 4, 8, 12, 16, 24, 32, 48) and use only those. Consistent spacing does more for polish than decoration.
- **Layout:** align to a grid, group related things, and use whitespace to separate groups rather than borders everywhere.
- **Avoid the generic AI look:** the centered headline over three icon cards and a soft purple gradient. Ask what is distinctive about this client and let it shape layout, imagery, and tone.
- **Match the context:** dashboards and admin screens favor clarity, density, and consistency. Marketing pages and portfolios can take more personality.

## 3. Build the details people feel

- **Every state:** default, hover, focus, active, disabled, loading, empty, error, success. A screen with only a default state is unfinished.
- **Forms:** visible labels (not placeholder-only), clear inline errors that say how to fix the problem, correct input types, sensible autofocus, a disabled-while-submitting button.
- **Feedback:** every action gets an acknowledgment (toast, inline message, state change). Never leave users wondering whether a click worked.
- **Motion:** short and purposeful (roughly 150 to 300ms), used to show cause and effect. Respect `prefers-reduced-motion`.
- **Touch:** tap targets at least 44px, inputs at 16px font size to prevent mobile zoom, content clear of notches and bottom bars.

## 4. Accessibility (not optional)

Semantic HTML (real buttons, links, headings in order), keyboard operation for everything, visible focus ring, alt text for meaningful images, labels linked to inputs, never color alone to convey meaning, sufficient contrast, and a layout that works zoomed to 200%. Test with the keyboard only, and with a screen-reader pass where possible.

## 5. Responsive

Design mobile-first, then widen. Check at roughly 360px, 768px, and 1280px. Wide content (tables, code) scrolls inside its own container instead of the page. Stress the layout with worst-case content: very long names, empty lists, large numbers, other languages.

## 6. Mobile apps (Android focus)

For Android apps, or any mobile UI, read `references/android.md` before designing. It covers dp/sp units, the 4/8dp grid, spacing and padding defaults (16dp side margins on phones), 48dp touch targets, the Material 3 type scale and color roles, dynamic color and dark theme, navigation patterns and back behavior, adaptive layouts for tablets and foldables, edge-to-edge and window insets, permissions, and TalkBack accessibility, ending in a review checklist.

For iOS or cross-platform apps, apply the same UX principles (hierarchy, states, accessibility, touch targets) but follow that platform's own guidelines for navigation, spacing, and components, and say which guidelines you used. For responsive websites viewed on phones, use sections 3 to 5 above.

## 7. Review before handing off

Look at the rendered result, not just the code. Check hierarchy (is the primary action obvious?), consistency (spacing, type, color), all states, contrast, keyboard path, and phone layout. List anything you could not check (no browser, no real device) and how to check it.

For Android, also run the checklist at the end of `references/android.md`. Hand finished design decisions to build-feature, and record them in DESIGN.md or PLAN.md.
