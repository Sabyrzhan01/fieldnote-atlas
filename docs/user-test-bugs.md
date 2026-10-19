# User-test bug report (GitHub issue draft)

**Label:** `user-test-bug`

## Goal
The first page load must execute the app script and render the seeded atlas without a blank page.

## Description
During the first real browser run, the page displayed blank because an unbalanced parenthesis in the event-binding function caused a JavaScript syntax error. The issue was found in Chrome, fixed by restructuring message binding, and rechecked by loading the page and exercising the add-observation journey.

## Reproduction
1. Start the local app.
2. Open the home page in a fresh browser tab.
3. Observe the page.

**Expected:** collection list, map pins, selected observation, and action controls render.
**Actual before fix:** blank page; browser console reported a syntax error.
**Environment:** Chrome in Codex in-app browser, local app.

## Regression checks
- Run `node --check app.js` (must pass).
- Open the page and confirm the seeded map and observation detail render.
- Open Add observation, create a note, and verify it appears in the map and detail panel.

## QA result
PASS after fix. `node --check app.js` passed; browser loaded the seeded atlas, displayed six seed observations, and created a seventh observation with place/tags. GitHub issue #2 in `Sabyrzhan01/fieldnote-atlas` uses the `user-test-bug` label, includes the reproduction and regression checks, and was closed with a QA PASS comment after verification.


## Bug 2 — collection switch showed stale observations and counts

**GitHub:** #16 (`user-test-bug`)

**Goal:** Switching collections scopes the archive, map, counts, search, filters, and new observations to the active collection.

**Description:** During the Chrome API-mode run, Quiet infrastructures reported zero observations in the API but continued to display all six notes from The city after rain; the sidebar also showed a hard-coded count.

**Reproduction:** Start the app in API mode with the SQLite seed; select Quiet infrastructures. Expected: zero observations, no stale detail or pins, and accurate count. Actual before fix: six stale observations and an incorrect count.

**Fix:** Scope the live UI and React frontend by `collection_id`, compute counts from scoped observations, clear selection when switching, and preserve the selected collection when creating notes in mock, FastAPI, and standard-library SQLite backends. Reject unknown collection IDs.

**Regression:** See `docs/testing-guidelines.md` cases 9–12; automated repository and route tests plus manual Chrome API and mock walkthrough passed. GitHub issue #16 was closed by QA after PASS evidence.
