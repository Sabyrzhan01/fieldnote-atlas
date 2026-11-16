"""Store street-map coordinates separately from sketch positions."""

from alembic import op
import sqlalchemy as sa

revision = "0002_geographic"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade():
    columns = {column["name"] for column in sa.inspect(op.get_bind()).get_columns("observations")}
    for name in ("latitude", "longitude"):
        if name not in columns:
            op.add_column("observations", sa.Column(name, sa.Float(), nullable=True))


def downgrade():
    with op.batch_alter_table("observations") as table:
        table.drop_column("longitude")
        table.drop_column("latitude")
