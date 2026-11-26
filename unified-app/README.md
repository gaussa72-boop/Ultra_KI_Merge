# AUREALIS OMNIA — Alliance AI

Responsive German-language cosmic project cockpit.

## Live application
https://aurealis-omnia-alliance-ai.onrender.com

## Current integrations
- 45 repositories catalogued from the two connected GitHub accounts.
- 53 Render services inventoried; 35 of the 45 repositories have at least one matching service.
- Service links are shown only when returned by the connected Render account.
- Ten named agent/persona profiles are available in the UI.
- The chat frontend is wired to the Quantum KI Ultra Pro V2 `POST /api/chat` endpoint at `https://quantum-ki-ultra-pro-v2-renewed.onrender.com`.
- The API allows CORS only from this Alliance AI dashboard origin.

## Current limitations
- The chat code and API deployment are live, but an end-to-end browser chat test and provider readiness check have not yet been completed.
- Agent profiles are role prompts routed through the shared model; they are not ten independent autonomous model instances.
- Per-project website agents are registry entries only. No background maintenance workers are running.
- GitHub repository webhooks, automatic test gates, approvals, persistent orchestration database and automatic future-project discovery are not yet configured.
- Render service records indicate configured services, not guaranteed healthy public websites.

## Deployment
- GitHub repository: gaussa72-boop/Ultra_KI_Merge
- Branch: main
- Render static publish directory: unified-app
- Build command: `echo "Static assets ready"`

## Security
No API keys or shared tokens belong in the frontend. Any write-enabled agent needs scoped server-side credentials, audit logs, backups, tests and explicit approval gates.
