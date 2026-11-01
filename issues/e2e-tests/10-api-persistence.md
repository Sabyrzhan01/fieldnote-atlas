# E2E Test: Full API & Database Persistence Lifecycle

**Labels:** `e2e-test`

## Goal
Verify complete end-to-end client-server and database persistence lifecycle using Playwright and HTTP API checks.

## Description
Ensure data created in the frontend is persisted into the database and available across process/browser cycles:
- Checks `/api/health` reports status ok.
- Creates an observation via UI modal.
- Directly queries REST API `/api/atlas` to verify database row was inserted.
- Deletes an observation via API `DELETE /api/observations/{id}`.
- Reloads the browser and verifies UI reflects deletion.

## Playwright Test
- Spec: `tests/e2e/test_10_api_persistence.py`
- Test: `test_full_api_and_ui_persistence_lifecycle`

## Acceptance Criteria
- [x] Backend API `/api/health` returns status ok.
- [x] Observations submitted via browser form are verified in REST API response.
- [x] Observation deleted via API is no longer present on UI page reload.
- [x] Playwright test passes headlessly across runs.
