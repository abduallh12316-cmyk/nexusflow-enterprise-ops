# Technical Scope (Implementation Brief)

Suggested reference architecture for a later implementation:
- Frontend: React + TypeScript.
- Backend: Python FastAPI or Node.js REST API.
- Database: PostgreSQL.
- Authentication: OIDC-ready interface with local mock mode.
- Audit events: append-only audit table.
- Reporting: JSON/CSV export and dashboard aggregates.
- Email: provider adapter with mock transport as default.
- Delivery: Docker Compose and CI workflow.

This pack supplies simulated management data and governance artifacts; it is not a deployed application. Keep mock mode separate from production integrations if implementing the application.
