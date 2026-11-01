# E2E Test: Interactive Map Observation Pin Selection

**Labels:** `e2e-test`

## Goal
Verify map rendering, observation pins placement, pin selection, and detail reader synchronization using Playwright.

## Description
Ensure that when viewing the atlas:
- The Almaty study map renders with base layers, roads, waterways, Panfilov Park, and geographic landmark labels.
- Observation pins appear at their respective coordinate positions with category icons.
- Default observation pin is highlighted with `.pin-active`.
- Clicking another observation pin updates the active pin state and populates the right detail reader with observation title, body, place, date, kind, and tags.

## Playwright Test
- Spec: `tests/e2e/test_02_map_pin_selection.py`
- Test: `test_map_pin_selection_updates_detail_panel`

## Acceptance Criteria
- [x] Map panel displays with caption "ALMATY, KAZAKHSTAN · 43.2383° N, 76.9455° E".
- [x] All 6 seeded observation pins render on the map.
- [x] Clicking a pin updates `.pin-active` class and reflects the note in the detail panel.
- [x] Playwright test passes headlessly across runs.
