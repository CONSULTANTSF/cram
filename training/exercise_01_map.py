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


def python_imperative_map(sequence):
    return

def python_functional_map(sequence):
    return

def sql_map(sequence):
    return

def map_reduce_map(sequence):
    return

def spark_map(sequence):
    return
