## Goal
Observations persist in a relational database after process restart.

## Acceptance criteria
- [ ] SQLite tables store collections and observations.
- [ ] Seed runs once and does not duplicate rows.
- [ ] Create/star/delete operations persist after a new connection.
- [ ] Repository boundary is independent of backend DBMS.
- [ ] Use SQLAlchemy implementation when dependencies are available; standard-library SQLite supports offline run.

## Out of scope
- Cloud database and migrations service.

## Constraints
- Document the tested DB path and ORM path separately.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
