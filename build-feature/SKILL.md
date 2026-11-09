---
name: build-feature
description: Implement a feature or fix a bug in a web or software project, in small verified steps, for both frontend and backend. Use whenever the user asks to build, add, change, or fix something in code, says "continue with the next feature", "the button doesn't work", or "implement step 2". Covers the development stage of the SDLC. Pair with test-feature for verification.
---

# build-feature

Goal: make the smallest correct change that delivers the feature, prove it works, and leave the codebase tidier than you found it.

## Before writing code

1. Read PLAN.md for the feature's acceptance criteria. If there are none, write them first (one line each, checkable).
2. Read the surrounding code: naming, structure, existing helpers, how similar things are done. Match them.
3. If this is a bug, **find the cause before changing anything**: reproduce it, read the error, trace where the bad value comes from, test one hypothesis at a time. A fix without a known cause usually moves the bug.

## While building

- **Smallest change that fully solves it.** No extra files, libraries, settings, or features that were not asked for. If a dependency is tempting, say why and let the user decide.
- **Test first when behavior changes.** Write a failing test from the acceptance criteria, then the code to pass it (details in test-feature).
- **Frontend:** for any new page or screen, use design-ui first for hierarchy, states, and accessibility. Then: semantic HTML, responsive from phone up, visible keyboard focus, alt text, sufficient contrast, loading and error and empty states for anything that fetches data. Keep the existing design direction; do not restyle pages the user already approved.
- **Backend:** validate and sanitize all input on the server, return correct status codes and a consistent error shape, use parameterized queries only (never string-built SQL), check permissions on every route, and keep secrets in environment variables.
- **Database changes** go through migrations, not manual edits, and must be reversible where practical.
- **Comments explain why**, not what. Name things clearly instead.
- Do not leave debug logging, dead code, or commented-out blocks behind.

## Finishing a feature

1. Run the project's tests, linter, and build. Read the output. Fix what fails.
2. Walk the real user flow once (browser or API call), not just the unit tests.
3. Update PLAN.md: mark the feature status and note any decisions. If the change affects setup, configuration, or an API, use write-docs to update the README or API docs in the same change.
4. Report: what changed, how it was checked, what was not checked.
5. Offer a commit message in the conventional style, for example `feat(booking): let visitors reserve a room`. Commit or push only if the user asks.

## When to stop and ask

The plan does not match reality, the change needs credentials or a paid service, the fix would touch unrelated areas, or two reasonable designs have a real tradeoff. Present the options with a recommendation, then wait.
