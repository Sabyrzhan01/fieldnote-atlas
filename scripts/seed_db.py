#!/usr/bin/env python3
"""Standalone idempotent database seeding script for PostgreSQL / SQLite."""
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.repository import SQLAlchemyRepository


def seed_database(target_url: str | None = None, force: bool = False) -> dict:
    url = target_url or os.getenv("DATABASE_URL") or os.getenv("FIELDNOTE_DB_URL")
    if not url:
        raise ValueError("DATABASE_URL environment variable is required to seed the database.")
    repo = SQLAlchemyRepository(url, seed_if_empty=True)
    if force:
        atlas = repo.reset()
    else:
        atlas = repo.list_atlas()
    result = {
        "collections": len(atlas["collections"]),
        "observations": len(atlas["observations"]),
    }
    print(f"[+] Database seeded at {repo.url}: {result['collections']} collections, {result['observations']} observations.")
    return result


if __name__ == "__main__":
    seed_database()
