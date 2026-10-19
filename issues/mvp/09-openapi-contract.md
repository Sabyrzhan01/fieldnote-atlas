## Goal
Frontend and backend share a clear, verifiable contract.

## Acceptance criteria
- [ ] OpenAPI 3 document describes health, atlas, create, star, delete paths.
- [ ] Request/response schemas include required fields and bounds.
- [ ] 400/404/422 behavior is documented.
- [ ] Contract matches actual route behavior.

## Out of scope
- Authentication and collaborative transport.

## Constraints
- Keep root `openapi.yaml` canonical.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
