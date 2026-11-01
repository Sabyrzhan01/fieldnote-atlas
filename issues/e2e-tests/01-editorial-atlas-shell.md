# E2E Test: Editorial Atlas Shell & Collection Navigation

**Labels:** `e2e-test`

## Goal
Verify the primary workspace layout, editorial atlas header, sidebar, branding, and collection navigation using Playwright.

## Description
Ensure that when a user lands on Fieldnote Atlas:
- The brandmark ("FIELDNOTE ATLAS / STUDIO") and user workspace selector ("Sabyr’s workspace · Personal studio") render correctly.
- All three seeded collections ("The city after rain", "Quiet infrastructures", "Edges of the steppe") are displayed with appropriate color indicators and observation counts.
- Topbar breadcrumb shows collection name with "PRIVATE" pill.
- Clicking a collection updates the active selection and refreshes hero headings and observation counts.

## Playwright Test
- Spec: `tests/e2e/test_01_editorial_atlas_shell.py`
- Test: `test_editorial_atlas_shell_renders_header_sidebar_and_collections`

## Acceptance Criteria
- [x] Brand elements and workspace studio titles are visible.
- [x] Three collections render in sidebar library with observation counts.
- [x] Switching collections switches hero banner and active selection styling.
- [x] Playwright test passes headlessly across runs.
