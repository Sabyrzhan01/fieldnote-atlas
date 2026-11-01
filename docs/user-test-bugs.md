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

## Bug 4 — POST /api/observations accepted payloads violating OpenAPI constraints
**GitHub:** #31 (`user-test-bug`, closed after QA PASS)

**Goal:** Make `POST /api/observations` enforce the documented OpenAPI constraints (`kind` enum, `x`/`y` within `0..100`, tag length `<= 40`, and non-whitespace `title`/`body`) with HTTP 422.

**Description:** `ObservationInput` in `backend/app/schemas.py` used plain `str` / `float` without bounds or whitespace stripping, allowing invalid `kind`, out-of-range coordinates, 41-char tags, and whitespace-only strings to return 201.

**Fix:** Updated `ObservationInput` in `backend/app/schemas.py` with `Literal['Field note', 'Interview', 'Artifact', 'Signal']`, `Field(ge=0, le=100)` on `x`/`y`, `StringConstraints(max_length=40)` on tags, and `StringConstraints(strip_whitespace=True, min_length=1, ...)` on `title` and `body`.

**Regression:** Added `test_openapi_observation_input_validation_rejects_invalid_payloads` in `backend/tests/test_repository.py` asserting all 8 invalid mutations return HTTP 422 while valid payloads return 201. PASS.

## Bug 5 — Selected observation tag chips overlapped in detail panel
**GitHub:** #32 (`user-test-bug`, closed after QA PASS)

**Goal:** Show each selected observation tag (`button[data-tag]`) as a readable, separately clickable chip with no horizontal overlap.

**Description:** `.tags button` in `style.css` applied `width: 22px` (intended only for `#addTag`) to all `<button data-tag="...">` tag chips, causing `#rain`, `#movement`, and `#informal paths` to overflow and overlap.

**Fix:** Scoped the `22px` dashed style to `.tags #addTag` and applied `.tags button[data-tag]` pill styling (`width: auto; white-space: nowrap; padding: 5px 7px; background: #f0efe9`).

**Regression:** Added bounding-box non-overlap assertion in `tests/e2e/test_07_tag_navigation.py` verifying `movement_box["x"] >= rain_box["x"] + rain_box["width"]` in headless Chromium. PASS.
