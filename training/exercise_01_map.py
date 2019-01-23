import sqlalchemy as sa

import decimal
import mrjob.job as mrj


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
    return []


def python_functional_map(sequence):
    return []


def sql_map():
    return '''
    '''


def map_reduce_map():
    return mrj.MRJob()


def spark_map(sequence):
    return
