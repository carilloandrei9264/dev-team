---
name: design-architecture
description: Choose the tech stack, folder structure, database schema, API design, and authentication approach for a project. Use after planning and before building, or whenever the user asks "what stack should I use", "how should I structure this", "design the database", "design the API", "monolith or microservices", or needs to decide how the pieces fit together. Covers the design stage of the SDLC.
---

# design-architecture

Goal: make the few decisions that are expensive to change later, keep everything else simple, and write the decisions down.

## Principles

- **The user's existing stack wins.** If the repo already uses something, extend it. Recommend a change only for a real, stated problem.
- **Boring and simple beats clever.** A static site needs no backend. A small app needs one server and one database, not microservices. Add complexity when a specific pain demands it.
- **Match the learner.** If the user is learning, prefer mainstream tools with good docs (for example: HTML/CSS/JS or React for the frontend, Node.js or Python for the backend, PostgreSQL for data) over trendy ones.

## Process

1. Read PLAN.md and the existing repo. List what the product must do that constrains the design (logins, payments, real-time, file uploads, SEO, offline).
2. **Recommend one default stack** and explain the choice in two or three sentences, mentioning one alternative and why you did not pick it. Cover: frontend, backend (if any), database (if any), hosting.
3. **Draw the structure.** Folder layout, and how a request flows (browser → frontend → API → database). A small text diagram is enough.
4. **Design the data.** List the main entities, their fields, and relationships. Add constraints and indexes where the queries will need them. Prefer SQL for data with relationships.
5. **Design the API** if there is one. Use consistent resource-based routes, correct HTTP methods and status codes, a standard error shape, and pagination for lists. Version it only if outside clients will depend on it.
6. **Decide auth and permissions.** Use a proven library or hosted provider rather than writing your own. Hash passwords with a modern algorithm, use secure httpOnly cookies or short-lived tokens, and enforce permissions on the server for every request, never only in the UI.
7. **Name the non-functional needs** that apply: expected load, privacy rules (what personal data is stored and why), backups, accessibility.
8. **Record decisions** in PLAN.md under *Decisions*, each with a one-line reason. Future you will ask why.

## Output

A short design note: stack and why, folder tree, data model, API list (if any), auth approach, and open questions. Keep it to roughly one page. Ask the user to confirm before building.

## Red flags to push back on

- Microservices, Kubernetes, or a message queue for a first version.
- Storing secrets or API keys in frontend code.
- Authorization checked only in the browser.
- A database chosen because it is fashionable rather than because of the data shape.
