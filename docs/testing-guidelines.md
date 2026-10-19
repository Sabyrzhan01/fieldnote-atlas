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
9. Switch among all collections; verify each note list, map pins, hero count, and sidebar count only include that collection. Empty collections show a clear empty state and no stale selected observation.
10. Search and apply Starred/Interviews filters after switching collections; results must remain scoped to the active collection.
11. Create a note from each collection in mock and API modes; verify `collection_id`, counts, visibility after reload, and persistence in that same collection.
12. Submit an observation for an unknown collection through each API backend; expect 422 and no inserted row.

## User-test bugs
For each bug seen in a real manual run, create a `user-test-bug` issue with Goal, Description, exact steps, actual/expected result, and browser. PM grooms it. Add a failing regression case before fixing. QA repeats the original steps and the regression test, posts evidence, and closes only on PASS. Never fabricate test evidence or bug reports.
