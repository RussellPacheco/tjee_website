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
import hashlib, os, binascii

# Generate hashed password
salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
hashed_pwd = hashlib.pbkdf2_hmac("sha512", os.getenv("TEMP_PASSWORD").encode("utf-8"), salt, 100000)
hashed_pwd = binascii.hexlify(hashed_pwd)
salt_hashedpwd = (salt + hashed_pwd).decode("ascii")

# Generate current timestamp
TIMESTAMP = datetime.now()

# Generate UUID for seed
UUID = uuid4()
UUID2 = uuid4()

# revision identifiers, used by Alembic.
revision = 'adcb3e9876ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    members = op.create_table("members",
                    sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column("firstname", sa.String(length=35), nullable=False),
                    sa.Column("lastname", sa.String(length=35), nullable=False),
                    sa.Column("gender", sa.String(length=6), nullable=False),
                    sa.Column("country", sa.String(length=56), nullable=False),
                    sa.Column("native_lang", sa.String(length=20), nullable=False),
                    sa.Column("lang_focus", sa.String(length=8), nullable=False),
                    sa.Column("line_id", sa.String(length=15), nullable=True, unique=True),
                    sa.Column("line_api_id", sa.String(length=40), nullable=True, unique=True),
                    sa.Column("meetup_id", sa.String(length=10), nullable=True, unique=True),
                    sa.Column("meetup_name", sa.String(length=25), nullable=True),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint("id")
                    )
    admins = op.create_table("admins",
                    sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
                    sa.Column("member_id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
                    sa.Column("username", sa.String(length=65), nullable=False),
                    sa.Column("password", sa.String(length=200), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table("line_messages",
                    sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False, unique=True),
                    sa.Column("created_by", postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column("message", sa.String(length=700), nullable=False),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.Column("last_sent", sa.DateTime(), nullable=True),
                    sa.Column("last_modified", sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['created_by'], ['members.id'], ondelete="SET NULL"),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table("new_members",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("meetup_id", sa.String(length=10), nullable=True, unique=True),
                    sa.Column("meetup_name", sa.String(length=25), nullable=True),
                    sa.Column("created_at", sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.bulk_insert(members, [{
        "id": UUID,
        "firstname": "Admin",
        "lastname": "Montecruz",
        "gender": "Male",
        "country": "Japan",
        "native_lang": "English",
        "lang_focus": "Japanese",
        "line_id": "n/a",
        "line_api_id": "n/a",
        "meetup_id": "n/a",
        "meetup_name": "n/a",
        "created_at": TIMESTAMP,
        "last_modified": TIMESTAMP
    }])

    op.bulk_insert(admins, [{
        "id": UUID2,
        "member_id": UUID,
        "username": "russ1487",
        "password": salt_hashedpwd,
        "created_at": TIMESTAMP,
        "last_modified": TIMESTAMP
    }])

    pass


def downgrade():
    op.drop_table("admins")
    op.drop_table("line_messages")
    op.drop_table("new_members")
    op.drop_table("members")
    pass
