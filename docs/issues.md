# GitHub issue backlog

Labels mvp, post-mvp, and user-test-bug exist in [the project repository](https://github.com/Sabyrzhan01/fieldnote-atlas). The 14 groomed MVP bodies are in issues/mvp/; ten scoped follow-ups are in issues/post-mvp/. GitHub Issues are canonical for current status. MVP and user-test-bug issue closure is documented in their comments and docs/qa-results.md. Post-MVP items represent deferred product capabilities, not promises that they are implemented.

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
Ten detailed follow-up issues are specified in issues/post-mvp/ and tracked as open GitHub issues with the post-mvp label (#17–#21, #23–#27):
- [Edit observations](../issues/post-mvp/01-edit-observations.md)
- [Delete and undo](../issues/post-mvp/02-delete-and-undo.md)
- [Evidence connections](../issues/post-mvp/03-evidence-connections.md)
- [Collection management](../issues/post-mvp/04-collections-management.md)
- [Export and mobile workflow](../issues/post-mvp/05-export-and-mobile.md)
- [Source register and citations](../issues/post-mvp/06-source-register.md) · [#23](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/23)
- [Research visit timeline](../issues/post-mvp/07-visit-timeline.md) · [#24](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/24)
- [Accessible map and evidence navigation](../issues/post-mvp/08-accessibility.md) · [#25](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/25)
- [Map layers and accessible legend](../issues/post-mvp/09-map-layers.md) · [#26](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/26)
- [Safe archive import with duplicate review](../issues/post-mvp/10-import-review.md) · [#27](https://github.com/Sabyrzhan01/fieldnote-atlas/issues/27)

Additional candidates after these scoped issues: place geocoding/map tiles with attribution, richer source attachments, and multi-researcher sharing/permissions.

## User-test bug procedure
Create a new user-test-bug issue only after a real manual test finds a defect. Include Goal and Description, steps, expected/actual behavior, and browser. PM grooms; QA adds regression cases; QA closes only after retest PASS.

## Assignment 2: Test, Containerise, and Deploy Backlog

### Playwright End-to-End Tests (`e2e-test`)
Ten comprehensive end-to-end test issues covering every feature separately, located in `issues/e2e-tests/`:
1. [01. Editorial Atlas Shell & Collection Navigation](../issues/e2e-tests/01-editorial-atlas-shell.md) — Goal: verify header, sidebar, branding, collections, and workspace navigation with Playwright.
2. [02. Interactive Map Observation Pin Selection](../issues/e2e-tests/02-map-pin-selection.md) — Goal: verify map rendering, pin coordinates, active pin state, and reader synchronization.
3. [03. Real-Time Observation Search](../issues/e2e-tests/03-search-observations.md) — Goal: verify case-insensitive search by title, body, and tag with real-time pin updates.
4. [04. Filter Cycling (All Notes, Starred, Interviews)](../issues/e2e-tests/04-filter-observations.md) — Goal: verify category filter cycling and accurate pin subset display.
5. [05. Create Fieldnote Observation Modal](../issues/e2e-tests/05-create-fieldnote.md) — Goal: verify create modal dialog, validation, toast alert, and instant map update.
6. [06. Star and Unstar Observations](../issues/e2e-tests/06-star-observation.md) — Goal: verify favorite toggle, heart icons, toast notifications, and DB persistence.
7. [07. Tag Chip Filtering Navigation](../issues/e2e-tests/07-tag-navigation.md) — Goal: verify clicking tag chips in reader filters observations.
8. [08. Connected Evidence Navigation](../issues/e2e-tests/08-connected-observations.md) — Goal: verify clicking linked evidence transitions to related observation.
9. [09. Export Atlas JSON Archive](../issues/e2e-tests/09-export-atlas.md) — Goal: verify export button triggers valid `fieldnote-atlas.json` download.
10. [10. Full API & Database Persistence Lifecycle](../issues/e2e-tests/10-api-persistence.md) — Goal: verify client-server and database persistence lifecycle across browser reloads.

### DevOps, Containerization & Cloud Deployment (`devops`)
Seven infrastructure and deployment issues located in `issues/devops/`:
1. [01. Single Production Dockerfile](../issues/devops/01-single-dockerfile.md) — Goal: bundle static frontend and FastAPI backend into a single non-root Docker container.
2. [02. SQLite to PostgreSQL Migration](../issues/devops/02-sqlite-to-postgres-migration.md) — Goal: SQLAlchemy dual-DB support and migration script (`migrate_sqlite_to_postgres.py`).
3. [03. Multi-Container Docker Compose Stack](../issues/devops/03-docker-compose-stack.md) — Goal: turn-key Docker Compose stack for app + PostgreSQL 16.
4. [04. PaaS Deployment (Render, Railway, Vercel)](../issues/devops/04-render-railway-vercel-deployment.md) — Goal: declarative configuration files for Render, Railway, and Vercel.
5. [05. AWS CloudFormation Free-Tier Deployment](../issues/devops/05-aws-cloudformation-free-tier.md) — Goal: 100% Free Tier CloudFormation template on EC2 t2/t3.micro with 20GB EBS.
6. [06. GCP Terraform Free-Tier Deployment](../issues/devops/06-gcp-terraform-free-tier.md) — Goal: Terraform config for Google Cloud Always Free tier (`e2-micro`, 25GB disk).
7. [07. GitHub Actions CI/CD Pipeline](../issues/devops/07-github-actions-ci-cd.md) — Goal: automated testing across Python, Node, and Playwright, and deployment on commit to `main`.
