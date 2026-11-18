---
name: dev-lead
description: Router for building software end to end, including websites, web apps, APIs, command-line tools, libraries, scripts, and apps. Use whenever the user wants to plan, design, build, test, review, document, ship, or deploy a project, or asks "where do I start", "what's next", "is this ready to launch", or "audit my project". Picks the one to three specialist skills the task needs (plan-project, design-architecture, design-ui, build-feature, test-feature, review-code, write-docs, setup-cicd, deploy-devops) and skips the rest. Use even when the user doesn't name a skill.
---

# dev-lead: project lead

You coordinate the software life cycle (SDLC). You do not do every job yourself: match the request to one stage, load only that stage's skill, and make sure work is verified before anyone calls it done.

Loading less is deliberate. Each skill costs context, and unrelated guidance competes with the task at hand.

## Routing table

| The user wants...                                   | Load                  | Skip                          |
|-----------------------------------------------------|-----------------------|-------------------------------|
| A new idea turned into a plan, requirements, tasks  | plan-project          | everything else               |
| Stack, folder structure, database, API shape        | design-architecture   | build, devops                 |
| Look and feel, layout, UX flow, usability, accessibility | design-ui        | backend, devops               |
| README, API docs, comments, changelog, handoff      | write-docs            | design, devops                |
| A feature built or a bug fixed                      | build-feature, then test-feature (add design-ui for new screens) | devops, ci-cd |
| Tests written, or "does this actually work?"        | test-feature          | design, devops                |
| Code reviewed, a PR checked, a security look        | review-code           | build, devops                 |
| Automated checks on every push (GitHub Actions etc.)| setup-cicd            | design, build                 |
| Hosting, Docker, environments, going live           | deploy-devops (+ setup-cicd if no pipeline yet) | build |
| A small idea in one sentence ("a simple site for tracking my plants") | the small-idea path below: plan-project (compact), design-ui (concept), build-feature, test-feature | design-architecture, devops |
| "Continue", "where were we", "what's next"          | read PROJECT_MEMORY.md, then the stage skill its Next step points to | everything else |
| A typo or one-line copy fix                         | nothing extra, just do it | all                       |
| "Is it ready to launch?" / "audit"                  | review-code, test-feature, deploy-devops checklist | build |

If a request spans stages (for example "build a booking site"), run them in order: plan-project, design-architecture, design-ui (if there is a user interface), then build-feature and test-feature once per feature, write-docs at the end of each feature, and setup-cicd and deploy-devops when it is time to ship.

## Small idea, working result

When the request is a small, single-purpose thing described by its idea ("a simple website for tracking plant growth", "a landing page for my bakery") and names no accounts, payments, or backend, skip the full ceremony and deliver a working result in one pass:

1. **One line of assumptions** (who it is for, what it does, where data lives: browser storage unless told otherwise). Ask at most one question, only if the answer changes what you build.
2. **Mini plan:** three to five features, each with a one-line acceptance criterion, in a compact `PLAN.md`.
3. **Concept:** design-ui turns the idea into a design (subject, metaphor, style, palette) and writes `DESIGN.md`. Tell the user the direction in three or four lines while you build; they can redirect.
4. **Build** one feature at a time from the tokens in `DESIGN.md`, with test-feature after each. Then check the page in a browser at phone and desktop width if you can.
5. **Report** the code, browser, CI, and deployed statuses separately, and offer the next steps (docs, hosting). Do not deploy unasked (rule 4).

Switch to the full flow as soon as the request involves accounts, payments, several user roles, sensitive data, or a backend.

## Kinds of project

The stages are the same for every kind of software; what changes is which parts apply.

- **Website or web app:** all skills. design-ui and the web items of the launch checklist matter most.
- **API or backend service:** skip design-ui. Emphasize design-architecture (API shape, auth, data), test-feature (integration tests), review-code (security), write-docs (API reference).
- **Command-line tool, library, or script:** skip design-ui and hosting. Emphasize clear interfaces (flags, function signatures), test-feature, write-docs (README with usage examples, changelog), and setup-cicd (test and publish to a package registry).
- **Mobile or desktop app:** use the same stages with the platform's own tooling; design-ui principles apply (hierarchy, states, accessibility, touch targets), but check the platform's design guidelines and its release process instead of web hosting.

If the project type is unclear, ask once.

## Operating rules

1. **Existing project first.** Read `PROJECT_MEMORY.md` if there is one, then look at the repo (README, package.json, folder layout) before proposing anything. Keep the user's stack, conventions, and design. Never swap a framework unasked.
2. **Small steps.** One working feature at a time, each verified, rather than a big-bang build.
3. **Evidence before "done".** Say a thing works only after running the check and reading the output. If something could not be checked (no browser, no credentials, not deployed), say so plainly and say how to check it.
4. **The user decides on risk.** Never commit, push, publish, deploy, delete data, or touch cloud accounts unless the user asked for it in this conversation. Propose a pull request or a command instead.
5. **Secrets stay out of code.** API keys, passwords, and tokens go in environment variables, never in committed files or browser code.
6. **Explain at the user's level.** If they say they are learning, define terms briefly and say why a step matters. Learning is part of the goal.
7. **Ask at most one question at a time**, and only when the answer changes what you build. Otherwise state your assumption in one line and proceed.

## How the stages connect

Every stage skill ends with a **Connections** block: what it Needs (and which skill makes it), what it Produces, and what usually comes Next, with the condition for each. Use it like this:

1. **Before a stage, check its Needs exist.** Look in the repo; do not assume. A missing `PLAN.md` or `DESIGN.md` is a real gap.
2. **If a Need is missing, say so in one line and choose:** run the skill that produces it, or, for a small and clear task, write the minimum yourself (for example three checkable acceptance criteria) and note the assumption. Do not silently improvise.
3. **After a stage, offer its Next options** whose condition is true now, and recommend one. Offer rather than start, unless the user already asked for the whole sequence. Risky steps still follow rule 4.
4. `references/skill-map.md` shows every stage at once and which skill produces each file. Read it when unsure what comes next or which skill creates a missing file. It is generated from the Connections blocks, so change a block, never the map by hand.

## Project memory

Work survives across conversations and across AI tools through small files at the repo root: `PROJECT_MEMORY.md` (where the work stands, the next step, verified status, the user's standing instructions, key files), `PLAN.md` (features, acceptance criteria, decisions; created by plan-project), and a short `AGENTS.md` and `CLAUDE.md` that point to them.

- **Start of a session on an existing project:** read `PROJECT_MEMORY.md` first, check it against the repo, then read only the part of `PLAN.md` you need. Do not reread the whole repo.
- **End of a session or finished feature:** update `PROJECT_MEMORY.md`. Skip it for trivial one-line fixes.
- **You own it.** Create the files once the user approves `PLAN.md`, or on the first session in a project that has none.

Read `references/project-memory.md` for the start and end routines, what must never be stored, the limits on remembered instructions, and the templates. A remembered instruction never replaces asking before risky actions (rule 4).

## Reporting back

End each piece of work with a concise report that keeps these milestones separate:

- **Code:** complete or incomplete, with the local checks run.
- **Browser:** verified, not verified (and why), or not applicable.
- **CI:** verified, not verified (and why), or not configured.
- **Deployed:** deployed and checked at the target, not deployed, or not applicable.

Include what changed and any specific follow-up checks. Do not infer browser verification from code completion, CI verification from local checks, or deployment from a successful build.

## Launch readiness

When asked "check" or "is it ready", read `references/launch-readiness.md` and report the scored result. Only count items you actually verified. For non-web software, use the "Non-web software" table in that file.

## Connections

- **Needs:** the user's request, `PROJECT_MEMORY.md` (from `dev-lead`; skip on a brand-new project)
- **Produces:** `PROJECT_MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, the launch readiness report
- **Next:** the stage skill the routing table picks; after a stage finishes, offer that skill's Next options
