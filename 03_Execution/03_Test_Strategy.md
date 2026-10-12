# Test Strategy

## Test levels
- Unit: validation, permission checks, KPI calculations, workflow transitions.
- Integration: API/database interactions, notification adapter, audit events.
- System: end-to-end request submission and approval.
- Security: authentication, authorization, input validation, secrets scanning.
- UAT: business scenarios signed off by Product Owner.
- Release: smoke tests, backup/restore evidence, rollback rehearsal.

## Release exit criteria
- 100% of Critical and High-priority test cases executed.
- Zero open Critical defects.
- No unresolved security finding without formal risk acceptance.
- Business owner signs off mandatory workflows.
- Rollback procedure tested and Operations accepts handover.
