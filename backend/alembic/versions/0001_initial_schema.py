"""Initial schema for collections and observations tables.

Revision ID: 0001_initial
Revises:
Create Date: 2026-11-02 12:00:00
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "0001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_tables = set(inspector.get_table_names())

    if "collections" not in existing_tables:
        op.create_table(
            "collections",
            sa.Column("id", sa.String(), nullable=False),
            sa.Column("title", sa.String(), nullable=False),
            sa.Column("subtitle", sa.String(), nullable=False),
            sa.Column("color", sa.String(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
        )

    if "observations" not in existing_tables:
        op.create_table(
            "observations",
            sa.Column("id", sa.String(), nullable=False),
            sa.Column("collection_id", sa.String(), nullable=False),
            sa.Column("title", sa.String(length=120), nullable=False),
            sa.Column("body", sa.Text(), nullable=False),
            sa.Column("kind", sa.String(), nullable=False),
            sa.Column("place", sa.String(), nullable=False),
            sa.Column("region", sa.String(), nullable=False),
            sa.Column("date", sa.String(), nullable=False),
            sa.Column("color", sa.String(), nullable=False),
            sa.Column("tags", sa.JSON(), nullable=False),
            sa.Column("source", sa.String(), nullable=False),
            sa.Column("starred", sa.Boolean(), nullable=False, server_default=sa.text("false")),
            sa.Column("x", sa.Float(), nullable=False, server_default=sa.text("50.0")),
            sa.Column("y", sa.Float(), nullable=False, server_default=sa.text("50.0")),
            sa.ForeignKeyConstraint(["collection_id"], ["collections.id"]),
            sa.PrimaryKeyConstraint("id"),
        )


def downgrade() -> None:
    op.drop_table("observations")
    op.drop_table("collections")
