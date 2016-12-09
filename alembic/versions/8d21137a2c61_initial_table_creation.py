"""Initial table creation

Peek App Database Migration Script

Revision ID: 8d21137a2c61
Revises: 
Create Date: 2016-11-04 19:39:33.513670

"""

# revision identifiers, used by Alembic.
revision = '8d21137a2c61'
down_revision = None
branch_labels = None
depends_on = None

import sqlalchemy as sa

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('NoopTable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('string1', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='papp_noop'
    )
    op.create_index('idx_NoopTable_unique_index', 'NoopTable', ['id', 'string1'], unique=True, schema='papp_noop')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_NoopTable_unique_index', table_name='NoopTable', schema='papp_noop')
    op.drop_table('NoopTable', schema='papp_noop')
    ### end Alembic commands ###
