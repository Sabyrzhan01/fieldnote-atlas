## Goal
The same UI can use the HTTP API while mock mode remains usable.

## Acceptance criteria
- [ ] Default mode uses mock service.
- [ ] `?api=1` fetches atlas from API.
- [ ] Creating a note in API mode posts to backend and updates UI.
- [ ] Star in API mode persists server-side.
- [ ] API failure shows visible feedback.

## Out of scope
- Multiuser sync and offline queue.

## Constraints
- No backend calls outside frontend service/data boundary.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
