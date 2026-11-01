# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas running against the SQLAlchemy and SQLite backend](docs/screenshots/fieldnote-atlas.jpg)

The map is a hand-composed Almaty study surface with selectable evidence pins, a fieldnote reader, and an editorial collection archive.

---

## Live Deployment & CI/CD Status

- **Live Web Application (Auto-Redeployed on Every Commit to `main`):** [https://sabyrzhan01.github.io/fieldnote-atlas/](https://sabyrzhan01.github.io/fieldnote-atlas/)
- **Production Container Image (GHCR, Auto-Published on Commit):** `ghcr.io/sabyrzhan01/fieldnote-atlas:latest`
- **GitHub Actions CI/CD Pipeline & Deployment Runs:** [https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/ci-cd.yml](https://github.com/Sabyrzhan01/fieldnote-atlas/actions/workflows/ci-cd.yml)
- **GitHub Issues Backlog (Closed with Verification Evidence):** [https://github.com/Sabyrzhan01/fieldnote-atlas/issues?q=is%3Aissue](https://github.com/Sabyrzhan01/fieldnote-atlas/issues?q=is%3Aissue)

---

## Assignment 2: Test, Containerise and Deploy

This release equips Fieldnote Atlas with a single-container full-stack `Dockerfile`, SQLite-to-PostgreSQL migration, multi-container `docker-compose.yml` orchestration, 10 Playwright end-to-end feature tests, CloudFormation and Terraform IaC templates, and an automated GitHub Actions CI/CD pipeline.

### Key Capabilities
- **Single Production Dockerfile (`Dockerfile`):** Bundles static frontend assets (`index.html`, `app.js`, `services.js`, `style.css`, `openapi.yaml`) and the FastAPI backend into a single non-root container with a built-in `/api/health` `HEALTHCHECK`.
- **SQLite -> PostgreSQL Migration (`backend/app/repository.py`, `scripts/migrate_sqlite_to_postgres.py`):** Dual-engine `SQLAlchemyRepository` supporting both SQLite and PostgreSQL (`postgresql://` and `postgres://` URI normalization, `pool_pre_ping=True`) plus an idempotent upsert migration script that preserves custom observations, tags, coordinates, and mutated seed states (such as toggled stars).
- **Multi-Container Docker Compose (`docker-compose.yml`):** Orchestrates the `web` container (`Dockerfile`) and `db` (`postgres:16-alpine` with `pg_isready` healthcheck and persistent `pgdata` volume).
- **Playwright End-to-End Suite (`tests/e2e/`):** **10 end-to-end test files (10 Playwright test functions)** covering every application feature separately, tracked 1-to-1 in GitHub issues `#40`–`#49` labeled `e2e-test`.
- **GitHub Actions CI/CD (`.github/workflows/ci-cd.yml`):** Runs 4 verification jobs on every push/PR (`test-backend` with PostgreSQL 16 migration verification, `test-frontend`, `test-e2e` running all 10 Playwright browser tests against PostgreSQL 16, and `test-docker-compose` booting and smoke-testing `docker-compose.yml`) before automatically publishing `ghcr.io/sabyrzhan01/fieldnote-atlas:latest` and redeploying the live web app on every push to `main`.

---

## Platform Distinction: Docker Compose on Railway vs. Render vs. Vercel

The assignment prompt mentions deploying to *"Render, Vercel, Railway - with Docker Compose only."* Because these three PaaS providers handle containers and `docker-compose.yml` very differently, we document the exact architectural distinction below and choose **Railway** (along with Docker Compose on AWS EC2 / GCP Compute Engine and CI) as the primary true Docker Compose target:

| Platform | Native `docker-compose.yml` Support? | How It Works & Repository Configuration | Official Documentation |
|---|---|---|---|
| **Railway (Chosen Compose PaaS Target)** | **Yes (Imports `docker-compose.yml` services)** | Railway supports importing `docker-compose.yml` directly into a project canvas, provisioning both the `web` (`Dockerfile`) service and the `db` (`postgres:16-alpine`) service + `pgdata` volume together. Also supports `railway.json`. ([Guide](docs/deployment/railway.md)) | [Railway Docker & Compose Docs](https://docs.railway.com/builds/dockerfiles) |
| **Render** | **No (Uses `render.yaml` Blueprint instead)** | Render does not run `docker-compose.yml` directly. Instead, `render.yaml` defines two separate Render resources: a Docker web service (`fieldnote-atlas` built from `Dockerfile`) and a managed Render PostgreSQL database (`fieldnote-atlas-db`) linked via `DATABASE_URL`. ([Guide](docs/deployment/render.md)) | [Render Docker Docs](https://render.com/docs/docker) |
| **Vercel** | **No (Serverless/Edge only; cannot run Compose)** | Vercel explicitly does not deploy `docker-compose.yml` or long-running stateful Docker/PostgreSQL containers. It requires its own `vercel.json` configuration to host static/edge assets and proxy `/api/*` requests to an external container backend (such as Railway or Render). ([Guide](docs/deployment/vercel.md)) | [Vercel Docker Compose Guidance](https://vercel.com/i/can-you-run-docker-compose-on-vercel) |
| **AWS EC2 & GCP GCE** | **Yes (Runs `docker compose up -d --build`)** | Both `aws/cloudformation.yaml` and `terraform/main.tf` install Docker + the Docker Compose plugin on a Linux VM and execute `docker compose up -d --build` directly from `docker-compose.yml`. | [AWS Guide](aws/README.md) · [GCP Guide](terraform/README.md) |

---

## AWS CloudFormation & GCP Terraform: Free Tier & Billing Notes

- **AWS CloudFormation (`aws/cloudformation.yaml`, [Guide](aws/README.md)):**
  - Provisions a single `t2.micro` or `t3.micro` EC2 instance with a 20 GB `gp3` EBS volume (`DeleteOnTermination: true`) and runs the full stack (`web` + `postgres:16-alpine`) via Docker Compose on the instance.
  - **No Paid Managed Add-ons:** Avoids NAT Gateways, Application Load Balancers, and managed RDS instances so it can run inside an AWS Free Account (`$100` promotional credits) without enabling paid-only account tiers.
  - **Billing & Public IPv4 Caveat:** AWS does **not** guarantee `$0` billing unconditionally. Charges can apply if usage exceeds Free Tier time/volume limits or available account credits, and AWS charges `$0.005/hour` for in-use public IPv4 addresses depending on your account's plan and Free Tier eligibility. See [AWS Free Tier guidance](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html) and [AWS EC2 Instance Addressing / Public IPv4 pricing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html). Always run `aws cloudformation delete-stack --stack-name fieldnote-atlas` when finished testing.
- **Google Cloud Terraform (`terraform/`, [Guide](terraform/README.md)):**
  - Provisions 1× `e2-micro` Compute Engine VM in `us-central1` with a 25 GB `pd-standard` disk, matching Google Cloud's Always Free tier quotas and `$300` Free Trial credit allowances. Run `terraform destroy` when finished to avoid consuming credits or network egress quotas.

---

## Quick Start with Docker Compose

Run the complete application (`Dockerfile` web service + `postgres:16-alpine` database) with a single command:

```sh
docker compose up -d --build
```

Open `http://127.0.0.1:8091/`. Health endpoint is at `http://127.0.0.1:8091/api/health`.

To stop the containers:
```sh
docker compose down
```

---

## Run Locally (Python Virtual Environment)

Requirement: Python 3.11+ and dependencies in `backend/requirements.txt`.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python3 server.py
```

Open `http://127.0.0.1:8091/`. Data defaults to SQLite (`fieldnote-atlas.sqlite3`).
To connect to PostgreSQL, set:
```sh
export DATABASE_URL="postgresql://fieldnote:fieldnote@localhost:5432/fieldnote_atlas"
python3 server.py
```

---

## Database Migration (SQLite to PostgreSQL) & What CI Asserts

To migrate an existing SQLite database into PostgreSQL:

```sh
python scripts/migrate_sqlite_to_postgres.py \
  --source sqlite:///fieldnote-atlas.sqlite3 \
  --target postgresql://fieldnote:fieldnote@localhost:5432/fieldnote_atlas
```

### What the CI Migration Tests Assert
In `.github/workflows/ci-cd.yml` (`test-backend` job) and `backend/tests/test_repository.py` (`test_database_migration_tool`), migration verification tests meaningful custom and mutated data rather than only default seed rows:
1. **Custom Observation Creation in Source SQLite:** Inserts custom non-seeded observations (`"Migrated canal telemetry"` in collection `c2` and `"Steppe windbreak survey"` in collection `c3`) with custom coordinates (`x`, `y`), tags (`["migrated", "hydrology"]`, `["steppe", "trees", "railway"]`), and `starred=True`.
2. **Seed State Mutation in Source SQLite:** Toggles `starred` on seeded observation `id="2"` (`"“We wait for the second bus”"`, which is initially `starred=False` in seed data) to `starred=True`.
3. **Upsert Migration into Live PostgreSQL 16:** Runs `scripts/migrate_sqlite_to_postgres.py` against the `postgres:16-alpine` service container (`seed_if_empty=False` + `session.merge()`).
4. **PostgreSQL & FastAPI `/api/atlas` Assertions:**
   - Asserts total row counts match exactly (`3` collections, `7` observations) with zero duplicate seed rows.
   - Queries PostgreSQL directly and through FastAPI `TestClient` (`GET /api/atlas`) to assert that the custom observations exist with their exact `collection_id`, `place`, `tags`, `starred`, and `x`/`y` coordinates, that observation `#2` preserved its mutated `starred=True` state, and that collection observation counts (`observationCount`) updated accurately.

---

## Running Automated Tests & Playwright E2E Assertions

### 1. Unit & Integration Tests (Backend & Frontend)
```sh
# Backend unit & migration tests (10 tests in backend/tests/test_repository.py)
python3 -m unittest discover -s backend/tests -v

# Frontend service unit tests (4 tests in frontend/tests/services.test.js)
node --test frontend/tests/services.test.js
```

### 2. Playwright End-to-End Tests (10 Feature Specs / 10 Tests)
All 10 features have dedicated Playwright test specs in `tests/e2e/` (10 test files containing 10 test functions, executed against live PostgreSQL 16 in CI):

```sh
# Install test dependencies (one-time)
pip install playwright pytest pytest-playwright pytest-asyncio httpx
playwright install chromium

# Run all 10 end-to-end tests headlessly
pytest tests/e2e/ -v
```

| # | Test File | GitHub Issue | What the Browser Test Asserts |
|---|---|---|---|
| 1 | `tests/e2e/test_01_editorial_atlas_shell.py` | [#40](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/40) | Renders `FIELDNOTE ATLAS / STUDIO` brandmark, workspace card, 3 sidebar collections with counts, topbar breadcrumb/pill, and switches active collection to `"Quiet infrastructures"`. |
| 2 | `tests/e2e/test_02_map_pin_selection.py` | [#41](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/41) | Renders Almaty map surface with 6 distinct coordinate pins; clicking pin `"“We wait for the second bus”"` transfers `.pin-active` class and updates the detail panel title, place (`Dostyk × Satpaev`), and type (`INTERVIEW`). |
| 3 | `tests/e2e/test_03_search_observations.py` | [#42](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/42) | Filters map pins and detail view in real time by title (`"puddles"` -> 1 pin), tag (`"transit"` -> 1 pin), body (`"asphalt"` -> 1 pin), nonexistent query (`0` pins + `.empty-detail` state), and restores all 6 pins when cleared. |
| 4 | `tests/e2e/test_04_filter_observations.py` | [#43](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/43) | Cycles `#filter` button through `All notes` (6 pins) -> `Starred` (2 starred pins, `Unstar observation` aria-label) -> `Interviews` (2 interview pins, `INTERVIEW` badge) -> back to `All notes` (6 pins). |
| 5 | `tests/e2e/test_05_create_fieldnote.py` | [#44](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/44) | Verifies opening `#noteForm` modal and clicking `#cancel` leaves pin count unchanged; then submits `"Zhibek Zholy Metro Mosaic"` with place and comma-separated tags, asserting toast notification, pin count increment (`6 -> 7`), and detail reader selection. |
| 6 | `tests/e2e/test_06_star_observation.py` | [#45](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/45) | Selects unstarred observation, clicks `#star` (`♡ -> ♥`), verifies toast `"Added to starred observations"`, reloads page (`page.reload()`) to assert backend database persistence, and toggles back off (`♥ -> ♡`). |
| 7 | `tests/e2e/test_07_tag_navigation.py` | [#46](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/46) | Clicks `#rain` tag chip (`button[data-tag='rain']`) in detail reader and asserts `#search` input populates with `"rain"` and map pins narrow to matching observations. |
| 8 | `tests/e2e/test_08_connected_observations.py` | [#47](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/47) | Clicks `#connected` evidence button on observation `#1` and asserts active detail reader and `.pin-active` map pin navigate to linked observation `"“We wait for the second bus”"`. |
| 9 | `tests/e2e/test_09_export_atlas.py` | [#48](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/48) | Intercepts browser download on `#export` click, asserts filename `fieldnote-atlas.json`, parses downloaded JSON, and asserts >= 6 observations with required schema keys (`id`, `title`, `body`, `place`, `tags`). |
| 10 | `tests/e2e/test_10_api_persistence.py` | [#49](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/49) | Verifies `GET /api/health` (`200 OK`), creates `"PostgreSQL Persistence Note"` in browser UI, queries `GET /api/atlas` via HTTP client to assert DB storage, deletes it via `DELETE /api/observations/{id}`, reloads UI, and asserts pin removal. |

---

## Deployment Guides

Detailed deployment instructions and platform caveats are documented in:
- [Railway Deployment (Recommended Docker Compose Import)](docs/deployment/railway.md)
- [Render Deployment (Blueprint Alternative to Compose)](docs/deployment/render.md)
- [Vercel Deployment (Edge/Serverless Caveats & API Proxy)](docs/deployment/vercel.md)
- [AWS CloudFormation Free-Tier Sized Guide](aws/README.md)
- [Google Cloud Platform Terraform Guide](terraform/README.md)

---

## Syncing GitHub Issues

To sync local groomed issue files to GitHub issues on `Sabyrzhan01/fieldnote-atlas`:

```sh
export GITHUB_TOKEN="your_personal_access_token"
python scripts/sync_github_issues.py
```

---

## Project Structure
- `backend/` — FastAPI application and SQLAlchemy repository supporting PostgreSQL and SQLite
- `tests/e2e/` — 10 Playwright end-to-end feature test specs (`test_01` through `test_10`)
- `issues/e2e-tests/` — Issue specifications for all 10 feature E2E tests (`e2e-test`, GitHub Issues `#40`–`#49`)
- `issues/devops/` — Issue specifications for Docker, PostgreSQL, PaaS, CloudFormation, Terraform, and CI/CD (`devops`, GitHub Issues `#33`–`#39`)
- `aws/` — AWS CloudFormation template (`cloudformation.yaml`) and billing/deployment guide
- `terraform/` — GCP Terraform configuration (`main.tf`, `variables.tf`, `outputs.tf`) and guide
- `docs/deployment/` — PaaS guides for Railway, Render, and Vercel
- `.github/workflows/` — GitHub Actions CI/CD workflow (`ci-cd.yml`)
- `Dockerfile` & `docker-compose.yml` — Container and multi-container Compose definitions
- `scripts/` — SQLite-to-PostgreSQL migration and GitHub issue sync scripts
