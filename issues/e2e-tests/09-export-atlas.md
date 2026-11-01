# E2E Test: Export Atlas JSON Archive

**Labels:** `e2e-test`

## Goal
Verify clicking the Export button triggers browser download of `fieldnote-atlas.json` archive using Playwright.

## Description
Ensure researchers can archive and back up their studies:
- Clicking `#export` in the detail reader triggers a file download event.
- Verifies the downloaded file name is `fieldnote-atlas.json`.
- Verifies the downloaded payload contains valid JSON array of observations with required fields (`id`, `title`, `body`, `place`, `tags`).

## Playwright Test
- Spec: `tests/e2e/test_09_export_atlas.py`
- Test: `test_export_atlas_downloads_json_archive`

## Acceptance Criteria
- [x] `#export` button triggers browser download.
- [x] Suggested file name matches `fieldnote-atlas.json`.
- [x] Downloaded file content parses as valid JSON with observation schema.
- [x] Playwright test passes headlessly across runs.
