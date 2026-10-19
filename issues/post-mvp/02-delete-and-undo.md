# Post-MVP: Delete observations with undo

## Goal
Researchers can remove an observation from an atlas and recover from an accidental deletion.

## Acceptance criteria
- [ ] A delete action names the selected observation before removal.
- [ ] Successful deletion removes its pin, detail, and count.
- [ ] A visible undo action restores the observation within the stated undo window.
- [ ] Deletion and restoration persist across reloads.

## Out of scope
- Permanent database purge and bulk deletion.

## Constraints
- Keep server deletion behind SQLAlchemy repository methods.
- Test cancellation, undo timeout, and missing IDs.
