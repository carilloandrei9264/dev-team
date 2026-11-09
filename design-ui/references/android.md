# Android design reference

Use this for Android apps (Kotlin with Jetpack Compose or XML views, or cross-platform apps that ship to Android). Based on Material Design and Android's own guidance. The numbers below are well-established defaults, but Material evolves: when a detail matters (exact component sizes, a new component, a new Android version), check material.io and developer.android.com/design before committing to it, and say so if you could not.

## Contents
1. Units and the grid
2. Spacing and padding
3. Touch targets
4. Typography
5. Color and theming
6. Navigation
7. Common components
8. Adaptive layouts (phones, tablets, foldables)
9. System integration (edge-to-edge, back, insets)
10. Accessibility
11. Performance and feel
12. Android design review checklist

## 1. Units and the grid

- **dp** (density-independent pixels) for sizes, spacing, and layout. **sp** (scale-independent pixels) for text only, so text follows the user's font size setting. Never use raw px.
- Base everything on a **4dp baseline**, with **8dp** as the main step. Common values: 4, 8, 12, 16, 24, 32, 48, 64.
- Store spacing, sizes, and colors as named resources or theme tokens, not literals scattered in screens.

## 2. Spacing and padding

| Where                                          | Default                                            |
|------------------------------------------------|----------------------------------------------------|
| Screen side margins, compact width (phones)    | 16dp                                               |
| Screen side margins, medium/expanded width     | 24dp                                               |
| Between a title and its related content        | 8dp to 16dp                                        |
| Between unrelated sections                     | 24dp to 32dp                                       |
| Inside cards and list-item padding             | 16dp                                               |
| Between cards in a list or grid                | 8dp to 16dp                                        |
| Between icon and its label                     | 8dp                                                |
| Between adjacent tappable elements             | at least 8dp                                       |
| Dialog content padding                         | 24dp                                               |

Group related things closer together than unrelated things. Use the same spacing for the same relationship across every screen. Spacing is applied on top of **system bar insets** (section 9), not instead of them.

## 3. Touch targets

- **Minimum 48dp x 48dp** for anything tappable, even when the visible icon or text is smaller (a 24dp icon sits inside a 48dp target).
- At least **8dp** between neighboring targets to prevent mis-taps.
- Put primary actions in the thumb zone (lower half of the screen) on phones. Avoid placing critical actions only at the top corners.
- Give every tappable element a visible pressed state (ripple) and a focus state for keyboard and switch users.

## 4. Typography

- Use the Material 3 type scale roles (display, headline, title, body, label) rather than ad hoc sizes. Typical anchors: body large 16sp, body medium 14sp, title large 22sp, label large 14sp. Check the current type scale for exact values.
- Body text no smaller than **14sp**, and prefer 16sp for reading content. Avoid text below 12sp.
- Support the user's font scale up to **200%**: no fixed-height containers around text, allow wrapping, let rows grow, and test with the largest system font size.
- Limit to one or two typefaces. Line length for reading around 40 to 60 characters on phones.
- Do not truncate important text (prices, names, warnings). If you must, use ellipsis and keep the full text reachable.

## 5. Color and theming

- Build the theme from **Material 3 color roles** (primary, on-primary, secondary, tertiary, surface, on-surface, error, outline, and the container roles) rather than hard-coded colors, so light, dark, and dynamic themes all work.
- **Dynamic color** (Material You, Android 12+): derive the scheme from the user's wallpaper when the product allows it. Keep a defined brand fallback scheme for older devices. If a brand color must stay fixed, say so.
- **Dark theme is expected.** Support it from the start, follow the system setting, and do not use pure black text on pure white or pure white on pure black for large areas.
- Contrast: **4.5:1** for body text, **3:1** for large text and UI components (icons, input borders). Measure it, in both themes.
- Never use color alone to carry meaning (add an icon or text for errors and status).
- Use elevation and tonal surfaces for hierarchy instead of heavy shadows and borders.

## 6. Navigation

Pick the pattern by number and importance of top-level destinations:

| Pattern                 | Use when                                              |
|-------------------------|-------------------------------------------------------|
| Navigation bar (bottom) | 3 to 5 top-level destinations, phones                 |
| Navigation rail         | 3 to 7 destinations on tablets and foldables, landscape |
| Navigation drawer       | many destinations, or secondary on large screens      |
| Tabs                    | switching between related views within one screen     |

Rules:
- Show labels with bottom navigation icons, and highlight the current destination.
- Keep the top bar to a title, a back or menu icon, and at most a few actions, with the rest in an overflow menu.
- Use a **FAB** for the single most important action on a screen only. One per screen.
- **Back must work predictably.** Support the system back gesture, including predictive back (Android 13+ opt-in, standard on newer versions). Never trap users or require an in-app back button as the only way out.
- Keep navigation state when switching bottom destinations and when rotating the device.

## 7. Common components

- **Buttons:** one filled (primary) button per view; use outlined or text buttons for secondary actions. Label with a verb ("Save", "Book room"). Disabled state must still be readable.
- **Text fields:** visible label (floating or above), helper text, and inline error text that says how to fix the problem. Set the correct keyboard type and IME action (next, done, search), and keep the field visible above the keyboard.
- **Lists:** consistent row height and padding, leading icon or image, primary and secondary text, trailing action. Handle empty, loading, and error states, and use pagination for long lists.
- **Cards:** group one coherent item; avoid cards inside cards.
- **Dialogs:** only for decisions that need attention. A clear title, brief content, and verb-labeled actions, with the confirming action on the right. Do not stack dialogs.
- **Bottom sheets:** for supplementary actions or details without leaving the screen.
- **Snackbars:** for brief, non-critical feedback, with an optional single action such as Undo. Not for errors that need resolution.
- **Progress:** show a progress indicator for waits over about a second; prefer skeleton or placeholder content over blank screens. Use determinate progress when you know the percentage.
- **Empty states:** explain what belongs here and offer the next step.

## 8. Adaptive layouts

Design to **window size classes**, not to specific devices:

| Class    | Width        | Typical device                | Layout guidance                                       |
|----------|--------------|-------------------------------|-------------------------------------------------------|
| Compact  | under 600dp  | most phones, portrait         | single pane, bottom navigation                        |
| Medium   | 600 to 839dp | small tablets, unfolded foldables, phones in landscape | navigation rail, optional two panes |
| Expanded | 840dp+       | tablets, large foldables, desktop mode | persistent navigation, list-detail or multi-pane |

- Do not lock orientation unless the content truly requires it (for example a camera or game).
- Use canonical layouts (list-detail, supporting pane, feed) for larger screens instead of stretching the phone layout.
- Constrain content width on wide screens (readable column around 600 to 840dp) rather than letting text run edge to edge.
- Handle foldable postures and window resizing (multi-window, split screen) without losing state.
- Test at least a small phone, a large phone, and a tablet or resizable emulator.

## 9. System integration

- **Edge-to-edge:** draw behind the status and navigation bars (the default and expected on current Android). Apply **window insets** as padding so content and controls are never hidden under the status bar, navigation bar, display cutout, or on-screen keyboard. Scrolling content may draw behind the bars; fixed controls must sit clear of them.
- **Gesture navigation:** keep tappable elements away from the system gesture edges at the left and right screen sides, and do not place critical controls right at the bottom edge.
- **Keyboard:** adjust layout with the IME inset so the focused field and its primary action stay visible.
- **Permissions:** ask at the moment the feature needs it, with a short explanation of why beforehand, and keep the app useful if the user declines. Do not request permissions at launch for things not yet needed.
- **Notifications:** use channels with sensible importance, only for things the user cares about, with a clear tap destination. Request the notification permission in context on Android 13+.
- **Splash and icons:** use the platform splash screen API, and provide an adaptive (and themed) launcher icon.
- **Share, deep links, and widgets** are optional extras; add them only when they serve a real user need.

## 10. Accessibility

- **TalkBack:** every control has a meaningful `contentDescription` (or semantics label in Compose); decorative images are marked as such. Make focus and reading order follow the visual order. Group related items into one announcement where it helps.
- Provide custom actions where gestures (swipe-to-dismiss) are the only way to do something.
- Support font scaling to 200%, display size changes, and bold text.
- Respect **reduce motion** and animation scale settings; avoid flashing content.
- 48dp touch targets, sufficient contrast, and no information carried by color alone (sections 3 and 5).
- Test with TalkBack on, with Switch Access or keyboard navigation, and run the Accessibility Scanner.

## 11. Performance and feel

- Keep the main thread free: no network or disk work on it. Show content quickly, then fill in.
- Aim for smooth scrolling (no dropped frames) and fast cold start. Use lazy lists (`LazyColumn` or `RecyclerView`) for long lists, and avoid nested scrolling of the same direction.
- Handle slow and offline networks: cache what matters, show cached data with a refresh indicator, and give clear retry actions instead of dead ends.
- Preserve state across configuration changes (rotation, dark mode toggle, font size change) and process death.
- Use motion to explain relationships (shared element, container transform), 150 to 300ms for small changes and up to about 500ms for large transitions, with standard easing.
- Provide haptic feedback sparingly for meaningful moments.

## 12. Android design review checklist

Report each as pass, fail, or not checked:

- [ ] Spacing uses the 4/8dp scale and 16dp side margins on phones
- [ ] All touch targets at least 48dp with 8dp between them
- [ ] Text in sp; no text below 12sp; layout survives 200% font scale
- [ ] Theme built from color roles; light and dark both checked; contrast measured
- [ ] Navigation pattern fits the destination count; back gesture behaves correctly
- [ ] One primary action per screen; FAB only for the key action
- [ ] Insets handled: nothing hidden under system bars, cutout, or keyboard
- [ ] Empty, loading, error, offline states exist for each data screen
- [ ] Works on compact, medium, and expanded widths and after rotation
- [ ] TalkBack labels, reading order, and focus checked
- [ ] Permissions requested in context; app still works if denied
- [ ] Verified on a real device or emulator (state clearly if only reasoned about)
