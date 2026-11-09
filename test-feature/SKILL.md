---
name: test-feature
description: Write, run, and interpret tests for a web or software project, and verify that a feature really works before calling it done. Use whenever the user asks for tests, "does this work", "check it", "why is the test failing", "add coverage", or when a feature or bug fix has just been built. Covers the testing/QA stage of the SDLC (unit, integration, end-to-end, manual checks, bug reports).
---

# test-feature

Goal: turn "I think it works" into evidence. Tests are the proof, and the safety net for later changes.

## Pick the right level

| Level        | Checks                                  | Use for                                   |
|--------------|-----------------------------------------|-------------------------------------------|
| Unit         | One function or component in isolation  | Logic, calculations, validation           |
| Integration  | Several pieces together (API + database)| Routes, queries, auth, permissions        |
| End-to-end   | A real browser clicking the real flow   | The core user flow, checkout, login       |
| Manual       | You look at it                          | Layout, feel, anything hard to automate   |

Most projects want many unit tests, a moderate number of integration tests, and a few end-to-end tests covering the core flow. Use the project's existing test tools; if none exist, suggest a mainstream one (for example Vitest or Jest for JavaScript, pytest for Python, Playwright for browser flows) and say why.

## Process

1. **Start from acceptance criteria** in PLAN.md. Each criterion becomes at least one test, so the tests prove the feature rather than the implementation.
2. **Write the test, watch it fail, then make it pass.** A test that never failed has not proven anything. If you are adding tests after the fact, temporarily break the code once to confirm the test catches it.
3. **Cover more than the happy path:** empty input, very long input, wrong types, missing permissions, duplicate submissions, network failure, and boundary values.
4. **Keep tests independent and deterministic.** No reliance on test order, real clocks, or live third-party services (use fakes or mocks at those edges only).
5. **Run the whole suite**, not just the new test. Read the output. Report counts: passed, failed, skipped.
6. **Walk the real flow** once, in a browser or with real API calls, for anything user-facing. If a browser tool is unavailable, say the browser check did not run and give the exact steps the user can follow.

## When a test fails

Treat it as information. Read the full error, decide whether the code or the test is wrong, and fix the cause. Never delete, skip, or loosen a test just to turn it green, unless it was wrong and you explain why.

## Bug reports

When you find a bug and are not fixing it immediately, write it up so anyone can reproduce it:

```
Title: short, specific
Steps: 1. ... 2. ... 3. ...
Expected: ...
Actual: ...
Evidence: error text, screenshot, failing test name
Severity: blocker | major | minor
```

## Reporting

State what was tested and how, the result counts, and what was not tested. Never claim "all tests pass" or "fixed" without having run them in this session. Coverage numbers are a hint, not a goal: a high percentage with weak assertions proves little.
