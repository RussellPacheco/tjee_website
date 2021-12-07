"""create members table

Revision ID: adcb3e9876ca
Revises: 
Create Date: 2021-12-05 08:59:53.003865

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from uuid import uuid4
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'adcb3e9876ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("members",
                    sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column("first_name", sa.String(length=35), nullable=False),
                    sa.Column("last_name", sa.String(length=35), nullable=False),
                    sa.Column("gender", sa.Text(length=1), nullable=False),
                    sa.Column("country", sa.Text(length=56), nullable=False),
                    sa.Column("native_lang", sa.Text(length=20), nullable=False),
                    sa.Column("lang_focus", sa.Text(length=3), nullable=False),
                    sa.Column("line_id", sa.Text(length=15), nullable=True, unique=True),
                    sa.Column("line_api_id", sa.String(length=40), nullable=True, unique=True),
                    sa.Column("meetup_id", sa.Text(length=10), nullable=True, unique=True),
                    sa.Column("meetup_name", sa.Text(length=25), nullable=True),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint("id")
                    )
    op.create_table("admins",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("member_id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
                    sa.Column("username", sa.String(length=65), nullable=False),
                    sa.Column("password", sa.String(length=200), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table("line_messages",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("created_by", postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column("message", sa.Text(length=700), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_sent", sa.DateTime(), nullable=True),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['created_by'], ['members.id'], ondelete="SET NULL"),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table("new_members",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("meetup_id", sa.Text(length=10), nullable=True, unique=True),
                    sa.Column("meetup_name", sa.Text(length=25), nullable=True),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade():
    op.drop_table("members")
    op.drop_table("admins")
    pass
