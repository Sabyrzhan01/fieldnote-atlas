# E2E Test: Star and Unstar Observations

**Labels:** `e2e-test`

## Goal
Verify toggling the starred status of an observation, toast notifications, and persistence using Playwright.

## Description
Ensure researchers can favorite / star evidence for synthesis:
- Clicking `#star` on an unstarred observation updates icon from hollow heart (`♡`) to filled heart (`♥`) and sets `aria-label="Unstar observation"`.
- Displays toast: "Added to starred observations".
- Clicking `#star` again toggles back to hollow heart and displays "Removed from starred observations".
- Reloading the page confirms the star status was persisted in the backend database.

## Playwright Test
- Spec: `tests/e2e/test_06_star_observation.py`
- Test: `test_toggle_star_observation_and_toast`

## Acceptance Criteria
- [x] `#star` toggles between starred and unstarred visually and semantically.
- [x] Toast notifications confirm state change.
- [x] Star state persists across browser page reloads.
- [x] Playwright test passes headlessly across runs.
