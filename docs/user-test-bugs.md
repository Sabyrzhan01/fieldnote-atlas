# User-test bug reports

**Label:** `user-test-bug`

## Bug 1 — blank page on first load
**GitHub:** #2 (closed after QA PASS)

**Goal:** The first page load must execute the app script and render the seeded atlas without a blank page.

**Description:** During the first real browser run, an unbalanced parenthesis in the event-binding function caused a JavaScript syntax error and a blank page. The issue was fixed and rechecked in Chrome.

**Reproduction:** Start the local app, open the home page in a fresh browser tab, and observe the page. Expected: collection list, map pins, selected observation, and controls render. Actual before fix: blank page; browser console reported a syntax error.

**Regression:** `node --check app.js`; load the seeded atlas; add an observation and verify it appears on the map and in detail. PASS.

## Bug 2 — collection switch showed stale observations and counts
**GitHub:** #16 (closed after QA PASS)

**Goal:** Switching collections scopes the archive, map, counts, search, filters, and new observations to the active collection.

**Description:** During Chrome API-mode testing, Quiet infrastructures reported zero observations in the API but continued to display six notes from The city after rain; the sidebar count was hard-coded.

**Reproduction:** Start the app in API mode and select Quiet infrastructures. Expected: zero observations, no stale detail or pins, and accurate count. Actual before fix: six stale observations and an incorrect count.

**Fix:** Scope the UI by `collection_id`, derive counts from collection membership, clear selection when switching, preserve selected collection on create, and reject unknown collection IDs.

**Regression:** See `docs/testing-guidelines.md` cases 9–12; automated repository and route tests plus manual Chrome API and mock walkthrough passed.

## Bug 3 — clean checkout could not install Python dependencies
**GitHub:** #22 (`user-test-bug`, QA PASS; closed after the fix and docs were committed)

**Goal:** A new contributor can install dependencies and run the app from a clean clone using the README steps.

**Description:** README referenced `backend/requirements.txt`, but the file was missing from `main`. This blocked setup before the server could start.

**Fix:** Added a dependency manifest for FastAPI, SQLAlchemy, Uvicorn, and HTTPX; updated README to create and activate a virtual environment.

**Regression:** Created a fresh Python 3.14 virtual environment, installed the manifest, ran 7 backend and 4 frontend service tests, ran build/syntax checks, and verified API health plus create/star/delete/validation in TestClient. All passed. The GitHub issue includes PM-groomed scope, acceptance criteria, QA regression cases, and QA PASS evidence. This was the same development session, not an independent QA review.
