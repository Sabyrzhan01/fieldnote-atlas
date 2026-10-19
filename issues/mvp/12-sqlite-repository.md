## Goal
Observations persist in a relational database after process restart.

## Acceptance criteria
- [ ] SQLite tables store collections and observations.
- [ ] Seed runs once and does not duplicate rows.
- [ ] Create/star/delete operations persist after a new connection.
- [ ] Repository boundary is independent of backend DBMS.
- [x] Use SQLAlchemy as the DBMS-agnostic ORM for the default SQLite repository.

## Out of scope
- Cloud database and migrations service.

## Constraints
- Document SQLAlchemy/SQLite as the default tested path; keep the in-memory repository for the staged workflow.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
