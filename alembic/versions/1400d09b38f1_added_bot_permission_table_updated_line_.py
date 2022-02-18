"""added bot_permission table, updated line and newmembers table

Revision ID: 1400d09b38f1
Revises: cb43b2df8ebe
Create Date: 2022-01-25 15:43:57.627208

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '1400d09b38f1'
down_revision = 'cb43b2df8ebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bot_permissions_table = op.create_table('bot_permissions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('permission_name', sa.String(length=15), nullable=False),
                    sa.Column('permission_value', sa.Boolean(), nullable=False),
                    sa.Column('last_modified', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('line_messages',
                  sa.Column('num_id', sa.Integer(), sa.Identity(always=False, start=1, cycle=True), nullable=False))
    op.add_column('line_messages', sa.Column('title', sa.String(length=45), nullable=False))
    op.add_column('new_members', sa.Column('app_date', sa.DateTime(), nullable=False))
    op.add_column('new_members', sa.Column('link', sa.String(length=150), nullable=False))
    op.add_column('new_members', sa.Column('answer_one', sa.String(length=250), nullable=True))
    op.add_column('new_members', sa.Column('answer_two', sa.String(length=250), nullable=True))
    op.add_column('new_members', sa.Column('answer_three', sa.String(length=250), nullable=True))
    op.alter_column('new_members', 'meetup_id',
                    existing_type=sa.VARCHAR(length=10),
                    nullable=False)
    op.alter_column('new_members', 'meetup_name',
                    existing_type=sa.VARCHAR(length=25),
                    nullable=False)

    op.bulk_insert(bot_permissions_table, [{
        "id": 1,
        "permission_name": "group_join",
        "permission_value": False,
        "last_modified": datetime.now()
    }])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('new_members', 'meetup_name',
                    existing_type=sa.VARCHAR(length=25),
                    nullable=True)
    op.alter_column('new_members', 'meetup_id',
                    existing_type=sa.VARCHAR(length=10),
                    nullable=True)
    op.drop_column('new_members', 'answer_three')
    op.drop_column('new_members', 'answer_two')
    op.drop_column('new_members', 'answer_one')
    op.drop_column('new_members', 'link')
    op.drop_column('new_members', 'app_date')
    op.drop_column('line_messages', 'title')
    op.drop_column('line_messages', 'num_id')
    op.drop_table('bot_permissions')
    # ### end Alembic commands ###
