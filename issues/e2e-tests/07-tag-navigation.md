# E2E Test: Tag Chip Filtering Navigation

**Labels:** `e2e-test`

## Goal
Verify clicking a tag chip in the detail reader triggers tag-based filtering using Playwright.

## Description
Ensure researcher tags enable fast evidence traversal:
- When an observation with tags is selected, tags render as distinct clickable chips (e.g. `#rain`, `#movement`).
- Clicking a tag chip (e.g. `[data-tag="rain"]`) populates `#search` with the tag name.
- The map and detail reader filter to observations possessing that tag.

## Playwright Test
- Spec: `tests/e2e/test_07_tag_navigation.py`
- Test: `test_clicking_tag_chip_filters_observations`

## Acceptance Criteria
- [x] Tag chips are clickable buttons in the observation detail card.
- [x] Clicking a tag populates `#search` input with tag text.
- [x] Visible pins update to display notes sharing that tag.
- [x] Playwright test passes headlessly across runs.
