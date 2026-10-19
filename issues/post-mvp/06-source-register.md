# Post-MVP: Source register and citations

## Goal
Researchers can maintain reusable source records and cite them consistently across observations.

## Acceptance criteria
- [ ] A source has a stable ID, title, creator, source type, publication/date, and optional URL or archival identifier.
- [ ] An observation can reference one or more sources while preserving a short excerpt and page/time locator.
- [ ] Source details are readable from the observation and source register.
- [ ] Deleting or editing a source cannot silently erase observation content or citations.
- [ ] API, SQLite constraints, and UI behavior have regression coverage.

## Out of scope
- Automatic web scraping, citation-style generation, and uploaded files.

## Constraints
- Keep provenance distinct from observation text; validate external links and render them safely.
