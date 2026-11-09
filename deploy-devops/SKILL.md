---
name: deploy-devops
description: Deploy and operate a web app or software project, including hosting choices, Docker containers, environment variables and secrets, staging vs production, domains and HTTPS, monitoring, backups, and rollback. Use whenever the user mentions deploying, hosting, going live, Docker, servers, AWS, Azure, GCP, Vercel, Netlify, Terraform, DevOps, environments, logs, monitoring, uptime, or "how do I put this online".
---

# deploy-devops

Goal: get the project running somewhere real, safely, and be able to see when it breaks and undo a bad release. DevOps is the habit of building, shipping, and running software as one loop.

## Safety rules (read first)

- **Never deploy, create cloud resources, change DNS, delete data, or run migrations against production unless the user explicitly asks in this conversation.** Default to preparing: write the config, show the commands, explain what each does and what it could cost.
- Say clearly when a step costs money or needs an account, before doing it.
- Run destructive or irreversible commands only after the user confirms the exact command and target.
- Never put secrets in images, repos, or logs. Use the host's secrets or environment settings.

## Pick the simplest hosting that fits

| Project type                      | Good starting point                                         |
|-----------------------------------|-------------------------------------------------------------|
| Static site (HTML/CSS/JS)         | Static host with a free tier (for example Netlify, Vercel, GitHub Pages, Cloudflare Pages) |
| Frontend framework with light API | Same platforms, using their serverless or edge functions    |
| Backend API + database            | Managed platform (Render, Railway, Fly.io) or a container service |
| Needs custom infrastructure       | A cloud provider (AWS, Azure, GCP), ideally with infrastructure as code |

Recommend one, explain why in two sentences, mention current free-tier and pricing limits only after checking the provider's current pricing page, since these change.

## Deployment workflow

1. **Configuration through environment.** One codebase, with settings (database URL, API keys, feature flags) read from environment variables. Provide a `.env.example` listing the names with no real values, and make sure `.env` is in `.gitignore`.
2. **Environments.** At least local and production; add staging when real users depend on the app, so changes are tried somewhere safe first.
3. **Containerize when useful.** A Dockerfile makes "works on my machine" reproducible. Keep images small (multi-stage builds), run as a non-root user, pin base image versions, and add a `.dockerignore`.
4. **Automate through CI/CD.** Deploy from the pipeline (see setup-cicd), not from a laptop, so each release is traceable.
5. **Database changes** ship as migrations, applied deliberately, with a backup taken first.
6. **Domain and HTTPS.** Use the host's managed certificates. Redirect HTTP to HTTPS. Explain DNS records in plain words if the user is new.
7. **Health check.** After deploy, load the real URL, run through the core flow, and read the logs. A deploy is not done until this is verified.

## Operate it

- **Logs:** know where to read them and make sure errors are logged with enough context, without personal data or secrets.
- **Monitoring:** at minimum an uptime check and error alerts to an address the user actually reads.
- **Backups:** if there is a database, automatic backups plus one tested restore.
- **Rollback:** know before releasing how to return to the previous version (redeploy the last good build, or revert the commit). Write it in the README.
- **Infrastructure as code** (Terraform or similar) once there is more than a couple of resources, so the setup is reviewable and repeatable.

## Pre-deploy checklist

Report each as done, pending, or not applicable:

- [ ] Tests and build pass in CI
- [ ] No secrets in the repo or client code; `.env.example` present
- [ ] Production environment variables set on the host
- [ ] Database migrations ready and a backup taken
- [ ] HTTPS and domain working
- [ ] Error monitoring and uptime check configured
- [ ] Rollback steps written down
- [ ] Core flow verified on the live URL

For a full readiness score, use the launch readiness reference in the dev-lead skill.
