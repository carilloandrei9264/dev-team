---
name: setup-cicd
description: Set up or fix CI/CD pipelines that automatically test, build, and deploy code on every push, especially GitHub Actions. Use whenever the user mentions CI, CD, CI/CD, pipelines, GitHub Actions, workflows, automated checks or deploys, "my build failed", or "why is the pipeline red". Covers the integration and delivery automation stage of the SDLC.
---

# setup-cicd

Goal: every change is checked automatically, and shipping becomes a boring, repeatable action.

- **CI (continuous integration):** on every push and pull request, install, lint, test, and build. Catches breakage within minutes.
- **CD (continuous delivery or deployment):** after CI passes on the main branch, package and release. Delivery stops at a ready artifact for a human to approve; deployment pushes it live automatically.

## Process

1. **Read the project first.** Find the language, package manager, test and build commands (package.json scripts, Makefile, pyproject). The pipeline should run exactly the commands a developer runs locally. Confirm they pass locally before automating them.
2. **Start with CI only.** One workflow, triggered on `push` and `pull_request`. Steps: check out, set up the language with dependency caching, install with a lockfile (`npm ci`, `pip install -r`), lint, test, build.
3. **Add CD later and gated.** Deploy only from `main`, only after CI passes, and for anything that matters to real users, behind a manual approval (GitHub environment with required reviewers).
4. **Keep it fast.** Cache dependencies, run independent jobs in parallel, and fail fast. A slow pipeline gets ignored.
5. **Protect the main branch.** Suggest branch protection: require the CI check to pass and a pull request before merge. Say that this is a repo setting the user applies; do not assume access.

## Starter CI workflow (Node example, adapt to the stack)

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run lint --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
```

Pin third-party actions to a version tag or commit, and use the minimal `permissions` block as above.

## Security rules for pipelines

- Secrets live in the repository's encrypted secrets store, never in the workflow file or logs. Do not echo them.
- Give each job the least permission it needs. Avoid running untrusted pull-request code with deploy secrets.
- Prefer short-lived cloud credentials (OIDC) over long-lived keys when the platform supports it.
- Treat third-party actions as code you are running: prefer official or well-known ones and pin versions.

## Debugging a failed build

1. Open the **first** failing step and read its full log. Later errors are often consequences.
2. Reproduce locally with the same command and the same language version.
3. Common causes: version mismatch between local and CI, missing environment variable or secret, lockfile out of sync, test relying on order or timing, a service the test needs that is not running in CI, case-sensitive file paths on Linux.
4. Change one thing at a time and rerun. Do not stack guesses.

## Hand-off

Tell the user which file you created or changed, what triggers it, what it runs, and what is not yet automated. Do not commit or push the workflow unless asked.
