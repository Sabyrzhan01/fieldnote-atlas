# GitHub issue backlog

Labels `mvp`, `post-mvp`, and `user-test-bug` exist in [the project repository](https://github.com/Sabyrzhan01/fieldnote-atlas). The 14 groomed issue bodies are in `issues/mvp/`; they have been adapted into the GitHub backlog. All 14 MVP issues and the one browser-discovered `user-test-bug` issue are QA-commented and closed. GitHub Issues are canonical for current status. The import script is for a fresh fork only; do not run it against the existing repository, where it would create duplicates.

## MVP
1. **Bootstrap app shell and passing checks** — Goal: runnable frontend/backend project skeleton. AC: production build succeeds; backend health endpoint succeeds; root instructions work.
2. **Build editorial atlas shell** — Goal: show workspace navigation, collection header, map, and evidence panel. AC: selected collection and note are visible at desktop width; loading/empty state is understandable.
3. **Add fictional seeded collections and observations** — Goal: demo has representative evidence. AC: multiple note types, places, tags, sources, dates, and linked note render.
4. **Select map observations** — Goal: map selection drives evidence detail. AC: selecting each pin updates selected styling and detail; selected state survives filter reset when possible.
5. **Search observations** — Goal: find evidence by title, body, or tag. AC: case-insensitive search; empty state; clearing restores results.
6. **Filter by all/starred/interview** — Goal: narrow the visible research set. AC: filter selection is visible; counts and pins update; zero matches handled.
7. **Create a field note** — Goal: add a useful observation. AC: title/body required; place and tags optional; successful note appears in atlas; validation is visible.
8. **Star observations** — Goal: mark evidence for later synthesis. AC: toggle visible and persists across reload.
9. **Define OpenAPI contract** — Goal: document every frontend backend operation. AC: valid OpenAPI 3 spec describes paths, schemas, errors, and responses; HTTP client matches it.
10. **Implement in-memory API** — Goal: satisfy frontend service contract without DB. AC: health/list/create/star routes work; validation and not-found cases documented and tested.
11. **Connect frontend to API** — Goal: operate the UI through the in-memory backend. AC: API mode selectable/configured; CORS works; main browsing and creation journeys pass.
12. **Persist repositories with SQLAlchemy and SQLite** — Goal: state survives process restart. AC: repository interface preserved; schema initialized; create/star persists; temp DB test passes.
13. **Integrate persisted API** — Goal: app defaults to SQLite-backed API. AC: browser create/star survives backend restart; seed is idempotent; error states visible.
14. **Run independent QA and close MVP** — Goal: evidence-based acceptance. AC: build/backend checks pass; manual walkthrough recorded; all MVP issues have QA PASS comments and are closed by QA.

## Post-MVP
- Add place geocoding and real map tiles with attribution.
- Add edit/delete and undo for observations.
- Add explicit relationship creation and collection management.
- Add CSV/Markdown export and richer source attachments.
- Add mobile layout and keyboard navigation.
- Add optional multi-researcher sharing and permissions.

## User-test bug procedure
Create a new `user-test-bug` issue only after a real manual test finds a defect. Include **Goal** and **Description**, steps, expected/actual behavior, and browser. PM grooms; QA adds regression cases; QA closes only after retest PASS.
