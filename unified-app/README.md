# AUREALIS OMNIA — Alliance AI

A unified project cockpit prototype added to the existing `Ultra_KI_Merge` repository.

## What is included
- Responsive German-language cosmic/steampunk dashboard.
- Clickable navigation for overview, apps, repositories, 10 agent roles, per-project website-agent registry, personalities, update matrix, deployments, monitoring and chat.
- Static project catalog based on repositories visible in the two connected GitHub accounts at creation time.
- Direct GitHub links for every catalogued repository.
- Explicit UI labels distinguishing catalogued projects from services that are actually integrated or deployed.

## Important implementation boundaries
- The chat is a local UI prototype, not a live LLM connection.
- Per-project agents are a registry/architecture proposal, not active autonomous agents.
- The Update Matrix is a workflow/status view, not yet a running webhook or CI/CD automation.
- No API keys, database credentials, or private tokens are embedded in frontend code.
- No existing projects or repositories are overwritten by this static dashboard.

## Run locally
Open `unified-app/index.html` in a browser.

## Deploy on Render
Create a Static Site from this repository, branch `main`, publish directory `unified-app`, with no build command required.

## Next integration phase
1. Add a backend service with authenticated GitHub and Render integrations.
2. Store credentials only as encrypted server-side environment variables.
3. Import repository/service metadata dynamically rather than relying on the initial static catalog.
4. Implement per-project agents with explicit scopes and human approval for writes/deployments.
5. Implement Update Matrix webhooks, test gates, deployment verification, and an auditable event log.
6. Connect PostgreSQL only after confirming the target service and schema.

