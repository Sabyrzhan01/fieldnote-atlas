# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas concept: editorial map-led research archive](docs/design-system.md)

## Run locally

Requirement: Python 3.11+ (no third-party packages are needed for the runnable edition).

```sh
python3 server.py
```

Open `http://127.0.0.1:8091/` for the localStorage mock-service edition. Open `http://127.0.0.1:8091/?api=1` for the frontend connected to the SQLite API. The API can be checked at `/api/health` and `/api/atlas`.

The default runnable API uses Python's SQLite DB-API so it can run offline with the system Python. `backend/app/` also contains a FastAPI API with in-memory and SQLAlchemy repository implementations. Install `backend/requirements.txt` to run that ORM-backed path; it has been exercised with FastAPI's test client and a SQLite database.

Optional frontend convenience commands, if `npm` is available:

```sh
npm run dev
npm test
npm run build
```

`npm run dev` delegates to the same dependency-free Python server. SQLite state is written to `fieldnote.db`; use `FIELDNOTE_DB_PATH` to choose another file.

## Project map
- `frontend/` — React, TypeScript, Vite; mock and API service implementations
- `backend/` — FastAPI; in-memory and SQLAlchemy repository modes
- `openapi.yaml` — frontend/backend contract
- `docs/` — product spec, brainstorm, design brief, test/process guidance, backlog, role briefs

## Workflow
This project follows the staged path in `docs/process.md`: mock-backed frontend → OpenAPI contract → in-memory backend → SQLite through SQLAlchemy → integrated frontend/backend. The GitHub repository is [Sabyrzhan01/fieldnote-atlas](https://github.com/Sabyrzhan01/fieldnote-atlas). It has the `mvp`, `post-mvp`, and `user-test-bug` labels. Groomed MVP issue bodies are in `issues/mvp/`; the GitHub backlog has 14 MVP issues and two user-test-bug issues, each with QA comments and closed after passing checks.

## Status
Runnable dependency-free edition and the optional FastAPI/SQLAlchemy edition are verified. API checks passed for seed, selected-collection create, invalid input, star, SQLite persistence across fresh processes, delete, and not-found. The Chrome walkthrough verified first render, search, starred filtering, local mock creation, SQLite API-backed creation, and collection scoping including the empty state. JavaScript/Python syntax checks, OpenAPI parsing, five repository tests, in-memory API checks, and SQLAlchemy persistence checks pass. Both real browser bugs were recorded as `user-test-bug` GitHub issues, fixed, regression-checked, and closed by QA.
