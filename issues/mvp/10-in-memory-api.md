## Goal
The API contract works without persistent storage for rapid integration.

## Acceptance criteria
- [ ] Health and atlas return documented response shapes.
- [ ] Create validates and returns created note.
- [ ] Star toggles existing note.
- [ ] Missing IDs return 404.
- [ ] Memory repository can be replaced without changing route contract.

## Out of scope
- SQLite and authentication.

## Constraints
- Keep storage behind a repository boundary.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
