# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

This repository includes the complete source project in [`fieldnote-atlas-source.zip`](fieldnote-atlas-source.zip) and a readable consolidation of all project Markdown files in [`PROJECT-DOCUMENTATION.md`](PROJECT-DOCUMENTATION.md). The archive preserves the project directory structure.

## Run locally

1. Download and unzip `fieldnote-atlas-source.zip`.
2. In the extracted `fieldnote-atlas` folder, run `python3 server.py`.
3. Open `http://127.0.0.1:8091/` for mock-service mode or `http://127.0.0.1:8091/?api=1` for the SQLite API-backed UI.

The default runnable server uses Python's standard library and SQLite DB-API. The optional FastAPI + SQLAlchemy backend is in `backend/app/`; install `backend/requirements.txt` to run it.

## Project status

The project follows the staged mock frontend → OpenAPI contract → in-memory backend → SQLAlchemy/SQLite → integrated UI workflow. The GitHub issue tracker has 14 closed `mvp` issues and one closed `user-test-bug` issue. QA evidence, role guides, test guidance, the brainstorm transcript, and the process notes are included in the source archive and combined documentation file. `docs/qa-results.md` records automated and manual checks.
