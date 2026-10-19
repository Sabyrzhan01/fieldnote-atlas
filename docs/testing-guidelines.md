# Testing guidelines

## Automated checks
- `npm run build` must complete with no TypeScript or bundler errors.
- Test service behavior for creating observations, starring/un-starring, deletion, and persistence across reload.
- Backend tests cover each OpenAPI route, validation errors, not-found behavior, and repository persistence.
- SQLite persistence test uses a temporary database and verifies data after repository reinitialization.

## Browser walkthrough
1. Open the app and confirm a seeded collection, map, pins, selected observation, source, tags, and connection render.
2. Select a different pin; confirm note content and selected pin update.
3. Search a unique title/tag and verify unrelated notes disappear; clear search.
4. Cycle filters and confirm starred/interview results.
5. Star a note, reload, and confirm it remains starred.
6. Submit the add-note form with valid data; confirm it appears in list/map; reload and confirm persistence.
7. Submit with a missing required title/body; confirm the browser blocks submission and preserves entered text.
8. Run against API mode and confirm create/read/star survive backend restart once SQLite stage is complete.

## User-test bugs
For each bug seen in a real manual run, create a `user-test-bug` issue with Goal, Description, exact steps, actual/expected result, and browser. PM grooms it. Add a failing regression case before fixing. QA repeats the original steps and the regression test, posts evidence, and closes only on PASS. Never fabricate test evidence or bug reports.
