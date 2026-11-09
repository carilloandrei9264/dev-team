---
name: review-code
description: Review code, a diff, a pull request, or a whole project for bugs, security problems, readability, performance, and test gaps, and respond properly to review feedback. Use whenever the user says "review this", "check my code", "is this secure", "look at my PR", "audit the code", or pastes code and asks if it is good, and before merging any substantial change.
---

# review-code

Goal: catch the problems that matter before they ship, and say them clearly enough to act on. A good review is specific, prioritized, and kind.

## Review in this order

1. **Correctness.** Does it do what the plan or issue says? Check edge cases, error handling, off-by-one errors, null or empty values, async and race conditions.
2. **Security.** Check the items below. Anything here is usually a blocker.
   - Secrets, keys, or tokens in code, config, or git history
   - Input not validated or sanitized on the server; SQL built by string concatenation; unescaped output (XSS)
   - Missing or client-only authorization; IDs that let users access each other's data
   - Weak password handling, insecure cookies or tokens, missing CSRF protection where needed
   - Dependencies with known vulnerabilities (run the package manager's audit)
   - Overly broad CORS, verbose error messages that leak internals, unrestricted file uploads
3. **Tests.** Is the new behavior covered, including failure cases? Would the tests fail if the code broke?
4. **Design and readability.** Clear names, small functions, no duplication that will hurt, follows the project's conventions, no unrequested extras.
5. **Performance.** Only flag what is measurable or obviously wasteful: queries in loops, missing indexes on filtered columns, unbounded lists, large unoptimized images or bundles.
6. **Accessibility and UX** for frontend changes: keyboard use, contrast, labels, states for loading/error/empty.

## Output format

Group findings by severity, most important first. Each finding names the file and line, says what is wrong, why it matters, and gives a concrete fix.

```
Verdict: approve | approve with changes | needs work

Blockers
- path/file.js:42 — SQL built from user input. Allows injection. Use a parameterized query: ...

Should fix
- ...

Nits (optional)
- ...

Good
- (name something genuinely well done)
```

Do not pad with style nits when real problems exist. If nothing is wrong, say so briefly. Be clear about what you did not review (files skipped, no runtime check).

## Receiving review feedback

When the user brings you review comments to act on:

1. Understand each comment before changing code. If one is unclear, ask.
2. Verify the claim against the code. Reviewers are sometimes wrong, and blindly applying a bad suggestion adds a bug.
3. Fix valid points one at a time and rerun tests. Push back politely, with evidence, on the ones that are not valid.
4. Summarize what you changed and what you declined, with reasons.
