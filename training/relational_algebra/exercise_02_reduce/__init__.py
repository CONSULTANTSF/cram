import sqlalchemy as sa


def database_metadata():
    return sa.MetaData()

def database_transaction_table(metadata):
    return sa.Table(
        'transaction', metadata,
        sa.Column('customer_id', sa.Integer),
        sa.Column('product_id', sa.Integer),
        sa.Column('quantity', sa.BigInteger),
        sa.Column('price_total_quantity', sa.Numeric(24, 2)),
    )
