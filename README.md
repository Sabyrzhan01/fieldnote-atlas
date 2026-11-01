# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas running against the SQLAlchemy and SQLite backend](docs/screenshots/fieldnote-atlas.jpg)

The map is a hand-composed Almaty study surface with selectable evidence pins, a fieldnote reader, and an editorial collection archive.

---

## Assignment 2: Test, Containerise and Deploy

This release enhances Fieldnote Atlas with production containerization, PostgreSQL migration, automated Playwright end-to-end testing, CloudFormation & Terraform infrastructure, and continuous integration/continuous deployment.

### Key Capabilities
- **Single Production Dockerfile:** Bundles static frontend assets and FastAPI backend into a secure, non-root, healthchecked container.
- **SQLite -> PostgreSQL Migration:** Dual-database SQLAlchemy support with automated migration tool (`scripts/migrate_sqlite_to_postgres.py`).
- **Multi-Container Docker Compose:** Production stack orchestrating the application and PostgreSQL 16 (`docker compose up -d`).
- **Playwright End-to-End Suite:** 10 discrete test specifications covering every feature separately, tracked via GitHub issues labeled `e2e-test`.
- **Cloud Deployment Configurations:**
  - **PaaS (Docker Compose):** Render Blueprint (`render.yaml`), Railway (`railway.json`), and Vercel (`vercel.json`).
  - **AWS (Free Tier):** AWS CloudFormation template (`aws/cloudformation.yaml`) deploying to `t2.micro` / `t3.micro` EC2 with 20GB gp3 EBS (\$0 cost guarantee, safely consuming \$100 credit).
  - **Google Cloud (Free Tier):** Terraform configuration (`terraform/`) provisioning Always Free `e2-micro` instance in `us-central1` (\$300 trial credit safe).
- **GitHub Actions CI/CD:** Complete automated pipeline (`.github/workflows/ci-cd.yml`) executing backend tests, PostgreSQL integration tests, frontend checks, Playwright E2E tests, and auto-deploying on merge to `main`.
- **GitHub Issues Backlog:** All features and infrastructure tasks groomed under `issues/e2e-tests/` and `issues/devops/` with automated synchronization script (`scripts/sync_github_issues.py`).

---

## Quick Start with Docker Compose

Run the application and PostgreSQL database with a single command:

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
export DATABASE_URL="postgresql://user:pass@localhost:5432/fieldnote_atlas"
python3 server.py
```

---

## Database Migration (SQLite to PostgreSQL)

To migrate an existing SQLite database into PostgreSQL:

```sh
python scripts/migrate_sqlite_to_postgres.py --source sqlite:///fieldnote-atlas.sqlite3 --target postgresql://fieldnote:fieldnote@localhost:5432/fieldnote_atlas
```

---

## Running Automated Tests

### 1. Unit & Integration Tests (Backend & Frontend)
```sh
# Backend tests (SQLite & SQLAlchemy tests)
python3 -m unittest discover -s backend/tests -v

# Frontend unit tests
node --test frontend/tests/services.test.js
```

### 2. Playwright End-to-End Tests
All features have dedicated Playwright test specs in `tests/e2e/`:

```sh
# Install test dependencies (one-time)
pip install playwright pytest pytest-playwright pytest-asyncio httpx
playwright install chromium

# Run all 11 end-to-end tests headlessly
pytest tests/e2e/ -v
```

Features covered by Playwright specs:
1. `tests/e2e/test_01_editorial_atlas_shell.py` — Editorial Shell, Sidebar, Collections
2. `tests/e2e/test_02_map_pin_selection.py` — Interactive Map Selection & Detail Reader
3. `tests/e2e/test_03_search_observations.py` — Real-Time Title, Body, and Tag Search
4. `tests/e2e/test_04_filter_observations.py` — Filter Cycling (All, Starred, Interviews)
5. `tests/e2e/test_05_create_fieldnote.py` — Observation Modal, Validation, Instant Pin Creation
6. `tests/e2e/test_06_star_observation.py` — Star/Favorite Toggle, Toast Alerts, Persistence
7. `tests/e2e/test_07_tag_navigation.py` — Tag Chip Filter Navigation
8. `tests/e2e/test_08_connected_observations.py` — Connected Evidence Navigation
9. `tests/e2e/test_09_export_atlas.py` — JSON Archive Export Download
10. `tests/e2e/test_10_api_persistence.py` — Full Client-Server API & Database Lifecycle

---

## Deployment Guides

Detailed deployment instructions are documented for each target platform:
- [Render Deployment (Docker Compose)](docs/deployment/render.md)
- [Railway Deployment (Docker Compose)](docs/deployment/railway.md)
- [Vercel Deployment](docs/deployment/vercel.md)
- [AWS CloudFormation Free-Tier Guide](aws/README.md)
- [Google Cloud Platform Terraform Guide](terraform/README.md)

---

## Syncing GitHub Issues

To sync all local groomed issue files to GitHub issues on `Sabyrzhan01/fieldnote-atlas`:

```sh
export GITHUB_TOKEN="your_personal_access_token"
python scripts/sync_github_issues.py
```

---

## Project Structure
- `backend/` — FastAPI application and SQLAlchemy repository supporting PostgreSQL and SQLite
- `tests/e2e/` — Complete Playwright end-to-end test suite
- `issues/e2e-tests/` — Issue specifications for all feature E2E tests (`e2e-test`)
- `issues/devops/` — Issue specifications for Docker, PostgreSQL, PaaS, CloudFormation, Terraform, and CI/CD (`devops`)
- `aws/` — AWS CloudFormation template (`cloudformation.yaml`) and guide
- `terraform/` — GCP Terraform configuration (`main.tf`, `variables.tf`, etc.) and guide
- `docs/deployment/` — PaaS guides for Render, Railway, and Vercel
- `.github/workflows/` — GitHub Actions CI/CD workflow (`ci-cd.yml`)
- `Dockerfile` & `docker-compose.yml` — Container definitions
- `scripts/` — Database migration and GitHub issue sync scripts
