# Fieldnote Atlas

Fieldnote Atlas is a visual field-research workspace for collecting observations, artifacts, interview fragments, and signals, then connecting them to places and each other. Read `docs/spec.md` before changing product behavior.

## Commands
- App (FastAPI + SQLAlchemy/SQLite): install `backend/requirements.txt`, then run `python3 server.py` (or `npm run dev` if npm is installed)
- Frontend production build: `npm run build`
- In-memory workflow stage: `FIELDNOTE_REPOSITORY=memory python3 server.py`
- Mock-service frontend stage: open `/?mock=1`
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
- The canonical frontend entry is `index.html`, `app.js`, and `style.css`. Keep API calls behind a small service boundary where practical.
- Preserve the build sequence in `docs/process.md`: mock frontend, OpenAPI, in-memory backend, SQLite via SQLAlchemy, then frontend/backend integration.
- Do not add secrets or real personal interview data. Seed content is fictional.
