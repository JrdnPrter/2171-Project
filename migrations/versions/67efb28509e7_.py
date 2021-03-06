"""empty message

Revision ID: 67efb28509e7
Revises: bef678c7ebfd
Create Date: 2021-03-24 23:06:58.745648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67efb28509e7'
down_revision = 'bef678c7ebfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee_profiles', sa.Column('empid', sa.String(length=10), nullable=False))
    op.drop_column('employee_profiles', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee_profiles', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('employee_profiles', 'empid')
    # ### end Alembic commands ###
