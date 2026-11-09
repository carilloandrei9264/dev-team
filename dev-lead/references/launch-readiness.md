# Launch readiness check

Score each applicable item **pass / partial / fail / not checked**, with the evidence (command output, screenshot, file path). Leave out items that do not apply (a portfolio has no checkout). Report coverage: items checked ÷ items applicable.

| Category (weight)        | Items                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------|
| Works as intended (25)   | Main user flow completes; forms validate; no console errors; no broken links; custom 404        |
| Works for everyone (20)  | Text contrast measured; keyboard focus visible; alt text; layouts at phone, tablet, desktop     |
| Trust and safety (25)    | No secrets in client code or git history; HTTPS; input validated server-side; auth and permissions tested; privacy policy matches what the site collects; dependencies audited |
| Speed (15)               | Images sized and compressed; no blocking scripts; page usable on a slow connection              |
| Found and shared (10)    | Titles and meta descriptions; share image and favicon; sitemap and robots.txt                   |
| Operability (5)          | Deployed from CI; rollback path known; errors and uptime monitored; backups if there is a database |

## Report format

```
Launch readiness: NN/100 (Needs work | Ready with caveats | Ready)   Coverage: X/Y
Blockers: ...
Top fixes: 1. ... 2. ... 3. ...
Not checked: item (why, and how to check it)
```

A blocker is anything that leaks data, breaks the main flow, or makes the site unusable on a phone. Any blocker means "Needs work" regardless of score.

## Non-web software

For command-line tools, libraries, scripts, and services without a user interface, replace the table above with these categories. Skip anything that does not apply.

| Category (weight)       | Items                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Works as intended (30)  | Main use case runs end to end; documented examples actually work; sensible errors and exit codes; tests pass on a clean checkout |
| Trust and safety (30)   | No secrets in code or history; inputs validated; dependencies audited; least privilege; license file present |
| Usability (15)          | `--help` or API docs are accurate; clear error messages; install steps verified on a clean machine      |
| Documentation (15)      | README with quick start; changelog; configuration documented; known limits stated                       |
| Release (10)            | Version tagged; built and published by CI; rollback or yank path known                                  |
