# Post-MVP: Create and manage collections

## Goal
Researchers can create, rename, and archive collections for distinct field studies.

## Acceptance criteria
- [ ] Create validates a non-empty title and assigns a stable ID.
- [ ] Rename updates the collection name without moving observations.
- [ ] Archive behavior explains what happens to contained observations.
- [ ] Collection counts remain correct after create, rename, archive, and reload.

## Out of scope
- Shared permissions and cross-user ownership.

## Constraints
- Enforce collection foreign keys in SQLAlchemy.
- Cover empty, populated, and invalid collection cases.
