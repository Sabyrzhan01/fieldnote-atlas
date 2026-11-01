# E2E Test: Connected Evidence Navigation

**Labels:** `e2e-test`

## Goal
Verify connected observation hyperlinks allow seamless jumping between related research artifacts using Playwright.

## Description
Ensure researchers can follow threads of evidence:
- When viewing observation 1 ("A city measured in puddles"), a "CONNECTED TO" section shows the linked note "“We wait for the second bus”".
- Clicking `#connected` shifts active selection to the linked observation.
- The map highlights the linked pin and the detail reader shows its contents.

## Playwright Test
- Spec: `tests/e2e/test_08_connected_observations.py`
- Test: `test_connected_observation_link_navigation`

## Acceptance Criteria
- [x] Connected observation widget renders with title and type metadata.
- [x] Clicking connection link selects the linked note.
- [x] Map active pin updates to the connected observation.
- [x] Playwright test passes headlessly across runs.
