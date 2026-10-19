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
