# Fieldnote Atlas — Project Documentation

Consolidated Markdown source from the repository. Individual files remain canonical.


---

<!-- README.md -->

# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas concept: editorial map-led research archive](docs/design-system.md)

## Run locally

Requirement: Python 3.11+ (no third-party packages are needed for the runnable edition).

```sh
python3 server.py
```

Open `http://127.0.0.1:8091/` for the localStorage mock-service edition. Open `http://127.0.0.1:8091/?api=1` for the frontend connected to the SQLite API. The API can be checked at `/api/health` and `/api/atlas`.

The default runnable API uses Python's SQLite DB-API so it can run offline with the system Python. `backend/app/` also contains a FastAPI API with in-memory and SQLAlchemy repository implementations. Install `backend/requirements.txt` to run that ORM-backed path; it has been exercised with FastAPI's test client and a SQLite database.

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
This project follows the staged path in `docs/process.md`: mock-backed frontend → OpenAPI contract → in-memory backend → SQLite through SQLAlchemy → integrated frontend/backend. The GitHub repository is [Sabyrzhan01/fieldnote-atlas](https://github.com/Sabyrzhan01/fieldnote-atlas). It has the `mvp`, `post-mvp`, and `user-test-bug` labels. Groomed MVP issue bodies are in `issues/mvp/`; the GitHub backlog has 14 MVP issues and two user-test-bug issues, each with QA comments and closed after passing checks.

## Status
Runnable dependency-free edition and the optional FastAPI/SQLAlchemy edition are verified. API checks passed for seed, selected-collection create, invalid input, star, SQLite persistence across fresh processes, delete, and not-found. The Chrome walkthrough verified first render, search, starred filtering, local mock creation, SQLite API-backed creation, and collection scoping including the empty state. JavaScript/Python syntax checks, OpenAPI parsing, five repository tests, in-memory API checks, and SQLAlchemy persistence checks pass. Both real browser bugs were recorded as `user-test-bug` GitHub issues, fixed, regression-checked, and closed by QA.


---

<!-- PROJECT-DOCUMENTATION.md -->

# Fieldnote Atlas — Project Documentation

This file combines every Markdown file from the source bundle so the complete documentation is readable in GitHub. The archive preserves the original directory structure.

---

## `.github/ISSUE_TEMPLATE/bug_report.md`

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

---

## `AGENTS.md`

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

---

## `README.md`

# Fieldnote Atlas

**A visual field-research archive for the details that make a place feel like itself.** Collect observations, interview fragments, artifacts, and signals; keep their sources and tags attached; explore the evidence on a map.

![Fieldnote Atlas concept: editorial map-led research archive](docs/design-system.md)

## Run locally

Requirement: Python 3.11+ (no third-party packages are needed for the runnable edition).

```sh
python3 server.py
```

Open `http://127.0.0.1:8091/` for the localStorage mock-service edition. Open `http://127.0.0.1:8091/?api=1` for the frontend connected to the SQLite API. The API can be checked at `/api/health` and `/api/atlas`.

The default runnable API uses Python's SQLite DB-API so it can run offline with the system Python. `backend/app/` also contains a FastAPI API with in-memory and SQLAlchemy repository implementations. Install `backend/requirements.txt` to run that ORM-backed path; it has been exercised with FastAPI's test client and a SQLite database.

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
This project follows the staged path in `docs/process.md`: mock-backed frontend → OpenAPI contract → in-memory backend → SQLite through SQLAlchemy → integrated frontend/backend. The GitHub repository is [Sabyrzhan01/fieldnote-atlas](https://github.com/Sabyrzhan01/fieldnote-atlas). It has the `mvp`, `post-mvp`, and `user-test-bug` labels. Groomed MVP issue bodies are in `issues/mvp/`; the GitHub backlog has 14 MVP issues and one user-test-bug issue, each with QA comments and closed after passing checks.

## Status
Runnable dependency-free edition and the optional FastAPI/SQLAlchemy edition are verified. API checks passed for seed, create, invalid input, star, SQLite persistence across fresh processes, delete, and not-found. The Chrome walkthrough verified first render, search, starred filtering, local mock creation, and SQLite API-backed creation. JavaScript/Python syntax checks, OpenAPI parsing, four repository tests, in-memory API checks, and SQLAlchemy persistence checks pass. The first-load browser bug was recorded as a `user-test-bug` GitHub issue, fixed, regression-checked, and closed by QA.

---

## `docs/brainstorming-chat.md`

# Brainstorming chat record

This file preserves the assignment prompt and the idea-selection notes from before implementation. It is a concise record, not a verbatim export of every assistant turn.

## User's assignment prompt

> Pick a project idea, different from Part I, and come up with a non trivial app (no habit tracker, to-do list, etc). Come up with an idea you will be proud to show off.
>
> If interested in startup and money part, get ideas from: https://trustmrr.com/
>
> Fully follow:
> - https://aishippingblog.com/p/ai-native-development-specifications
> - https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with
>
> I know they start from different places, but think about how can you combine.
> Utilize Github Issues in the first article's workflow. Use non-generic design references (Lovable / v0 / Claude Design) or give the coding agent strong visual references. Close all MVP tags (up to 100 issues is okay). Use SQLite for persistent storage and a DBMS-agnostic ORM. Work in iterations: mock-service frontend → OpenAPI contract → in-memory backend → SQLite storage → connect frontend and backend. Keep Markdown documentation in GitHub and improve it while developing. Save the brainstorming chat as Markdown. Run and thoroughly test the app. If a real user-test bug is found, create a GitHub issue with Goal and Description, ask PM to groom it and QA to add cases, label it `user-test-bug`, then fix and retest. QA should close passing `mvp` and `user-test-bug` issues before the deadline.

## Idea discussion and decision

We considered a neighborhood soundwalk archive, a personal museum of found objects, an oral-history map, and a field-research atlas. The atlas best combined a distinctive map-led portfolio presentation with a meaningful research workflow: a researcher can compare observations, interview excerpts, artifacts, and local signals while keeping each item's place, date, source, and tags attached.

The selected project is **Fieldnote Atlas**: a visual field-research archive seeded with fictional Almaty observations. The first release focuses on browsing and selecting evidence, search, filters, starring, and creating a field note. It does not use live location data or claim real map precision.

The user later supplied `https://github.com/Sabyrzhan01/fieldnote-atlas` as the destination repository and confirmed being signed in. The selected idea should be compared with the student's Part I topic before submission; that topic was not included in the conversation available for this record.

## Follow-up choices

- Visual direction: warm editorial research journal, understated cartography, terracotta markers, serif display type, and monospaced metadata. See `design-system.md` for concrete references and tokens.
- Build loop: mock-backed interactive frontend first, then OpenAPI, in-memory FastAPI, SQLAlchemy/SQLite, and a connected API mode.
- Workflow: groomed GitHub issues with `mvp`, `post-mvp`, and `user-test-bug` labels; PM, engineer, and QA role guides; only QA closes passing MVP/bug issues.
- Startup research was optional in the assignment, so the project stayed focused on the research workflow instead of adding speculative monetization.

---

## `docs/brainstorming.md`

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
The MVP follows five inspectable checkpoints: frontend with mock service; OpenAPI verified against the service boundary; in-memory backend; SQLAlchemy/SQLite repository; frontend connected to persistent backend. The GitHub issue backlog is canonical in `Sabyrzhan01/fieldnote-atlas`; all 14 MVP issues and the real browser-found bug issue have QA PASS comments and are closed.

---

## `docs/design-system.md`

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

---

## `docs/issues.md`

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

---

## `docs/process.md`

# Development process

## Workflow basis
This staged workflow combines the spec-first backlog/PM-engineer-QA loop from [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications) with the mock-service frontend → OpenAPI → in-memory API → SQLite/SQLAlchemy sequence from [Build and Ship a Full-Stack App with AI Coding Assistants](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with). The issue tracker is the current source of task status; the local issue files are the groomed source templates. Design inspiration and component references are recorded in `design-system.md`.

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

---

## `docs/qa-results.md`

# QA evidence

## Environment
- Chrome in-app browser on localhost, 2026-10-20.
- Python 3.14 standard library server; SQLite database `fieldnote.db`.

## Automated checks
- `node --check app.js` — PASS.
- Ruby standard-library YAML parser loaded `openapi.yaml` and verified five API paths — PASS.
- `python3 -m compileall -q backend server.py` — PASS.
- `python3 -m unittest discover -s backend/tests -v` — PASS, 4 tests.
- `.venv/bin/python` FastAPI TestClient workflow — PASS: in-memory seed, health/atlas, create validation (422), create/star/delete, and missing-ID behavior.
- SQLAlchemy SQLite API workflow across three fresh Python processes — PASS: idempotent seed, create, star, and delete persisted after process restart.
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
The first browser load was blank due to an unbalanced parenthesis in `app.js` event binding. Fixed and added `docs/user-test-bugs.md` with Goal, Description, reproduction steps, and regression checks. GitHub issue #2 was created with the `user-test-bug` label, regression-checked in Chrome, and closed by QA with a PASS comment.

## Remaining checks
- No automated visual-regression test or formal Playwright suite was added; browser checks above were manual.
- The integrated browser path uses the standard-library SQLite API at `/` with `?api=1`. FastAPI/SQLAlchemy is a separately tested backend API path.
- All 14 `mvp` issues and the `user-test-bug` issue in the GitHub repository were QA-commented and closed after passing checks. No `post-mvp` issue was in scope for the first release.

---

## `docs/spec.md`

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

---

## `docs/task-template.md`

## Goal
One or two sentences describing what must be true when this is done.

## Acceptance criteria
- [ ] Checkable behavior/result

## Out of scope
- Explicitly excluded work or a link to a follow-up issue

## Constraints
- Relevant files, architecture, libraries, and linked project docs

---

## `docs/team/pm.md`

# Product manager

Groom one issue before implementation. Read its original text, `docs/spec.md`, `docs/process.md`, and `docs/task-template.md`. Rewrite the issue with Goal, checkable Acceptance criteria, Out of scope, and Constraints. Include awkward cases, relevant docs, and a realistic verification expectation. Move excluded work to a linked follow-up issue instead of silently dropping it. Do not write code. Definition of done: a new engineer can implement the issue without clarification and QA can verify each criterion from the running result.

---

## `docs/team/qa-engineer.md`

# QA engineer

Independently verify finished work against the issue's acceptance criteria and `docs/testing-guidelines.md`. Inspect and run the app; do not trust implementation claims. Add test cases for missed acceptance edges and, for user-test bugs, update the regression suite. Do not fix implementation code. Post an issue comment headed `## QA: PASS` or `## QA: FAIL`, with a verdict per criterion, exact test command and result, and manual walkthrough evidence. On FAIL, leave the issue open. On PASS, close the issue and explain closure in the comment. Do not claim browser or remote checks you did not perform.

---

## `docs/team/software-engineer.md`

# Software engineer

Implement one groomed issue at a time. Read all linked docs and acceptance criteria first. Follow `docs/process.md`'s staged architecture, keep frontend calls in the service layer, and use SQLAlchemy for persistence so storage can change without route/UI changes. Add or update focused tests. Run relevant checks and report exact commands/results. Commit the work, but do not close the issue. If requirements conflict or cannot be met, explain that on the issue before changing scope.

---

## `docs/testing-guidelines.md`

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

---

## `docs/user-test-bugs.md`

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

---

## `issues/mvp/01-bootstrap-runnable-project.md`

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

---

## `issues/mvp/02-editorial-atlas-shell.md`

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

---

## `issues/mvp/03-seeded-observations.md`

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

---

## `issues/mvp/04-map-selection.md`

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

---

## `issues/mvp/05-search-evidence.md`

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

---

## `issues/mvp/06-filter-evidence.md`

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

---

## `issues/mvp/07-create-fieldnote.md`

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

---

## `issues/mvp/08-star-observations.md`

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

---

## `issues/mvp/09-openapi-contract.md`

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

---

## `issues/mvp/10-in-memory-api.md`

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

---

## `issues/mvp/11-connect-frontend-api.md`

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

---

## `issues/mvp/12-sqlite-repository.md`

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

---

## `issues/mvp/13-integrated-walkthrough.md`

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

---

## `issues/mvp/14-independent-qa-close.md`

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


---

<!-- AGENTS.md -->

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


---

<!-- docs/process.md -->

# Development process

## Workflow basis
This staged workflow combines the spec-first backlog/PM-engineer-QA loop from [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications) with the mock-service frontend → OpenAPI → in-memory API → SQLite/SQLAlchemy sequence from [Build and Ship a Full-Stack App with AI Coding Assistants](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with). The issue tracker is the current source of task status; the local issue files are the groomed source templates. Design inspiration and component references are recorded in `design-system.md`.

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


---

<!-- docs/testing-guidelines.md -->

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


---

<!-- docs/brainstorming-chat.md -->

# Brainstorming chat record

This file preserves the assignment prompt and the idea-selection notes from before implementation. It is a concise record, not a verbatim export of every assistant turn.

## User's assignment prompt

> Pick a project idea, different from Part I, and come up with a non trivial app (no habit tracker, to-do list, etc). Come up with an idea you will be proud to show off.
>
> If interested in startup and money part, get ideas from: https://trustmrr.com/
>
> Fully follow:
> - https://aishippingblog.com/p/ai-native-development-specifications
> - https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with
>
> I know they start from different places, but think about how can you combine.
> Utilize Github Issues in the first article's workflow. Use non-generic design references (Lovable / v0 / Claude Design) or give the coding agent strong visual references. Close all MVP tags (up to 100 issues is okay). Use SQLite for persistent storage and a DBMS-agnostic ORM. Work in iterations: mock-service frontend → OpenAPI contract → in-memory backend → SQLite storage → connect frontend and backend. Keep Markdown documentation in GitHub and improve it while developing. Save the brainstorming chat as Markdown. Run and thoroughly test the app. If a real user-test bug is found, create a GitHub issue with Goal and Description, ask PM to groom it and QA to add cases, label it `user-test-bug`, then fix and retest. QA should close passing `mvp` and `user-test-bug` issues before the deadline.

## Idea discussion and decision

We considered a neighborhood soundwalk archive, a personal museum of found objects, an oral-history map, and a field-research atlas. The atlas best combined a distinctive map-led portfolio presentation with a meaningful research workflow: a researcher can compare observations, interview excerpts, artifacts, and local signals while keeping each item's place, date, source, and tags attached.

The selected project is **Fieldnote Atlas**: a visual field-research archive seeded with fictional Almaty observations. The first release focuses on browsing and selecting evidence, search, filters, starring, and creating a field note. It does not use live location data or claim real map precision.

The user later supplied `https://github.com/Sabyrzhan01/fieldnote-atlas` as the destination repository and confirmed being signed in. The selected idea should be compared with the student's Part I topic before submission; that topic was not included in the conversation available for this record.

## Follow-up choices

- Visual direction: warm editorial research journal, understated cartography, terracotta markers, serif display type, and monospaced metadata. See `design-system.md` for concrete references and tokens.
- Build loop: mock-backed interactive frontend first, then OpenAPI, in-memory FastAPI, SQLAlchemy/SQLite, and a connected API mode.
- Workflow: groomed GitHub issues with `mvp`, `post-mvp`, and `user-test-bug` labels; PM, engineer, and QA role guides; only QA closes passing MVP/bug issues.
- Startup research was optional in the assignment, so the project stayed focused on the research workflow instead of adding speculative monetization.


---

<!-- docs/brainstorming.md -->

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
The MVP follows five inspectable checkpoints: frontend with mock service; OpenAPI verified against the service boundary; in-memory backend; SQLAlchemy/SQLite repository; frontend connected to persistent backend. The GitHub issue backlog is canonical in `Sabyrzhan01/fieldnote-atlas`; all 14 MVP issues and both real browser-found bug issues have QA PASS comments and are closed.


---

<!-- docs/issues.md -->

# GitHub issue backlog

Labels `mvp`, `post-mvp`, and `user-test-bug` exist in [the project repository](https://github.com/Sabyrzhan01/fieldnote-atlas). The 14 groomed issue bodies are in `issues/mvp/`; they have been adapted into the GitHub backlog. All 14 MVP issues and both browser-discovered `user-test-bug` issues are QA-commented and closed. GitHub Issues are canonical for current status. The import script is for a fresh fork only; do not run it against the existing repository, where it would create duplicates.

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


---

<!-- docs/design-system.md -->

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


---

<!-- docs/task-template.md -->

## Goal
One or two sentences describing what must be true when this is done.

## Acceptance criteria
- [ ] Checkable behavior/result

## Out of scope
- Explicitly excluded work or a link to a follow-up issue

## Constraints
- Relevant files, architecture, libraries, and linked project docs


---

<!-- docs/spec.md -->

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


---

<!-- docs/qa-results.md -->

# QA evidence

## Environment
- Chrome in-app browser on localhost, 2026-10-20.
- Python 3.14 standard library server; SQLite database `fieldnote.db`.

## Automated checks
- `node --check app.js` — PASS.
- Ruby standard-library YAML parser loaded `openapi.yaml` and verified five API paths — PASS.
- `python3 -m compileall -q backend server.py` — PASS.
- `python3 -m unittest discover -s backend/tests -v` — PASS, 5 tests, including collection-scoped creation and counts.
- `.venv/bin/python` FastAPI TestClient workflow — PASS: in-memory seed, health/atlas, create validation (422), create/star/delete, and missing-ID behavior.
- SQLAlchemy SQLite API workflow across three fresh Python processes — PASS: idempotent seed, create, star, and delete persisted after process restart.
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
The first browser load was blank due to an unbalanced parenthesis in `app.js` event binding. Fixed and added `docs/user-test-bugs.md` with Goal, Description, reproduction steps, and regression checks. GitHub issue #2 was created with the `user-test-bug` label, regression-checked in Chrome, and closed by QA with a PASS comment.

## Collection-scope regression (GitHub #16)
- Switched to Quiet infrastructures in Chrome API mode; API and UI list, map, selected detail, hero/sidebar counts matched collection membership. Empty collection showed no stale note. PASS.
- Created “Pipe hum at dusk” from Quiet infrastructures in Chrome API mode; it appeared in that collection only and its count incremented from 0 to 1. PASS.
- Mock service normalizes legacy observations and derives counts from ownership; service scope/create behavior covered in regression guidelines. PASS.
- Unknown collection IDs returned 422 without creating a row in FastAPI and standard-library API paths (the request validation was also checked in FastAPI TestClient). PASS.
- `npm run build`, `python3 -m compileall -q backend server.py`, and `python3 -m unittest discover -s backend/tests -v` — PASS, 5 tests.
- All 14 `mvp` issues and both `user-test-bug` issues were QA-commented and closed after passing checks. No `post-mvp` issue was in scope for the first release.


---

<!-- docs/user-test-bugs.md -->

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


---

<!-- issues/mvp/03-seeded-observations.md -->

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


---

<!-- issues/mvp/04-map-selection.md -->

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


---

<!-- issues/mvp/12-sqlite-repository.md -->

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


---

<!-- issues/mvp/07-create-fieldnote.md -->

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


---

<!-- issues/mvp/02-editorial-atlas-shell.md -->

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


---

<!-- issues/mvp/01-bootstrap-runnable-project.md -->

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


---

<!-- issues/mvp/14-independent-qa-close.md -->

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


---

<!-- issues/mvp/11-connect-frontend-api.md -->

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


---

<!-- issues/mvp/08-star-observations.md -->

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


---

<!-- issues/mvp/09-openapi-contract.md -->

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


---

<!-- issues/mvp/10-in-memory-api.md -->

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


---

<!-- issues/mvp/05-search-evidence.md -->

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


---

<!-- issues/mvp/13-integrated-walkthrough.md -->

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


---

<!-- issues/mvp/06-filter-evidence.md -->

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


---

<!-- .github/ISSUE_TEMPLATE/bug_report.md -->

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


---

<!-- docs/team/qa-engineer.md -->

# QA engineer

Independently verify finished work against the issue's acceptance criteria and `docs/testing-guidelines.md`. Inspect and run the app; do not trust implementation claims. Add test cases for missed acceptance edges and, for user-test bugs, update the regression suite. Do not fix implementation code. Post an issue comment headed `## QA: PASS` or `## QA: FAIL`, with a verdict per criterion, exact test command and result, and manual walkthrough evidence. On FAIL, leave the issue open. On PASS, close the issue and explain closure in the comment. Do not claim browser or remote checks you did not perform.


---

<!-- docs/team/software-engineer.md -->

# Software engineer

Implement one groomed issue at a time. Read all linked docs and acceptance criteria first. Follow `docs/process.md`'s staged architecture, keep frontend calls in the service layer, and use SQLAlchemy for persistence so storage can change without route/UI changes. Add or update focused tests. Run relevant checks and report exact commands/results. Commit the work, but do not close the issue. If requirements conflict or cannot be met, explain that on the issue before changing scope.


---

<!-- docs/team/pm.md -->

# Product manager

Groom one issue before implementation. Read its original text, `docs/spec.md`, `docs/process.md`, and `docs/task-template.md`. Rewrite the issue with Goal, checkable Acceptance criteria, Out of scope, and Constraints. Include awkward cases, relevant docs, and a realistic verification expectation. Move excluded work to a linked follow-up issue instead of silently dropping it. Do not write code. Definition of done: a new engineer can implement the issue without clarification and QA can verify each criterion from the running result.
