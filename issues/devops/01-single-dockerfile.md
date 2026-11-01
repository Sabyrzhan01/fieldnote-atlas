# DevOps: Single Production Dockerfile (Connected Static Frontend + Backend)

**Labels:** `devops`, `docker`

## Goal
Package the static frontend and FastAPI backend into a single production-ready, secure Docker container.

## Description
Create a multi-purpose `Dockerfile`:
- Uses lightweight `python:3.11-slim` base image.
- Copies and serves static assets (`index.html`, `app.js`, `style.css`, `services.js`, `docs/`) via FastAPI root mount.
- Installs Python dependencies (`fastapi`, `SQLAlchemy`, `psycopg2-binary`, `uvicorn`).
- Enforces non-root security execution (`USER appuser`).
- Respects dynamic `$PORT` and `$HOST` environment variables for cloud portability.
- Built-in container healthcheck querying `/api/health`.

## Deliverables
- `Dockerfile`
- `.dockerignore`

## Acceptance Criteria
- [x] Docker image builds cleanly with `docker build -t fieldnote-atlas .`.
- [x] Container serves static frontend at root `/` and API at `/api/`.
- [x] Non-root user execution confirmed.
- [x] Healthcheck passes.
