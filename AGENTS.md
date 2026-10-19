# Fieldnote Atlas

Fieldnote Atlas is a visual field-research workspace for collecting observations, artifacts, interview fragments, and signals, then connecting them to places and each other. Read `docs/spec.md` before changing product behavior.

## Commands
- App: `python3 server.py` (or `npm run dev` if npm is installed)
- Frontend production build: `npm run build`
- Optional FastAPI backend: `cd backend && python3 -m pip install -r requirements.txt && uvicorn app.main:app --reload --port 8091`
- Backend checks: `python3 -m unittest discover -s backend/tests`
- OpenAPI contract: `openapi.yaml`

## Documents
- `docs/process.md` — task lifecycle and iteration stages
- `docs/design-system.md` — visual direction and references for agents
- `docs/testing-guidelines.md` — expected checks and bug workflow
- `docs/task-template.md` — issue grooming template
- `docs/brainstorming.md` — idea exploration before implementation
- `docs/team/pm.md`, `software-engineer.md`, `qa-engineer.md` — role instructions

## Working rules
- GitHub Issues are the canonical backlog after repository setup. Use `mvp`, `post-mvp`, and `user-test-bug` labels.
- Groom issues before implementation. Engineer does not close issues. QA checks acceptance criteria and closes passing issues.
- Implement one issue at a time and record QA evidence. Do not claim remote GitHub actions that were not performed.
- Keep frontend network access in `frontend/src/services/`. The mock service and HTTP service implement the same interface.
- Preserve the build sequence in `docs/process.md`: mock frontend, OpenAPI, in-memory backend, SQLite via SQLAlchemy, then frontend/backend integration.
- Do not add secrets or real personal interview data. Seed content is fictional.
