"""Create password column

Revision ID: c27b7888a4fb
Revises: e0cfcb59f5d8
Create Date: 2020-02-09 14:07:07.687018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c27b7888a4fb'
down_revision = 'e0cfcb59f5d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch_users', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch_users', 'password')
    # ### end Alembic commands ###
