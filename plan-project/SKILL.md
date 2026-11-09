---
name: plan-project
description: Turn a rough idea into clear requirements, user stories, a feature list, and a small-step build plan. Use at the start of any new website, app, or software project, when the user says "I want to build...", "help me plan", "what features does it need", or when scope is unclear or a project feels too big to start. Covers the planning and requirements stage of the SDLC and produces PLAN.md.
---

# plan-project

Goal: replace a vague idea with a plan small enough to start today and clear enough to know when it is finished.

## Process

1. **Understand the idea.** Ask one question at a time, and only about things that change the plan: who uses it, what the one most important thing they do is, and what "done" looks like. If the user already answered something, do not ask it again. If they say "pick sensible defaults", record your assumptions and continue.
2. **Find the core flow.** Write the single path that must work for the project to be worth anything (for a clinic site: visitor finds a service, books a slot, gets a confirmation). Everything else is secondary.
3. **List features and cut ruthlessly.** Split into *must have for v1*, *later*, and *not doing*. A first version that ships beats a complete one that doesn't.
4. **Write user stories for must-haves.** Format: "As a [who], I can [do what], so that [why]", each with acceptance criteria that can be checked (see test-feature).
5. **Slice into small steps.** Each step is one working, testable piece a user could see ("visitors can view the room list"), not a technical layer ("set up the database"). Order them so every step builds on a working base.
6. **Note risks and unknowns.** Accounts, costs, third-party services (email, payments, maps), data privacy, anything that needs credentials the user may not have. State it in plain words early so it is not a surprise later.
7. **Write PLAN.md** and show it to the user for approval before any code.

## PLAN.md template

```markdown
# [Project name]
**Goal:** one sentence.
**Users:** who, and what they need.
**Core flow:** step → step → step.

## Features
| # | Feature | Priority | Status | Acceptance (how we know it works) |
|---|---------|----------|--------|-----------------------------------|
| 1 | ...     | must     | todo   | ...                               |

## Not doing (yet)
- ...

## Decisions
- [date] Chose X because Y.

## Risks and open questions
- ...
```

## Sizing

A small site gets one compact PLAN.md. Do not generate folders of sprint paperwork for a project that fits on a page. For larger systems, add a short `docs/` note per step only when the step is complex enough to need it.

## Hand-off

Finish with the first step to build and the suggested next skill (design-architecture if the stack or data model is undecided, otherwise build-feature).
