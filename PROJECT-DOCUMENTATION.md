# Fieldnote Atlas — project documentation bundle


# Source file: `.github/ISSUE_TEMPLATE/bug_report.md`

---
name: User test bug
about: Record a defect observed while using the running app
labels: user-test-bug
---

## Goal

## Description

## Steps to reproduce
1.

## Expected behavior

## Actual behavior

## Environment

## Regression tests to add


# Source file: `AGENTS.md`

# Fieldnote Atlas

Fieldnote Atlas is a visual field-research workspace for collecting observations, artifacts, interview fragments, and signals, then connecting them to places and each other. Read `docs/spec.md` before changing product behavior.

## Commands
- App: `python3 server.py` (or `npm run dev` if npm is installed)
- Frontend production build: `npm run build`
- Optional FastAPI backend: `cd backend && python3 -m pip install -r requirements.txt && uvicorn app.main:app --reload --port 8091`
- Backend checks: `python3 -m unittest discover -s backend/tests`
- OpenAPI contract: `openapi.yaml`

## Documents
- `docs/process.md` — task lifecycle and iteration stages
- `docs/design-system.md` — visual direction and references for agents
- `docs/testing-guidelines.md` — expected checks and bug workflow
- `docs/task-template.md` — issue grooming template
- `docs/brainstorming.md` — idea exploration before implementation
- `docs/team/pm.md`, `software-engineer.md`, `qa-engineer.md` — role instructions

## Working rules
- GitHub Issues are the canonical backlog after repository setup. Use `mvp`, `post-mvp`, and `user-test-bug` labels.
- Groom issues before implementation. Engineer does not close issues. QA checks acceptance criteria and closes passing issues.
- Implement one issue at a time and record QA evidence. Do not claim remote GitHub actions that were not performed.
- Keep frontend network access in `frontend/src/services/`. The mock service and HTTP service implement the same interface.
- Preserve the build sequence in `docs/process.md`: mock frontend, OpenAPI, in-memory backend, SQLite via SQLAlchemy, then frontend/backend integration.
- Do not add secrets or real personal interview data. Seed content is fictional.


# Source file: `README.md`

# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas concept: editorial map-led research archive](docs/design-system.md)

## Run locally

Requirement: Python 3.11+ (no third-party packages are needed for the runnable edition).

```sh
python3 server.py
```

Open `http://127.0.0.1:8091/` for the localStorage mock-service edition. Open `http://127.0.0.1:8091/?api=1` for the frontend connected to the SQLite API. The API can be checked at `/api/health` and `/api/atlas`.

The current runnable API uses Python's SQLite DB-API so it can run offline with the system Python. The earlier FastAPI/SQLAlchemy implementation remains in `backend/app/` as the planned ORM-backed deployment architecture; it requires installing `backend/requirements.txt` when the package registry is available.

Optional frontend convenience commands, if `npm` is available:

```sh
npm run dev
npm test
npm run build
```

`npm run dev` delegates to the same dependency-free Python server. SQLite state is written to `fieldnote.db`; use `FIELDNOTE_DB_PATH` to choose another file.

## Project map
- `frontend/` — React, TypeScript, Vite; mock and API service implementations
- `backend/` — FastAPI; in-memory and SQLAlchemy repository modes
- `openapi.yaml` — frontend/backend contract
- `docs/` — product spec, brainstorm, design brief, test/process guidance, backlog, role briefs

## Workflow
This project follows the staged path in `docs/process.md`: mock-backed frontend → OpenAPI contract → in-memory backend → SQLite through SQLAlchemy → integrated frontend/backend. GitHub Issues become the canonical backlog when the project is connected to a GitHub repo. Create the `mvp`, `post-mvp`, and `user-test-bug` labels and import `docs/issues.md`.

Groomed MVP issue bodies are in `issues/mvp/`. Once signed in and connected to the intended GitHub repo, run `python3 scripts/import_github_issues.py` to create 14 `mvp` issues and the observed `user-test-bug` issue.

## Status
Runnable dependency-free edition is verified in Chrome. API checks passed for seed, create, invalid input, star, SQLite reconnect persistence, delete, and not-found. The browser walkthrough verified first render, search, starred filtering, local mock creation, and SQLite API-backed creation. Python/JS syntax checks and four repository unit tests pass. GitHub Issues have not been created: no Git remote or authenticated GitHub session is available in the current browser. Import `docs/issues.md` after connecting the project repo, then have QA complete and close the backlog.


# Source file: `docs/brainstorming.md`

# Brainstorming record

## Initial brief
Build a non-trivial app idea, different from the student's Part I project, that is worth showing. Avoid habit trackers and to-do lists. Follow AI-native specification and full-stack build workflows: think through product scope, use GitHub Issues, a deliberate visual reference, mock-backed frontend first, OpenAPI contract, in-memory backend, SQLite persistence through an ORM, and then integration. Include Markdown docs and a record of the brainstorming. Run and thoroughly test the app; report actual bugs as `user-test-bug` issues and have PM/QA groom and verify. Close MVP and user-test-bug issues through QA before the deadline.

## Idea exploration
Candidate ideas included a neighborhood soundwalk archive, a personal museum of found objects, an oral-history map, and a field-research atlas. The field-research atlas combines the strongest portfolio demo (map + evidence detail + relationships), has a clear user and workflow, and can grow into a niche research tool rather than another generic productivity list.

## Chosen idea: Fieldnote Atlas
An independent researcher, designer, journalist, urbanist, or student collects field observations, interview fragments, artifacts, and signals. Each item retains its place, date, source, tags, and links to related evidence. A map and reading panel help the researcher spot patterns across locations and visits.

## MVP decisions
- Desktop-first local app; no login or collaboration in MVP.
- Seed with fictional Almaty observations to create a compelling demo without exposing private data.
- Deliver browsing, pin selection, search, basic filters, starring, and adding a field note.
- Use a typed frontend service abstraction; begin with a mock service and move to the agreed HTTP API.
- API backend: FastAPI; persistence: SQLAlchemy + SQLite.
- Visual direction: warm editorial research journal, muted cartography, terracotta pins, serif titles, mono metadata. Inspiration pointers are in `design-system.md`.

## Build workflow
The MVP should follow five inspectable checkpoints: frontend with mock service; OpenAPI generated from/verified against the service boundary; in-memory backend; SQLAlchemy/SQLite repository; frontend connected to persistent backend. GitHub issue backlog is canonical once a repository exists. The local environment currently has no repository remote or GitHub CLI, so external issue creation/closure is not represented as completed.


# Source file: `docs/design-system.md`

# Design direction

## Reference brief for v0 / Lovable / coding agent
Create a quiet, editorial urban fieldwork atlas. Imagine a beautifully typeset research journal opened beside a map: warm off-white paper, delicate rules, dusty terracotta pins, sage map patches, tiny cartographic labels, and restrained dark ink. The interface should have hierarchy and whitespace; avoid generic SaaS gradients, bright blue, oversized cards, rounded-everything, and dashboard KPI clutter. Collection titles use an elegant display serif; operational labels use a precise mono; body copy is human and readable. The map is the hero, with selected evidence in a narrow reading panel. Use hand-composed map geometry and clear markers if live map tiles are unavailable.

## Inspiration references
- Mapbox Studio's restrained cartographic label hierarchy and layered map composition.
- Are.na's calm visual research/archive browsing and modular evidence objects.
- Kinfolk / The New Yorker digital typography: confident editorial serif paired with restrained utility text.
- Fieldnotes Brand notebooks: tactile, durable, practical fieldwork character.

These are visual references only; do not copy brand assets or exact layouts.

## Tokens and behavior
- Canvas `#f6f5f1`, sidebar `#f0efe9`, paper `#fbfaf7`, ink `#2c302b`, muted `#898b82`, rule `#e7e5de`, accent `#cc6949`.
- Typography: DM Sans for controls/body, DM Mono for metadata, Playfair Display for collection and note titles.
- Pins use category color and a selected halo. Labels reveal on hover or selection.
- Give buttons hover/focus states, meaningful accessible labels, visible error feedback, and preserve content when a form validation error occurs.
- Responsive desktop target; make layout usable at 900px. Mobile layout remains a follow-up.


# Source file: `docs/issues.md`

# GitHub issue backlog

Create labels: `mvp` (orange), `post-mvp` (gray), and `user-test-bug` (red). The 14 groomed issue bodies are in `issues/mvp/`. After authenticating `gh` and setting the repo remote, run `python3 scripts/import_github_issues.py` to create the MVP issues and the observed bug issue. GitHub issues are canonical after import.

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


# Source file: `docs/process.md`

# Development process

## Canonical work
GitHub Issues are the canonical backlog after a GitHub remote is configured. Every MVP issue must be groomed, implemented, independently checked against acceptance criteria, and closed by QA only after PASS. Labels: `mvp`, `post-mvp`, and `user-test-bug`.

## Staged implementation
1. **Frontend + mockService:** Build and inspect the full interactive UI with seeded local mock data. No backend dependency.
2. **OpenAPI:** Describe the frontend service contract in root `openapi.yaml`; treat it as the shared boundary.
3. **In-memory backend:** Implement that contract with FastAPI and an in-memory repository; connect the frontend and validate the contract.
4. **SQLite persistence:** Replace the repository implementation with SQLAlchemy models and SQLite, keeping routes and response shapes stable.
5. **Integrated QA:** Run backend checks, production build, and browser walkthrough against the real backend. Record steps and results.

## Roles
- PM grooms each issue using `docs/team/pm.md` before implementation.
- Engineer implements one groomed issue using `docs/team/software-engineer.md`; never closes it.
- QA checks the running result against acceptance criteria using `docs/team/qa-engineer.md`, posts PASS/FAIL evidence, and closes a passing issue.

## Bug loop
When a bug is found during hands-on app use, create a GitHub issue labeled `user-test-bug` with a **Goal** and **Description**, reproduction steps, observed/expected behavior, and environment. PM grooms it; QA adds the missing regression cases to `docs/testing-guidelines.md` and the relevant test suite. Fix, repeat the same user journey, post QA verdict, then close. Do not invent user-test bugs when none were observed.

## Git discipline
Commit at meaningful milestones. Keep all Markdown project artifacts in the repository. Do not mark an issue done until the corresponding code/docs are committed and QA has checked it.


# Source file: `docs/qa-results.md`

# QA evidence

## Environment
- Chrome in-app browser on localhost, 2026-10-20.
- Python 3.14 standard library server; SQLite database `fieldnote.db`.

## Automated checks
- `node --check app.js` — PASS.
- Ruby standard-library YAML parser loaded `openapi.yaml` and verified five API paths — PASS.
- `python3 -m compileall -q backend server.py` — PASS.
- `python3 -m unittest discover -s backend/tests -v` — PASS, 4 tests.
- HTTP/API smoke script — PASS: health/atlas seed, create valid observation (201), reject blank required fields (422), star toggle, close/reopen SQLite DB and verify created row remains, delete row, reject repeated delete (404).
- Browser console — page loaded and rendered with no JS syntax errors after the reported fix.

## Browser walkthrough
- Fresh load displayed all three collections, six fictional seed notes, six map pins, and selected note/source/tags. PASS.
- Search for `noticeboard` reduced results to one matching observation. PASS.
- Starred filter reduced results to the two seeded starred notes. PASS.
- Mock-service create flow added a note with place/tags and it remained after reload. PASS.
- `?api=1` create flow submitted through the real HTTP API; note appeared in UI and SQLite count increased. PASS.
- SQL API operations were exercised independently for persistence and delete behavior. PASS.

## Bug found and addressed
The first browser load was blank due to an unbalanced parenthesis in `app.js` event binding. Fixed and added `docs/user-test-bugs.md` as the required `user-test-bug` issue draft with Goal, Description, reproduction steps, and regression checks. GitHub issue creation/QA closure could not be completed because no repo/remote or signed-in GitHub account was available.

## Remaining checks
- No automated visual-regression test or formal Playwright suite was added; browser checks above were manual.
- FastAPI + SQLAlchemy code path is included but not run because external Python dependencies could not be downloaded. The runnable default API uses standard-library SQLite DB-API. The integrated working route is `/` with `?api=1`.
- GitHub labels, issues, QA comments and issue closure remain to be done after repository/account access is available.


# Source file: `docs/spec.md`

# Product specification — Fieldnote Atlas

## Idea and audience
Fieldnote Atlas is a desktop-first, visual field-research archive for independent researchers, designers, journalists, urbanists, and students. It makes qualitative evidence explorable by connecting an observation to a place, source, tags, and related observations. This project is intentionally distinct from the common tracker/task-manager app: its main object is evidence and its main interaction is spatial exploration.

## User problem
Field research is often scattered across camera rolls, notebooks, transcripts, and map pins. Researchers lose the context that makes a fragment useful: where it came from, what it relates to, and what patterns emerge across visits. The app provides one browsable atlas that preserves that context.

## MVP workflows
1. Browse a seeded research collection and its observation pins on a map.
2. Select a pin to read its observation, source, tags, and a related observation.
3. Search observation titles, body text, and tags; filter all notes, starred notes, and interviews.
4. Add a field note with a title, body, place, and comma-separated tags.
5. Star/unstar an observation and retain changes locally/backend.
6. Run as a local web app with persistent SQLite storage after the staged integration is complete.

## Data model
- Collection: id, title, subtitle, color, created_at.
- Observation: id, collection_id, title, body, kind (`field_note`, `interview`, `artifact`, `signal`), place, region, latitude, longitude, observed_at, source, tags, starred, created_at.
- Connection: id, source_observation_id, target_observation_id, relationship label.

## Product constraints
- No account/authentication, cloud sync, real-time collaboration, AI-generated conclusions, or media upload in MVP.
- Seeded map and interview content is fictional; do not imply precise live GIS data. The initial map is a visual local prototype.
- Keep data access behind a typed service interface.
- Target modern desktop browsers at 900px width and above; smaller viewport adaptation is post-MVP.

## Design intent
An editorial research atlas: warm paper surfaces, muted botanical map tones, terracotta observation marks, serif collection titles, and compact mono labels. The map and evidence panel should feel like a considered field journal, not a generic admin dashboard. See `docs/design-system.md`.

## Success criteria
- A first-time user can identify the active collection, select a note, and understand its source and place without instruction.
- Search/filter visibly narrows the evidence set.
- Creating and starring observations survives app reload after SQLite integration.
- Frontend/API contract matches `openapi.yaml`; backend tests and a human browser walkthrough pass.


# Source file: `docs/task-template.md`

## Goal
One or two sentences describing what must be true when this is done.

## Acceptance criteria
- [ ] Checkable behavior/result

## Out of scope
- Explicitly excluded work or a link to a follow-up issue

## Constraints
- Relevant files, architecture, libraries, and linked project docs


# Source file: `docs/team/pm.md`

# Product manager

Groom one issue before implementation. Read its original text, `docs/spec.md`, `docs/process.md`, and `docs/task-template.md`. Rewrite the issue with Goal, checkable Acceptance criteria, Out of scope, and Constraints. Include awkward cases, relevant docs, and a realistic verification expectation. Move excluded work to a linked follow-up issue instead of silently dropping it. Do not write code. Definition of done: a new engineer can implement the issue without clarification and QA can verify each criterion from the running result.


# Source file: `docs/team/qa-engineer.md`

# QA engineer

Independently verify finished work against the issue's acceptance criteria and `docs/testing-guidelines.md`. Inspect and run the app; do not trust implementation claims. Add test cases for missed acceptance edges and, for user-test bugs, update the regression suite. Do not fix implementation code. Post an issue comment headed `## QA: PASS` or `## QA: FAIL`, with a verdict per criterion, exact test command and result, and manual walkthrough evidence. On FAIL, leave the issue open. On PASS, close the issue and explain closure in the comment. Do not claim browser or remote checks you did not perform.


# Source file: `docs/team/software-engineer.md`

# Software engineer

Implement one groomed issue at a time. Read all linked docs and acceptance criteria first. Follow `docs/process.md`'s staged architecture, keep frontend calls in the service layer, and use SQLAlchemy for persistence so storage can change without route/UI changes. Add or update focused tests. Run relevant checks and report exact commands/results. Commit the work, but do not close the issue. If requirements conflict or cannot be met, explain that on the issue before changing scope.


# Source file: `docs/testing-guidelines.md`

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


# Source file: `docs/user-test-bugs.md`

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
PASS after fix. `node --check app.js` passed; browser loaded the seeded atlas, displayed six seed observations, and created a seventh observation with place/tags. The issue is ready to be imported and closed by QA in GitHub; no GitHub issue could be created in this environment because no repository or authenticated GitHub integration is available.


# Source file: `issues/mvp/01-bootstrap-runnable-project.md`

## Goal
A student can start the application and run repeatable checks.

## Acceptance criteria
- [ ] `python3 server.py` starts the local site at `http://127.0.0.1:8091/`.
- [ ] `python3 -m unittest discover -s backend/tests -v` exits successfully.
- [ ] `python3 -m compileall -q backend server.py` exits successfully.

## Out of scope
- Do not add a framework dependency to the offline runnable path.

## Constraints
- Root scripts, README, and tests.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/02-editorial-atlas-shell.md`

## Goal
A visitor can understand the active research collection and navigate the main workspace.

## Acceptance criteria
- [ ] Sidebar shows workspace and three collections.
- [ ] Header identifies active collection and private status.
- [ ] Atlas, timeline, and all-notes navigation are visible.
- [ ] At widths ≥900px, map and selected-note panel are both visible.

## Out of scope
- Timeline interaction and account management.

## Constraints
- Follow `docs/design-system.md`; keep fictional Almaty demo data.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/03-seeded-observations.md`

## Goal
The demo contains varied, contextualized qualitative evidence.

## Acceptance criteria
- [ ] At least six observations cover all four kinds.
- [ ] Each has title, body, place, date, source, color, and tags.
- [ ] Seed data is fictional and does not claim live-map precision.

## Out of scope
- User import and uploaded media.

## Constraints
- Use one shared seed dataset and do not add personal interview data.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/04-map-selection.md`

## Goal
Selecting a map pin opens the matching observation detail.

## Acceptance criteria
- [ ] Each pin is keyboard/click selectable.
- [ ] Selected pin has visible emphasis.
- [ ] Detail title, kind, date, place, body, tags, and source match selected pin.
- [ ] Selecting a pin from filtered results remains valid.

## Out of scope
- Real geocoding and third-party map tiles.

## Constraints
- Keep map UI independent from evidence-detail rendering.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/05-search-evidence.md`

## Goal
A researcher can find notes by title, body, or tags.

## Acceptance criteria
- [ ] Search is case-insensitive.
- [ ] Matching title/body/tag appears in results.
- [ ] Nonmatching pins/cards are removed.
- [ ] Clearing search restores the selected collection.
- [ ] Empty results show a useful empty state.

## Out of scope
- Semantic search and AI summaries.

## Constraints
- Search must not mutate source note content.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/06-filter-evidence.md`

## Goal
A researcher can switch between all, starred, and interview notes.

## Acceptance criteria
- [ ] Current filter is visible.
- [ ] Starred filter contains only starred notes.
- [ ] Interview filter contains only interviews.
- [ ] Map pins and result count match the filter.
- [ ] Changing filter with zero matches is handled.

## Out of scope
- Custom saved filters.

## Constraints
- Use same result set for map and detail selection.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/07-create-fieldnote.md`

## Goal
A researcher can add a contextual field note.

## Acceptance criteria
- [ ] Title and body are required with 120/1000 character maximums.
- [ ] Place and comma-separated tags are optional.
- [ ] Invalid submission keeps entered text and identifies missing fields.
- [ ] Successful submission appears selected with provided fields.
- [ ] API mode writes the note to SQLite.

## Out of scope
- Edit/delete, image upload, and non-fieldnote creation.

## Constraints
- Keep client calls in the service layer; API validates inputs.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/08-star-observations.md`

## Goal
A researcher can mark notes and retain that choice.

## Acceptance criteria
- [ ] Star button describes its action accessibly.
- [ ] Click toggles state and gives visible feedback.
- [ ] Mock mode state survives browser reload.
- [ ] API mode state survives reload and server restart.

## Out of scope
- Shared-user favorites.

## Constraints
- Use one service interface for mock and API implementations.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/09-openapi-contract.md`

## Goal
Frontend and backend share a clear, verifiable contract.

## Acceptance criteria
- [ ] OpenAPI 3 document describes health, atlas, create, star, delete paths.
- [ ] Request/response schemas include required fields and bounds.
- [ ] 400/404/422 behavior is documented.
- [ ] Contract matches actual route behavior.

## Out of scope
- Authentication and collaborative transport.

## Constraints
- Keep root `openapi.yaml` canonical.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/10-in-memory-api.md`

## Goal
The API contract works without persistent storage for rapid integration.

## Acceptance criteria
- [ ] Health and atlas return documented response shapes.
- [ ] Create validates and returns created note.
- [ ] Star toggles existing note.
- [ ] Missing IDs return 404.
- [ ] Memory repository can be replaced without changing route contract.

## Out of scope
- SQLite and authentication.

## Constraints
- Keep storage behind a repository boundary.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/11-connect-frontend-api.md`

## Goal
The same UI can use the HTTP API while mock mode remains usable.

## Acceptance criteria
- [ ] Default mode uses mock service.
- [ ] `?api=1` fetches atlas from API.
- [ ] Creating a note in API mode posts to backend and updates UI.
- [ ] Star in API mode persists server-side.
- [ ] API failure shows visible feedback.

## Out of scope
- Multiuser sync and offline queue.

## Constraints
- No backend calls outside frontend service/data boundary.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/12-sqlite-repository.md`

## Goal
Observations persist in a relational database after process restart.

## Acceptance criteria
- [ ] SQLite tables store collections and observations.
- [ ] Seed runs once and does not duplicate rows.
- [ ] Create/star/delete operations persist after a new connection.
- [ ] Repository boundary is independent of backend DBMS.
- [ ] Use SQLAlchemy implementation when dependencies are available; standard-library SQLite supports offline run.

## Out of scope
- Cloud database and migrations service.

## Constraints
- Document the tested DB path and ORM path separately.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/13-integrated-walkthrough.md`

## Goal
A researcher can complete a full end-to-end workflow with persistence.

## Acceptance criteria
- [ ] Start server with clean database and load app in API mode.
- [ ] Search and select seeded evidence.
- [ ] Create note, reload page, and confirm it remains.
- [ ] Toggle star, restart server, and confirm state remains.
- [ ] Document exact commands and results in `docs/qa-results.md`.

## Out of scope
- Deployment and browser support beyond Chrome.

## Constraints
- Use `docs/testing-guidelines.md`.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.


# Source file: `issues/mvp/14-independent-qa-close.md`

## Goal
MVP issues close only after QA evidence supports each criterion.

## Acceptance criteria
- [ ] QA posts PASS/FAIL against every acceptance criterion.
- [ ] Automated checks and manual journey are recorded.
- [ ] Found user-test defects get `user-test-bug` issue and regression case.
- [ ] QA closes only passing MVP and user-test-bug issues.

## Out of scope
- Closing issues based only on engineer claims.

## Constraints
- Follow `docs/team/qa-engineer.md`; do not fabricate remote issue status.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
