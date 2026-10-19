# Post-MVP: Safe archive import with duplicate review

## Goal
Researchers can bring an existing archive into a collection and inspect changes before saving.

## Acceptance criteria
- [ ] Documented CSV/JSON format maps to supported observation fields.
- [ ] Invalid rows show row numbers and field-level reasons.
- [ ] Preview summarizes creates, duplicates, and validation errors before commit.
- [ ] Import is atomic or reports partial results; retry does not duplicate committed rows.
- [ ] Unicode, delimiters, malformed data, and duplicate-key cases are tested.

## Out of scope
- Media ingestion, external services, and semantic deduplication.

## Constraints
- Enforce file-size and row-count limits; never execute imported content.
