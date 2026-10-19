## Goal
A researcher can add a contextual field note.

## Acceptance criteria
- [ ] Title and body are required with 120/1000 character maximums.
- [ ] Place and comma-separated tags are optional.
- [ ] Invalid submission keeps entered text and identifies missing fields.
- [ ] Successful submission appears selected with provided fields.
- [ ] API mode writes the note to SQLite.

## Out of scope
- Edit/delete, image upload, and non-fieldnote creation.

## Constraints
- Keep client calls in the service layer; API validates inputs.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
