"""Adds transcription table

Revision ID: 0d26fea9d934
Revises: 24e9d6374256
Create Date: 2019-10-16 02:41:54.939838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0d26fea9d934"
down_revision = "24e9d6374256"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "transcription",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("file_id", sa.Integer(), nullable=False),
        sa.Column("transcription", sa.Text(), nullable=False),
        sa.Column("start_time", sa.Float(), nullable=False),
        sa.Column("end_time", sa.Float(), nullable=False),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "last_modified",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.utc_timestamp(),
        ),
        sa.ForeignKeyConstraint(["file_id"], ["data.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transcription")
    # ### end Alembic commands ###
