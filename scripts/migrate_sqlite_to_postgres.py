#!/usr/bin/env python3
"""
Migrate Fieldnote Atlas data from SQLite to PostgreSQL.

Usage:
    python scripts/migrate_sqlite_to_postgres.py [--source sqlite:///path/to/db.sqlite3] [--target postgresql://user:pass@host:5432/dbname]

If not specified, source defaults to `fieldnote-atlas.sqlite3` at repo root,
and target defaults to `DATABASE_URL` or `FIELDNOTE_DB_URL` environment variable.
"""

import os
import sys
import argparse
from pathlib import Path

# Add project root to path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from backend.app.repository import SQLAlchemyRepository

def migrate(source_url: str, target_url: str) -> dict:
    print(f"[*] Connecting to source: {source_url}")
    source_repo = SQLAlchemyRepository(source_url)
    source_data = source_repo.list_atlas()
    
    src_collections = source_data.get("collections", [])
    src_observations = source_data.get("observations", [])
    print(f"[*] Read {len(src_collections)} collections and {len(src_observations)} observations from source.")

    print(f"[*] Connecting to target: {target_url}")
    target_repo = SQLAlchemyRepository(target_url, seed_if_empty=False)

    # Insert or update collections and observations into target
    with target_repo.Session() as session:
        existing_col_ids = {c.id for c in session.query(target_repo.C).all()}
        added_cols = 0
        for col in src_collections:
            if col["id"] not in existing_col_ids:
                added_cols += 1
            session.merge(target_repo.C(
                id=col["id"],
                title=col["title"],
                subtitle=col["subtitle"],
                color=col["color"]
            ))
        session.commit()

        existing_obs_ids = {o.id for o in session.query(target_repo.O).all()}
        added_obs = 0
        for obs in src_observations:
            if obs["id"] not in existing_obs_ids:
                added_obs += 1
            session.merge(target_repo.O(
                id=obs["id"],
                collection_id=obs.get("collection_id", "c1"),
                title=obs["title"],
                body=obs["body"],
                kind=obs["kind"],
                place=obs["place"],
                region=obs["region"],
                date=obs["date"],
                color=obs["color"],
                tags=obs.get("tags") or [],
                source=obs["source"],
                starred=bool(obs.get("starred", False)),
                x=float(obs.get("x", 50.0)),
                y=float(obs.get("y", 50.0))
            ))
        session.commit()

    target_data = target_repo.list_atlas()
    final_cols = len(target_data.get("collections", []))
    final_obs = len(target_data.get("observations", []))
    print(f"[+] Migration complete! Target now contains {final_cols} collections and {final_obs} observations.")
    return {
        "source_collections": len(src_collections),
        "source_observations": len(src_observations),
        "target_collections": final_cols,
        "target_observations": final_obs,
        "added_collections": added_cols,
        "added_observations": added_obs,
    }

def main():
    parser = argparse.ArgumentParser(description="Migrate Fieldnote Atlas SQLite database to PostgreSQL.")
    parser.add_argument("--source", help="Source SQLite URL (e.g. sqlite:///fieldnote-atlas.sqlite3)")
    parser.add_argument("--target", help="Target PostgreSQL URL (e.g. postgresql://user:pass@host:5432/dbname)")
    args = parser.parse_args()

    default_source_file = ROOT_DIR / "fieldnote-atlas.sqlite3"
    source = args.source or f"sqlite:///{default_source_file}"
    target = args.target or os.getenv("DATABASE_URL") or os.getenv("FIELDNOTE_DB_URL")

    if not target:
        print("[!] ERROR: Target database URL not provided.")
        print("    Specify --target or set DATABASE_URL / FIELDNOTE_DB_URL environment variable.")
        sys.exit(1)

    result = migrate(source, target)
    print(f"[OK] Migration summary: {result}")

if __name__ == "__main__":
    main()
