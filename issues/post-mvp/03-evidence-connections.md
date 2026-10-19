# Post-MVP: Create and explore evidence connections

## Goal
Researchers can create typed, persisted relationships between observations and traverse the linked evidence.

## Acceptance criteria
- [ ] Connection records have their own persistent model and stable identifiers.
- [ ] A researcher can connect two existing observations with a relationship type and note.
- [ ] The observation detail shows its actual connections rather than a hard-coded sample.
- [ ] Deleting an endpoint removes or explicitly resolves its related connections.
- [ ] API contract, SQLite behavior, and UI are covered by tests.

## Out of scope
- Cross-workspace collaboration and graph analytics.

## Constraints
- Use SQLAlchemy relationships or foreign keys and the documented OpenAPI contract.
- Do not show invented static connections as saved user data.
