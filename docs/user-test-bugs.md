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
