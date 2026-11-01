# DevOps: Multi-Container Docker Compose Stack (App + PostgreSQL)

**Labels:** `devops`, `docker`

## Goal
Provide a turn-key multi-container stack running Fieldnote Atlas alongside a dedicated PostgreSQL database container.

## Description
- `docker-compose.yml` orchestrating:
  - `web` service: built from root `Dockerfile`, exposed on port `8091`, connected to `db`.
  - `db` service: `postgres:16-alpine`, persistent volume `postgres_data`, credentials and healthcheck via `pg_isready`.
- Includes healthcheck dependencies so the web service only boots after PostgreSQL is fully ready to accept connections.
- Easily runnable via `docker compose up -d`.

## Deliverables
- `docker-compose.yml`

## Acceptance Criteria
- [x] `docker compose config` validates cleanly.
- [x] `web` service depends on `db` healthcheck.
- [x] Persistent volume preserves database records across container restarts.
