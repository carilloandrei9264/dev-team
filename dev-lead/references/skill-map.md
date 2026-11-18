# Skill map

Generated from the Connections block at the end of every SKILL.md by `tools/skill_map.py`. Do not edit by hand: change a skill's Connections and run `python tools/skill_map.py --write`.

How to use it: before a stage, check its **Needs** exist in the repo. If one is missing, run the skill that produces it (see the file index) or, for a small clear task, write the minimum yourself and say so. After a stage, offer the **Next** options whose condition is true now.

## Stages

| Skill | Needs | Produces | Next |
|-------|-------|----------|------|
| `dev-lead` | the user's request, `PROJECT_MEMORY.md` (from `dev-lead`; skip on a brand-new project) | `PROJECT_MEMORY.md`, `AGENTS.md`, `CLAUDE.md`, the launch readiness report | the stage skill the routing table picks; after a stage finishes, offer that skill's Next options |
| `build-feature` | `PLAN.md` (from `plan-project`; if acceptance criteria are missing, write checkable ones first), `PROJECT_MEMORY.md` (from `dev-lead`; skip if the project has none), `DESIGN.md` (from `design-ui`; needed for new pages or screens, otherwise run `design-ui` first) | the code change, updated `PLAN.md` (status and decisions), updated `PROJECT_MEMORY.md`, a suggested commit message | `test-feature` (always, before calling anything done), `write-docs` (setup, configuration, or an API changed), `review-code` (a substantial change, before merge), `plan-project` (the plan no longer matches reality) |
| `deploy-devops` | passing CI (from `setup-cicd`; if there is no pipeline, run `setup-cicd` first), `README.md` (from `write-docs`; the run and rollback steps are written into it) | hosting and environment config, `.env.example`, a Dockerfile when useful, rollback steps, the pre-deploy checklist result | `write-docs` (record hosting, accounts, and rollback), `dev-lead` (the user asks for a full launch readiness score) |
| `design-architecture` | `PLAN.md` (from `plan-project`; if it is absent, write one-line goals and constraints first, or run `plan-project` when the scope is unclear) | stack, folder layout, data model, API and auth decisions, recorded in `PLAN.md` under Decisions | `design-ui` (the project has screens), `build-feature` (the user confirmed the design note and nothing needs designing visually) |
| `design-ui` | `PLAN.md` (from `plan-project`; the users and the core flow shape the screens) | `DESIGN.md` (concept, style, direction, palette, type, spacing), a text wireframe, the list of screen states | `build-feature` (the design is approved; hand over the design decisions) |
| `plan-project` | the user's idea; nothing else | `PLAN.md` (goal, core flow, features with acceptance criteria, decisions, risks) | `design-architecture` (stack, data model, or API still undecided), `design-ui` (the project has screens and no design direction yet), `build-feature` (stack and design are settled or not needed) |
| `review-code` | the code, diff, or pull request to review, `PLAN.md` (from `plan-project`; optional, to judge correctness against the plan) | a review with a verdict and findings grouped by severity | `build-feature` (blockers or should-fix items to act on), `test-feature` (test gaps found), `deploy-devops` (the verdict is approve and the user wants to ship) |
| `setup-cicd` | test and build commands that pass locally (from `test-feature`) | `.github/workflows/ci.yml` (or the equivalent for the project's CI), a short note on what is and is not automated | `deploy-devops` (CI is green and the user wants to ship), `build-feature` (a failure turns out to be a code bug, not a pipeline problem) |
| `test-feature` | `PLAN.md` (from `plan-project`; the acceptance criteria become the tests), the built feature or fix (from `build-feature`) | tests, a result report (counts and what was not tested), bug reports | `build-feature` (a check fails because the code is wrong), `review-code` (checks pass and the change is substantial), `setup-cicd` (the checks should run automatically and no pipeline exists yet) |
| `write-docs` | the working code, config, and scripts to document (from `build-feature`), `PLAN.md` (from `plan-project`; for goals and status) | `README.md`, `CHANGELOG.md`, files under `docs/`, code comments, the handoff report | `build-feature` (the next feature in the plan), `setup-cicd` (shipping and no pipeline exists yet), `deploy-devops` (shipping) |

## Who makes which file

| File | Produced or updated by | Needed by |
|------|------------------------|-----------|
| `AGENTS.md` | `dev-lead` | - |
| `CHANGELOG.md` | `write-docs` | - |
| `CLAUDE.md` | `dev-lead` | - |
| `DESIGN.md` | `design-ui` | `build-feature` |
| `PLAN.md` | `build-feature`, `design-architecture`, `plan-project` | `build-feature`, `design-architecture`, `design-ui`, `review-code`, `test-feature`, `write-docs` |
| `PROJECT_MEMORY.md` | `dev-lead`, `build-feature` | `dev-lead`, `build-feature` |
| `README.md` | `write-docs` | `deploy-devops` |
