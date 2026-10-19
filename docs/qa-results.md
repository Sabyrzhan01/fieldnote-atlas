# QA evidence

## Environment
- Chrome in-app browser on localhost, 2026-10-20.
- Python 3.14 virtual environment; FastAPI + SQLAlchemy default backend and SQLite database `fieldnote-atlas.sqlite3`.

## Automated checks
- `node --check app.js` — PASS.
- Ruby standard-library YAML parser loaded `openapi.yaml` and verified five API paths — PASS.
- `python3 -m compileall -q backend server.py` — PASS.
- `.venv/bin/python -m unittest discover -s backend/tests -v` — PASS, 7 tests, including collection-scoped creation, counts, SQLAlchemy persistence, and deletion.
- `.venv/bin/python` FastAPI TestClient workflow — PASS: in-memory seed, health/atlas, create validation (422), create/star/delete, and missing-ID behavior.
- SQLAlchemy SQLite API workflow across three fresh Python processes — PASS: idempotent seed, create, star, and delete persisted after process restart.
- HTTP/API smoke script — PASS: health/atlas seed, create valid observation (201), reject blank required fields (422), star toggle, close/reopen SQLite DB and verify created row remains, delete row, reject repeated delete (404).
- Browser console — page loaded and rendered with no JS syntax errors after the reported fix.

## Browser walkthrough
- Fresh load displayed all three collections, six fictional seed notes, six map pins, and selected note/source/tags. PASS.
- Search for `noticeboard` reduced results to one matching observation. PASS.
- Starred filter reduced results to the two seeded starred notes. PASS.
- Mock-service create flow added a note with place/tags and it remained after reload. PASS.
- Default route create flow submitted through FastAPI + SQLAlchemy; note appeared in UI and SQLite count increased. The page was reloaded and collection count and note reappeared. PASS.
- SQL API operations were exercised independently for persistence and delete behavior. PASS.

## Bug found and addressed
The first browser load was blank due to an unbalanced parenthesis in `app.js` event binding. Fixed and added `docs/user-test-bugs.md` with Goal, Description, reproduction steps, and regression checks. GitHub issue #2 was created with the `user-test-bug` label, regression-checked in Chrome, and closed by QA with a PASS comment.

## Collection-scope regression (GitHub #16)
- Switched to Quiet infrastructures in Chrome API mode; API and UI list, map, selected detail, hero/sidebar counts matched collection membership. Empty collection showed no stale note. PASS.
- Created “Pipe hum at dusk” from Quiet infrastructures in Chrome API mode; it appeared in that collection only and its count incremented from 0 to 1. PASS.
- Mock service normalizes legacy observations and derives counts from ownership; service scope/create behavior covered in regression guidelines. PASS.
- Unknown collection IDs returned 422 without creating a row in the FastAPI + SQLAlchemy API. PASS.
- `python3 -m compileall -q backend server.py`, Node syntax checks, `node --test frontend/tests/services.test.js` (4/4), and `.venv/bin/python -m unittest discover -s backend/tests -v` (7/7) — PASS.
- Five post-MVP follow-up specifications are in `issues/post-mvp/`. They are explicitly deferred scope, not claims about implemented behavior.
- QA evidence was produced in the same Codex task as implementation; it is not independent-agent QA.

## Fresh-checkout verification (2026-10-20)
- Cloned public `main` into a clean checkout. The documented `backend/requirements.txt` was missing; GitHub issue #22 records the defect and the PM-groomed scope.
- Restored `backend/requirements.txt` and documented virtual-environment setup. Installed dependencies into a Python 3.14 venv.
- `pnpm test` passed: 7 Python repository tests and 4 JavaScript service tests. `pnpm build` passed: Python compile and JavaScript syntax checks.
- FastAPI TestClient passed health, list, create in selected collection, star, delete, repeated-delete 404, and unknown collection 422.
- Isolated SQLite-backed browser walkthrough passed initial render, switching to an empty collection, creating a note in that collection, persistence after reload, starring and star persistence, and search narrowing to one result. Temporary test data and database were removed.
- Server log included a missing `/favicon.ico` response (404); this does not affect core app behavior and is not an MVP criterion.
- Verification was performed by the same development session, not an independent reviewer. The GitHub issue #22 contains this QA PASS and was closed after the fix was committed.
