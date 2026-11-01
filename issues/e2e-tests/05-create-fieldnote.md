# E2E Test: Create Fieldnote Observation Modal

**Labels:** `e2e-test`

## Goal
Verify the create observation modal flow, form fields, validation, and instantaneous UI/database update using Playwright.

## Description
Ensure researchers can record new observations:
- Clicking `#add` opens the modal dialog with title, observation body, place, and tags inputs.
- Validates required fields (title and body).
- Submitting the form:
  - Closes the modal dialog.
  - Displays a toast confirmation: "Observation added to your atlas".
  - Adds a new pin to the map at random coordinates.
  - Automatically selects the new note and shows its content in the detail reader.
  - Increments collection observation count.
- Clicking "Cancel" or "×" closes modal without creating an observation.

## Playwright Test
- Spec: `tests/e2e/test_05_create_fieldnote.py`
- Test: `test_create_fieldnote_via_modal`, `test_create_fieldnote_modal_cancellation`

## Acceptance Criteria
- [x] Modal appears on `#add` click with correct header and inputs.
- [x] Submitting adds observation to active collection and updates map.
- [x] Detail panel shows new observation with tags and place.
- [x] Modal cancellation discards changes.
- [x] Playwright test passes headlessly across runs.
