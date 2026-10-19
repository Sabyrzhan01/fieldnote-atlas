# QA evidence

## Environment
- Chrome in-app browser on localhost, 2026-10-20.
- Python 3.14 standard library server; SQLite database `fieldnote.db`.

## Automated checks
- `node --check app.js` — PASS.
- Ruby standard-library YAML parser loaded `openapi.yaml` and verified five API paths — PASS.
- `python3 -m compileall -q backend server.py` — PASS.
- `python3 -m unittest discover -s backend/tests -v` — PASS, 4 tests.
- `.venv/bin/python` FastAPI TestClient workflow — PASS: in-memory seed, health/atlas, create validation (422), create/star/delete, and missing-ID behavior.
- SQLAlchemy SQLite API workflow across three fresh Python processes — PASS: idempotent seed, create, star, and delete persisted after process restart.
- HTTP/API smoke script — PASS: health/atlas seed, create valid observation (201), reject blank required fields (422), star toggle, close/reopen SQLite DB and verify created row remains, delete row, reject repeated delete (404).
- Browser console — page loaded and rendered with no JS syntax errors after the reported fix.

## Browser walkthrough
- Fresh load displayed all three collections, six fictional seed notes, six map pins, and selected note/source/tags. PASS.
- Search for `noticeboard` reduced results to one matching observation. PASS.
- Starred filter reduced results to the two seeded starred notes. PASS.
- Mock-service create flow added a note with place/tags and it remained after reload. PASS.
- `?api=1` create flow submitted through the real HTTP API; note appeared in UI and SQLite count increased. PASS.
- SQL API operations were exercised independently for persistence and delete behavior. PASS.

## Bug found and addressed
The first browser load was blank due to an unbalanced parenthesis in `app.js` event binding. Fixed and added `docs/user-test-bugs.md` with Goal, Description, reproduction steps, and regression checks. GitHub issue #2 was created with the `user-test-bug` label, regression-checked in Chrome, and closed by QA with a PASS comment.

## Remaining checks
- No automated visual-regression test or formal Playwright suite was added; browser checks above were manual.
- The integrated browser path uses the standard-library SQLite API at `/` with `?api=1`. FastAPI/SQLAlchemy is a separately tested backend API path.
- All 14 `mvp` issues and the `user-test-bug` issue in the GitHub repository were QA-commented and closed after passing checks. No `post-mvp` issue was in scope for the first release.
