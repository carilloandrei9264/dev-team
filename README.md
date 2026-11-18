# devteam: an SDLC skill pack

One router skill (`dev-lead`) plus eight stage skills that mirror the software life cycle. Works for websites, web apps, APIs, command-line tools, libraries, and apps. The router adapts which skills apply to the kind of project.

| Stage            | Skill                 |
|------------------|-----------------------|
| Planning         | plan-project          |
| Design (system)  | design-architecture   |
| Design (UI/UX)   | design-ui             |
| Development      | build-feature         |
| Testing          | test-feature          |
| Review           | review-code           |
| Documentation    | write-docs            |
| CI/CD            | setup-cicd            |
| DevOps / release | deploy-devops         |

For a single request, `dev-lead` loads only the one to three skills needed and applies shared rules (existing project first, small steps, evidence before "done", no risky actions without asking). A larger project can use more skills across its lifecycle; the router selects the relevant stage as the work progresses rather than loading the whole pack at once.

## How the skills connect

Each skill ends with a **Connections** block listing what it **Needs** (and which skill makes it), what it **Produces**, and what usually comes **Next**, each with a condition. That is how an AI picks the right skill for what is needed: if `build-feature` needs a `PLAN.md` that does not exist, it knows `plan-project` makes it.

`dev-lead/references/skill-map.md` collects every block into one overview and a "who makes which file" index. It is generated, so change a skill's Connections and refresh it:

```
python tools/skill_map.py --write
```

The tests fail if a block is missing, names a skill that does not exist, promises a file nobody produces, leaves a skill unreachable, or if the map is stale.

## Visual styles

`design-ui` carries a catalog of 15 visual styles in `design-ui/references/styles/`: minimal-swiss, corporate-trust, flat-material, glassmorphism, neumorphism, claymorphism, neo-brutalism, bento-grid, editorial, organic-natural, playful-memphis, retro-pixel, neon-cyber, aurora-gradient, and terminal-mono. `index.md` has a picker by situation and the token contract shared by every style. Each style file holds its signature traits, when to use and avoid it, CSS tokens, starter CSS, accessibility traps with fixes, and what it pairs with. The AI reads the index and only the one style it picks, not all 15.

To look at every style side by side in a browser:

```
python tools/style_catalog.py --gallery
```

That writes a throwaway `style-gallery.html` in the current folder (web fonts are not loaded, so fallback fonts show). The tests check that every style keeps the full shape, that its palette passes contrast (4.5:1 for text, 3:1 for the focus ring), and that its starter CSS uses tokens instead of raw colors. To add a style, copy an existing file, keep the same sections and tokens, and add a row to the index.

## From idea to design

Given only an idea ("a simple website for tracking plant growth"), `dev-lead` takes the small-idea path: one line of assumptions, a compact plan, a design concept, then a working build checked in the browser. The concept step lives in `design-ui/references/concept.md`. It collects the subject's vocabulary, picks one central metaphor that carries information (for plants: growth is a stem that gets taller), and translates it into palette, type, shape, imagery, components, and copy. It then picks and retunes a catalog style and records everything in `DESIGN.md`, so `build-feature` builds from tokens and the next session does not guess. The guardrails keep usability first: the theme goes on decoration and states, while navigation, forms, and labels stay plain. Four worked examples (plant tracker, coffee roaster, bedtime reading app, invoice tracker) show the output, and the tests check their palettes for contrast.

## Project memory

Work survives across conversations and across AI tools (Claude, Codex, Cursor, others) through small files in the project itself, not in this pack:

| File                        | Purpose                                                                  |
|-----------------------------|--------------------------------------------------------------------------|
| `PROJECT_MEMORY.md`         | where the work stands, the next step, verified status, your standing instructions, key files, gotchas |
| `PLAN.md`                   | goal, features, acceptance criteria, decisions                           |
| `AGENTS.md` and `CLAUDE.md` | a short pointer so each tool reads the memory first                      |

`dev-lead` creates them after you approve the plan and keeps them current. A new session reads the memory, checks it against the repo, and reads only what the next step needs instead of the whole project. The templates, the start and end routines, and the safety limits (no secrets, remembered instructions never replace asking before risky actions) are in `dev-lead/references/project-memory.md`.

## Install

Each skill folder is standalone. Copy the complete folder, including its `SKILL.md` and any `references/` files, so its guidance remains available.

- **Claude Code:** copy the folders into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project). Restart or refresh.
- **Claude.ai:** zip each skill folder separately. Keep the folder at the archive root (for example, `dev-lead/SKILL.md`) and include its `references/` folder if present. Upload under Settings > Capabilities > Skills. Upload `dev-lead` first, then the stage skills.
- Read each `SKILL.md` before installing anything. Skills are instructions your AI will follow, including ones you download from others.

## Check the pack

Run the local integrity checks with Python 3:

```sh
python -m unittest discover -s tests
```

These checks verify skill metadata, router and README coverage, referenced local Markdown files, the Connections blocks and the generated skill map, the visual style catalog, the idea-to-design concept guide, and that the project-memory templates keep their required sections. They check pack structure, not whether an AI selects the right skill.

For small-site feature work, the pack starts with a short set of observable acceptance checks and the project's existing lightweight test tools. Browser testing is an additional step when browser tools are available, not a prerequisite. Reports keep code completion, browser verification, CI verification, and deployment as separate milestones.

For a manual routing smoke test, install the skills and try these requests in Claude Code or Claude.ai. Confirm the indicated skill or skills are selected:

1. "I want to build a booking site for a small dental clinic. Help me plan it." (`plan-project`)
2. "What stack should I use for this? I'm a beginner." (`design-architecture`)
3. "Build step 1 of the plan." (`build-feature`, `test-feature`)
4. "Review this code for security problems." (`review-code`)
5. "Set up GitHub Actions to run my tests." (`setup-cicd`)
6. "How do I put this online?" (`deploy-devops`)
7. "Is it ready to launch?" (`dev-lead` launch-readiness flow)
8. "Design the landing page for this clinic." (`design-ui`)
9. "Write a README and API docs for this project." (`write-docs`)
10. In a project that has `PROJECT_MEMORY.md`: "Continue where we left off." (`dev-lead` reads the memory first, then the stage skill its next step names)
11. "Make me a simple website for tracking my plant growth." (`dev-lead` small-idea path: assumptions, compact plan, `design-ui` concept with a plant-themed `DESIGN.md`, build, browser check)

## Improve it

The value is in the loop: use a skill on a real project, note where the AI got it wrong or skipped something, then edit that skill's `SKILL.md` to prevent it. Add your own preferences (favorite stack, naming, test tools, hosting) to the relevant skill.

## Ideas for later

- `design-ui/references/android.md` already holds Android guidance (spacing, touch targets, Material 3, adaptive layouts). Add `ios.md` the same way if you need it.
- A `references/` folder per skill for your own templates (Dockerfiles, workflow files, README).
- Hosting-specific files under `deploy-devops/references/` (one per provider) so only the relevant one loads.
