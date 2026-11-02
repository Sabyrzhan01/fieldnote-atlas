# Fieldnote Atlas

[![CI](https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/ci.yml/badge.svg)](https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/ci.yml)
[![CD](https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/cd.yml/badge.svg)](https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/cd.yml)

**Fieldnote Atlas** is a warm editorial urban research and spatial notes platform for organizing field observations, oral interviews, architectural artifacts, and street-level signals on an interactive Almaty map.

- **Full-Stack Container Image (GHCR)**: `ghcr.io/sabyrzhan01/fieldnote-atlas:latest` (FastAPI + Vite SPA + Alembic PostgreSQL migrations on `:8000`)
- **Full-Stack PaaS Blueprints**: [`render.yaml`](./render.yaml) (Render Docker Web Service + Managed PostgreSQL) & [`railway.json`](./railway.json) / [`docker-compose.yml`](./docker-compose.yml) (Railway)
- **Static UI Preview (GitHub Pages — client-side mock mode only)**: **[https://sabyrzhan01.github.io/fieldnote-atlas/](https://sabyrzhan01.github.io/fieldnote-atlas/)**
- **GitHub Issues Tracker**: **[https://github.com/Sabyrzhan01/fieldnote-atlas/issues](https://github.com/Sabyrzhan01/fieldnote-atlas/issues)**

---

## 1. Architecture & Repository Structure

The project follows a clean two-tier architecture packaged into a single multi-stage container:

1. **Frontend (`frontend/`)**: Vite-built ES-module Single Page Application (`index.html`, `app.js`, `services.js`, `style.css`) with Vitest unit tests (`frontend/tests/services.test.js`).
2. **Backend (`backend/app/`)**: Single FastAPI + SQLAlchemy 2.0 backend (`main.py`, `repository.py`, `schemas.py`, `seed.py`) connected to **PostgreSQL 16** via `psycopg` (`DATABASE_URL`), managed with **Alembic** migrations (`alembic.ini`, `backend/alembic/`) and idempotent seeding (`scripts/seed_db.py`). FastAPI serves both the REST API (`/api/*`) and the compiled frontend static bundle (`frontend/dist`) with SPA fallback on a single port (`:8000`).
3. **E2E Suite (`e2e/`)**: 11 isolated Playwright TypeScript spec files (`e2e/01-first-render-seed.spec.ts` through `e2e/11-api-health.spec.ts`), one per application feature and GitHub Issue (`#54`–`#64`), resetting database state between tests via `POST /api/test/reset`.
4. **Infrastructure as Code (`infra/`)**: Free-tier-compliant **AWS CloudFormation** (`infra/aws/template.yaml`) and **GCP Terraform** (`infra/gcp/*.tf`) with `$5/month` budget alerts and zero paid add-ons.

```text
fieldnote-atlas/
├── .github/workflows/
│   ├── ci.yml                  # Stage 5: frontend-test, backend-test (Postgres 16), integration, e2e, docker-build
│   └── cd.yml                  # Stage 5/6: auto-redeploy on green CI on main (GHCR + GitHub Pages + Render/Railway/OIDC)
├── backend/
│   ├── alembic/                # Stage 1: Alembic environment & 0001_initial_schema.py migration
│   ├── app/                    # Stage 0/1/2: Single FastAPI + SQLAlchemy 2.0 + StaticFiles SPA backend
│   ├── tests/                  # Stage 1/4: Pytest repository & OpenAPI schema tests (runs against Postgres 16)
│   └── requirements.txt
├── frontend/
│   ├── index.html              # Editorial Atlas SPA entry point
│   ├── app.js                  # Interactive UI controller
│   ├── services.js             # API & Mock service layer
│   ├── style.css               # Warm editorial theme
│   ├── package.json            # Vite build & Vitest unit test runner
│   ├── vite.config.js          # Vite bundler config (outputs to frontend/dist)
│   └── tests/services.test.js  # Frontend unit tests (Vitest)
├── e2e/                        # Stage 4: 11 Playwright E2E spec files (Issues #54–#64)
├── infra/                      # Stage 7: Production IaC + cost controls
│   ├── aws/template.yaml       # AWS CloudFormation (ECS t3.micro, Single-AZ RDS db.t3.micro, ECR, Secrets Manager, Budget)
│   ├── gcp/                    # GCP Terraform (Cloud Run, Cloud SQL db-f1-micro, Artifact Registry, Billing Budget)
│   └── README.md               # Deploy commands, expected cost ($0/mo free tier), teardown, and budget alert docs
├── scripts/
│   ├── seed_db.py              # Stage 1: Standalone idempotent PostgreSQL/SQLite seed script
│   └── migrate_sqlite_to_postgres.py # Stage 1: SQLite -> PostgreSQL migration utility
├── Dockerfile                  # Stage 2: Multi-stage build (Node 20 Vite build -> Python 3.11-slim non-root + HEALTHCHECK)
├── docker-compose.yml          # Stage 3: Production stack (app + postgres:16-alpine with healthcheck & startup migrations)
├── docker-compose.test.yml     # Stage 3/4: Isolated E2E test stack with tmpfs Postgres & ENABLE_TEST_RESET=1
├── render.yaml                 # Stage 6: Render Docker + free Postgres blueprint
├── railway.json                # Stage 6: Railway Dockerfile deployment config
└── .env.example                # Environment variable template (no secrets committed)
```

---

## 2. Quickstart: Run with Docker Compose (`:8000`)

From a clean checkout, copy `.env.example` (optional) and start the full PostgreSQL 16 + FastAPI + Vite SPA stack:

```bash
cp .env.example .env
docker compose up --build
```

What happens automatically on startup:
1. `db` (`postgres:16-alpine`) starts with a named volume (`pgdata`) and passes its `pg_isready` healthcheck.
2. `app` waits for `db` (`condition: service_healthy`), runs `alembic upgrade head`, seeds the 3 collections and 6 Almaty observations via `python -m scripts.seed_db`, and serves both the SPA and REST API on **`http://localhost:8000`**.
3. Verify healthcheck:
   ```bash
   curl -fsS http://localhost:8000/api/health
   # {"status":"ok"}
   ```

---

## 3. Database Migrations & Seeding (Stage 1)

Run Alembic migrations and seed data against any PostgreSQL (`DATABASE_URL`) database:

```bash
export DATABASE_URL="postgresql+psycopg://fieldnote:fieldnote@localhost:5432/fieldnote_atlas"
alembic upgrade head
python -m scripts.seed_db
```

To migrate legacy SQLite records into PostgreSQL:

```bash
python scripts/migrate_sqlite_to_postgres.py \
  --source sqlite:///./legacy.db \
  --target postgresql+psycopg://fieldnote:fieldnote@localhost:5432/fieldnote_atlas
```

---

## 4. Running Tests (Stage 4)

### Frontend Unit Tests (Vitest)
```bash
cd frontend
npm install
npm test
```

### Backend Unit & Integration Tests (Pytest + PostgreSQL)
```bash
export DATABASE_URL="postgresql+psycopg://fieldnote:fieldnote@localhost:5432/fieldnote_test"
pytest backend/tests/test_repository.py -v
```

### Playwright End-to-End Tests against Docker Compose Stack
```bash
docker compose -f docker-compose.test.yml up -d --build
npx playwright test
docker compose -f docker-compose.test.yml down -v
```

Each E2E feature has its own dedicated spec file and GitHub Issue:
| Spec File | Feature Verified | GitHub Issue |
|---|---|---|
| `e2e/01-first-render-seed.spec.ts` | First render, editorial shell, 3 collections, 6 seeded pins | [#54](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/54) |
| `e2e/02-search.spec.ts` | Real-time search across title, body, and tags | [#55](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/55) |
| `e2e/03-starred-filter.spec.ts` | Filter cycling (`All notes` -> `Starred` -> `Interviews`) | [#56](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/56) |
| `e2e/04-create-entry.spec.ts` | Create observation modal and instant map/detail update | [#57](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/57) |
| `e2e/05-form-validation.spec.ts` | Required form validation & `422` API schema rejection | [#58](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/58) |
| `e2e/06-star-unstar.spec.ts` | Star/unstar toggle with toast feedback | [#59](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/59) |
| `e2e/07-delete-observation.spec.ts` | Delete observation via options modal | [#60](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/60) |
| `e2e/08-collections-empty-state.spec.ts` | Collection switching & empty collection detail state | [#61](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/61) |
| `e2e/09-map-markers.spec.ts` | Map markers selection, zoom controls, and layer switching | [#62](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/62) |
| `e2e/10-persistence-reload.spec.ts` | PostgreSQL persistence across full page reload | [#63](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/63) |
| `e2e/11-api-health.spec.ts` | `GET /api/health` and `GET /api/atlas` REST contract | [#64](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/64) |

---

## 5. CI/CD & Full-Stack Deployment (Stages 5, 6 & 7)

- **Continuous Integration ([`.github/workflows/ci.yml`](./.github/workflows/ci.yml))**: Triggered on every `push` and `pull_request` with 5 jobs:
  1. `frontend-test`: Vitest unit tests + Vite production build (`frontend/dist`)
  2. `backend-test`: Alembic migration + seed script + Pytest repository & SQLite-to-PostgreSQL migration suite against `postgres:16-alpine`
  3. `integration`: Live FastAPI + PostgreSQL 16 HTTP integration verification (`/api/health`, `/api/atlas`, `/api/test/reset`)
  4. `e2e`: Full Docker Compose stack (`docker-compose.test.yml`) + 11 Playwright E2E spec files + `playwright-e2e-report` artifact upload
  5. `docker-build`: Multi-stage `Dockerfile` build with BuildKit cache + non-root `appuser` and `/api/health` smoke test
- **Continuous Deployment ([`.github/workflows/cd.yml`](./.github/workflows/cd.yml))**: Triggered **strictly after** a successful `CI` workflow run on `main` (`workflow_run` with `conclusion == 'success'`). Publishes `ghcr.io/sabyrzhan01/fieldnote-atlas:latest`, updates the GitHub Pages static UI preview, and triggers Render/Railway deploy webhooks (`RENDER_DEPLOY_HOOK_URL` / `RAILWAY_WEBHOOK_URL`).
- **Full-Stack PaaS Deployment (Render or Railway)**:
  - **Render Blueprint ([`render.yaml`](./render.yaml) — [guide](./docs/deployment/render.md))**:
    1. In [Render Dashboard](https://dashboard.render.com/), click **New + → Blueprint** and select `Sabyrzhan01/fieldnote-atlas`.
    2. Render provisions the Docker web service (`fieldnote-atlas` on `PORT=8000`, `healthCheckPath: /api/health`) and free PostgreSQL database (`fieldnote-atlas-db`), injecting `DATABASE_URL` automatically.
    3. Optional: Add the Render Deploy Hook URL to GitHub Repository Secrets as `RENDER_DEPLOY_HOOK_URL`.
  - **Railway ([`railway.json`](./railway.json) & [`docker-compose.yml`](./docker-compose.yml) — [guide](./docs/deployment/railway.md))**:
    1. In [Railway](https://railway.app/), click **New Project → Import Docker Compose** (upload `docker-compose.yml`) or **Deploy from GitHub repo** (`Sabyrzhan01/fieldnote-atlas`) + **Add PostgreSQL** (`DATABASE_URL`).
    2. Generate a public domain on port `8000` and verify `/api/health` (`{"status":"ok"}`) and `/api/atlas`.
- **Cloud IaC ([`infra/README.md`](./infra/README.md))**: Free-tier AWS CloudFormation ([`infra/aws/template.yaml`](./infra/aws/template.yaml)) and GCP Terraform ([`infra/gcp/`](./infra/gcp/)) with `$5/month` budget alerts and teardown instructions.

---

## 6. Stage Issue Tracker (`#50`–`#67`)

- **Stage 0 (`cleanup`)**: [#50](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/50)
- **Stage 1 (`database`)**: [#51](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/51)
- **Stage 2 (`docker` — Dockerfile)**: [#52](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/52)
- **Stage 3 (`docker` — Docker Compose)**: [#53](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/53)
- **Stage 4 (`e2e-test`)**: [#54](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/54) – [#64](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/64)
- **Stage 5 (`ci-cd`)**: [#65](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/65)
- **Stage 6 (`deploy`)**: [#66](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/66)
- **Stage 7 (`infrastructure`)**: [#67](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/67)
