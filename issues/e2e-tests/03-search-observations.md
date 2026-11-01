# E2E Test: Real-Time Observation Search

**Labels:** `e2e-test`

## Goal
Verify real-time case-insensitive search across observation titles, bodies, and tags using Playwright.

## Description
Ensure search behaves smoothly:
- Typing keywords into `#search` filters observations on both the map and the evidence list.
- Search matches by title text (e.g. "puddles"), body description (e.g. "asphalt"), and tag keyword (e.g. "transit").
- Observation count counter updates in real time.
- If no results match, an empty state is shown in the detail panel.
- Clearing the search input immediately restores all observations.

## Playwright Test
- Spec: `tests/e2e/test_03_search_observations.py`
- Test: `test_search_observations_by_title_body_and_tags`

## Acceptance Criteria
- [x] Case-insensitive title, body, and tag searches filter map pins correctly.
- [x] Map count updates to reflect matching subset.
- [x] Empty search state handles non-matching queries gracefully.
- [x] Clearing search input restores full observation list.
- [x] Playwright test passes headlessly across runs.
