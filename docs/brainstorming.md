# Brainstorming record

## Initial brief
Build a non-trivial app idea, different from the student's Part I project, that is worth showing. Avoid habit trackers and to-do lists. Follow AI-native specification and full-stack build workflows: think through product scope, use GitHub Issues, a deliberate visual reference, mock-backed frontend first, OpenAPI contract, in-memory backend, SQLite persistence through an ORM, and then integration. Include Markdown docs and a record of the brainstorming. Run and thoroughly test the app; report actual bugs as `user-test-bug` issues and have PM/QA groom and verify. Close MVP and user-test-bug issues through QA before the deadline.

## Idea exploration
Candidate ideas included a neighborhood soundwalk archive, a personal museum of found objects, an oral-history map, and a field-research atlas. The field-research atlas combines the strongest portfolio demo (map + evidence detail + relationships), has a clear user and workflow, and can grow into a niche research tool rather than another generic productivity list.

## Chosen idea: Fieldnote Atlas
An independent researcher, designer, journalist, urbanist, or student collects field observations, interview fragments, artifacts, and signals. Each item retains its place, date, source, tags, and links to related evidence. A map and reading panel help the researcher spot patterns across locations and visits.

## Part I comparison
Part I was StudyFlow, a local student task planner for assignments, due dates, priorities, completion, filters, and progress stored in browser localStorage. Part II is Fieldnote Atlas, a map-based archive for place-based research observations, evidence sources, tags, and collections. The projects address different users and problems and have different core workflows; Fieldnote Atlas is distinct from StudyFlow.

## MVP decisions
- Desktop-first local app; no login or collaboration in MVP.
- Seed with fictional Almaty observations to create a compelling demo without exposing private data.
- Deliver browsing, pin selection, search, basic filters, starring, and adding a field note.
- Use a typed frontend service abstraction; begin with a mock service and move to the agreed HTTP API.
- API backend: FastAPI; persistence: SQLAlchemy + SQLite.
- Visual direction: warm editorial research journal, muted cartography, terracotta pins, serif titles, mono metadata. Inspiration pointers are in `design-system.md`.

## Build workflow
The MVP follows five inspectable checkpoints: frontend with mock service; OpenAPI verified against the service boundary; in-memory backend; SQLAlchemy/SQLite repository; frontend connected to persistent backend. GitHub Issues are canonical in `Sabyrzhan01/fieldnote-atlas`; current issue state is recorded in `docs/issues.md`.
