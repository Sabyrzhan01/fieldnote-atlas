# Fieldnote Atlas

Fieldnote Atlas is a visual field-research workspace for collecting observations, artifacts, interview fragments, and signals, then connecting them to places and each other. Read `docs/spec.md` before changing product behavior.

## Commands
- Full-stack Docker Compose (`app` + `postgres:16-alpine` on `:8000`): `docker compose up --build`
- Local Backend (FastAPI + SQLAlchemy + Alembic): install `backend/requirements.txt`, run `alembic upgrade head && python -m scripts.seed_db`, then `uvicorn backend.app.main:app --host 0.0.0.0 --port 8000`
- Frontend production build (`frontend/dist`): `cd frontend && npm install && npm run build`
- Frontend unit tests (Vitest): `cd frontend && npm test`
- Backend & PostgreSQL repository checks: `pytest backend/tests/test_repository.py -v`
- Playwright E2E suite (11 specs against Docker Compose stack): `npx playwright test`
- Mock-service frontend mode: open `/?mock=1`
- OpenAPI contract: `openapi.yaml`

## Documents
- `docs/process.md` — task lifecycle and iteration stages
- `docs/design-system.md` — visual direction and references for agents
- `docs/testing-guidelines.md` — expected checks and bug workflow
- `docs/task-template.md` — issue grooming template
- `docs/brainstorming.md` — idea exploration before implementation
- `docs/team/pm.md`, `software-engineer.md`, `qa-engineer.md` — role instructions
- `docs/deployment/` — Railway, Render, and Vercel deployment guides
- `infra/README.md` — AWS CloudFormation (`infra/aws/template.yaml`) and GCP Terraform (`infra/gcp/*.tf`) free-tier infrastructure guides

## Working rules
- GitHub Issues are the canonical backlog. Use `mvp`, `post-mvp`, `user-test-bug`, `cleanup`, `database`, `docker`, `e2e-test`, `ci-cd`, `deploy`, and `infrastructure` labels.
- Groom issues before implementation. Close issues only after verification and passing checks.
- The canonical frontend lives in `frontend/` (`frontend/index.html`, `frontend/app.js`, `frontend/services.js`, `frontend/style.css`). FastAPI (`backend/app/main.py`) serves the built SPA from `frontend/dist` and REST endpoints under `/api/*` on port `8000`.
- Do not add secrets or real personal interview data. Seed content is fictional; configuration uses environment variables (`.env.example`).
