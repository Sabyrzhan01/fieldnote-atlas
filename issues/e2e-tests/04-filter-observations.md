# E2E Test: Filter Cycling (All Notes, Starred, Interviews)

**Labels:** `e2e-test`

## Goal
Verify the observation filter cycle button switches between All notes, Starred, and Interviews using Playwright.

## Description
Ensure that clicking the filter toggle:
- Transitions filter state in sequential order: "All notes" -> "Starred" -> "Interviews" -> "All notes".
- When "Starred" is active, only starred observations (notes 1 and 3 in seed) render on map and in detail.
- When "Interviews" is active, only interview notes (notes 2 and 6) render.
- Pin counts and map footer accurately reflect the active filter mode.

## Playwright Test
- Spec: `tests/e2e/test_04_filter_observations.py`
- Test: `test_filter_observations_all_starred_and_interviews`

## Acceptance Criteria
- [x] `#filter` displays active filter mode label.
- [x] Filtering to "Starred" displays only starred observations.
- [x] Filtering to "Interviews" displays only interview-kind observations.
- [x] Cycling back to "All notes" restores the complete set.
- [x] Playwright test passes headlessly across runs.
