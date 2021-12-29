"""added bot_permissions table

Revision ID: 974043b41734
Revises: cb43b2df8ebe
Create Date: 2021-12-21 21:32:47.496190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '974043b41734'
down_revision = 'cb43b2df8ebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bot_permissions = op.create_table('bot_permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission_name', sa.String(15), nullable=False),
    sa.Column('permission_value', sa.Boolean(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(bot_permissions, [{"id": 1, "permission_name": "group_join", "permission_value": False}])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bot_permissions')
    # ### end Alembic commands ###
