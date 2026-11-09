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

These checks verify skill metadata, router and README coverage, and referenced local Markdown files. They check pack structure, not whether an AI selects the right skill.

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

## Improve it

The value is in the loop: use a skill on a real project, note where the AI got it wrong or skipped something, then edit that skill's `SKILL.md` to prevent it. Add your own preferences (favorite stack, naming, test tools, hosting) to the relevant skill.

## Ideas for later

- `design-ui/references/android.md` already holds Android guidance (spacing, touch targets, Material 3, adaptive layouts). Add `ios.md` the same way if you need it.
- A `references/` folder per skill for your own templates (Dockerfiles, workflow files, README).
- Hosting-specific files under `deploy-devops/references/` (one per provider) so only the relevant one loads.
