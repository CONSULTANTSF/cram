"""create event log

Revision ID: 64c02ea7d605
Revises: 
Create Date: 2019-01-07 11:14:03.213058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64c02ea7d605'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transaction',
        sa.Column('customer_id', sa.Integer),
        sa.Column('product_id', sa.Integer),
        sa.Column('quantity', sa.BigInteger),
        sa.Column('price_total_quantity', sa.Numeric(24, 2)),
    )


def downgrade():
    op.drop_table('transaction')
