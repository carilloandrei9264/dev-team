---
name: write-docs
description: Write and maintain project documentation, including README files, setup and install guides, API documentation, architecture notes, decision records, user guides, code comments and docstrings, changelogs, and handoff reports for clients or teammates. Use whenever the user says "document this", "write a README", "explain how this works", "add comments", "write API docs", "changelog", "handoff", or when a feature, API, or setup process has just been completed and has no docs yet.
---

# write-docs

Goal: someone who has never seen this project can understand it, run it, and change it safely. Good docs are accurate, findable, and short enough to be read.

## Rules

- **Accuracy over volume.** Docs that are wrong are worse than none. Read the actual code, config, and scripts, and run the setup commands you document when you can. Say when something was not verified.
- **Write for a named reader**: a new teammate, an end user, a client, or a future you. Decide who before writing, and match the vocabulary.
- **Lead with what the reader needs first**: what it is, how to run it, how to use it. Details go later.
- **Show, don't just tell.** Include copy-pasteable commands and a realistic example for every key step.
- **One source of truth.** Link to other docs instead of copying them, so they cannot drift apart.
- **Never put secrets in docs.** Use placeholders like `YOUR_API_KEY` and point to `.env.example`.

## Pick the document

| Need                          | Document                         | Where                    |
|-------------------------------|----------------------------------|--------------------------|
| What is this, how do I run it | README                           | repo root                |
| Project goals and status      | PLAN.md (from plan-project)      | repo root                |
| How it is built and why       | Architecture note, decision log  | `docs/architecture.md`   |
| How to call the API           | API reference                    | `docs/api.md` or OpenAPI |
| How to use the product        | User guide                       | `docs/guide.md`          |
| What changed between versions | Changelog                        | `CHANGELOG.md`           |
| Why the code does something   | Comments and docstrings          | in the code              |
| Results for a client          | Handoff report                   | `docs/handoff.md`        |

## README template

```markdown
# Project name
One or two sentences: what it does and who it is for.

## Features
- ...

## Quick start
Prerequisites (with versions), then exact commands:
    git clone ...
    cd ...
    cp .env.example .env
    npm install
    npm run dev
Open http://localhost:3000.

## Configuration
| Variable | Purpose | Example |

## Scripts
| Command | What it does |

## Project structure
Short tree with one-line notes.

## Testing
How to run tests.

## Deployment
Where it runs and how releases happen (link to deploy docs). Rollback steps.

## Contributing
Branching, commit style, how to open a pull request.

## License
```

## API docs

For each endpoint: method and path, purpose, auth required, parameters and body (with types), an example request, an example success response, and the error responses it can return. Prefer generating from an OpenAPI spec if the project has one.

## Decision records

When a significant choice is made, add a short entry to `docs/decisions.md`: date, decision, options considered, reason, consequences. Future readers will ask why.

## Code comments

Comment the **why** (a non-obvious reason, a workaround, a constraint), not the what. Add docstrings to public functions and modules: purpose, parameters, return value, errors raised. Delete comments that restate the code.

## Changelog

Follow the "Keep a Changelog" style: Added, Changed, Fixed, Removed, Security, grouped by version and date, written for users, not as a git log dump.

## Handoff report (client or teammate)

Plain words: what was built, how to run and update it, where it is hosted, accounts and who owns them, what was tested and what was not, open items with owners, and the next recommended steps. Pull the facts from PLAN.md and the launch readiness result in dev-lead.

## Keep it alive

After finishing a feature or change, check whether the README, API docs, or env variable list is now out of date and update it in the same change. Offer to do this at the end of build-feature work.
