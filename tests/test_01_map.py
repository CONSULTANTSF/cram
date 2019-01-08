import pytest
from training.exercise_01_map import *

import pyrsistent
import sqlalchemy as sa

import decimal


def database_engine():
    return sa.create_engine('postgresql://qbizinc@localhost/qbizinc')


@pytest.fixture
def event_log_table():
    metadata = database_metadata()
    transaction_table = database_transaction_table(metadata)
    with database_engine().begin() as conn:
        conn.execute(transaction_table.insert(), [
            {'customer_id': 1, 'product_id': 1, 'quantity': 10, 'price_total_quantity': decimal.Decimal('0.25')},
            {'customer_id': 2, 'product_id': 1, 'quantity': 5 , 'price_total_quantity': decimal.Decimal('0.50')},
            {'customer_id': 3, 'product_id': 2, 'quantity': 15, 'price_total_quantity': decimal.Decimal('0.75')},
            {'customer_id': 1, 'product_id': 2, 'quantity': 10, 'price_total_quantity': decimal.Decimal('1.00')},
            {'customer_id': 2, 'product_id': 3, 'quantity': 5 , 'price_total_quantity': decimal.Decimal('1.25')},
            {'customer_id': 3, 'product_id': 3, 'quantity': 15, 'price_total_quantity': decimal.Decimal('1.50')},
        ])
        return [dict(row) for row in conn.execute(transaction_table.select())]


expected = pyrsistent.pset([
    pyrsistent.pmap({'customer_id': 1, 'product_id': 1, 'quantity': 10, 'price_total_quantity': decimal.Decimal('0.25'), 'price_per_unit': decimal.Decimal('0.0250')}),
    pyrsistent.pmap({'customer_id': 2, 'product_id': 1, 'quantity': 5 , 'price_total_quantity': decimal.Decimal('0.50'), 'price_per_unit': decimal.Decimal('0.1000')}),
    pyrsistent.pmap({'customer_id': 3, 'product_id': 2, 'quantity': 15, 'price_total_quantity': decimal.Decimal('0.75'), 'price_per_unit': decimal.Decimal('0.0500')}),
    pyrsistent.pmap({'customer_id': 1, 'product_id': 2, 'quantity': 10, 'price_total_quantity': decimal.Decimal('1.00'), 'price_per_unit': decimal.Decimal('0.1000')}),
    pyrsistent.pmap({'customer_id': 2, 'product_id': 3, 'quantity': 5 , 'price_total_quantity': decimal.Decimal('1.25'), 'price_per_unit': decimal.Decimal('0.2500')}),
    pyrsistent.pmap({'customer_id': 3, 'product_id': 3, 'quantity': 15, 'price_total_quantity': decimal.Decimal('1.50'), 'price_per_unit': decimal.Decimal('0.3000')}),
])


def test_python_imperative_map(event_log_table):
    assert expected == pyrsistent.pset(pyrsistent.pmap(row) for row in python_imperative_map([event_log_table]))
