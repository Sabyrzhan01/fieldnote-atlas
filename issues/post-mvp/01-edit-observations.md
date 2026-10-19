# Post-MVP: Edit existing observations

## Goal
Researchers can correct a saved fieldnote without losing its collection, source, tags, or map placement.

## Acceptance criteria
- [ ] An edit action opens a form populated with the selected observation.
- [ ] Save validates title/body and preserves optional fields not changed.
- [ ] Cancel leaves the stored observation unchanged.
- [ ] Edited values survive a reload with SQLite persistence.

## Out of scope
- Bulk editing and revision history.

## Constraints
- Use the OpenAPI contract and SQLAlchemy repository boundary.
- Add service/API and browser regression coverage.
