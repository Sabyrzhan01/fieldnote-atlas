# DevOps: SQLite to PostgreSQL Migration & Dual-Database Support

**Labels:** `devops`, `database`

## Goal
Support production PostgreSQL alongside local SQLite using SQLAlchemy, and provide an automated data migration utility.

## Description
- Upgrade `backend/app/repository.py` to `SQLAlchemyRepository`, supporting both SQLite (`sqlite:///`) and PostgreSQL (`postgresql://`).
- Automatically normalize legacy `postgres://` connection strings provided by cloud providers (Render, Railway, Heroku).
- Add `psycopg2-binary` and `psycopg` drivers to `backend/requirements.txt`.
- Implement `scripts/migrate_sqlite_to_postgres.py` to copy collections, observations, tags, coordinates, and star statuses from SQLite to PostgreSQL.
- Add unit/integration tests for database migrations and connection string parsing.

## Deliverables
- `backend/app/repository.py`
- `scripts/migrate_sqlite_to_postgres.py`
- `backend/requirements.txt`
- `backend/tests/test_repository.py`

## Acceptance Criteria
- [x] Application connects seamlessly to PostgreSQL when `DATABASE_URL` is set.
- [x] SQLite fallback works seamlessly without configuration.
- [x] Migration script copies data with 100% fidelity.
- [x] All 10 repository unit tests pass.
