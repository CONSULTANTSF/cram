import pytest
from training.exercise_01_map import *
from training.exercise_01_map.python_imperative import *
from training.exercise_01_map.python_functional import *
from training.exercise_01_map.sql import *
from training.exercise_01_map.map_reduce import *
from training.exercise_01_map.spark import *

from mrjob.inline import InlineMRJobRunner
import pyrsistent
import sqlalchemy as sa

import decimal
import io


with decimal.localcontext() as dctx:
    dctx.prec = 28
    price_total_quantity_values = [
        decimal.Decimal('0.25'),
        decimal.Decimal('0.50'),
        decimal.Decimal('0.75'),
        decimal.Decimal('1.00'),
        decimal.Decimal('1.25'),
        decimal.Decimal('1.50'),
    ]
with decimal.localcontext() as dctx:
    dctx.prec = 28
    price_per_unit_values = [
        decimal.Decimal('0.0250'),
        decimal.Decimal('0.1000'),
        decimal.Decimal('0.0500'),
        decimal.Decimal('0.1000'),
        decimal.Decimal('0.2500'),
        decimal.Decimal('0.1000'),
    ]


input_ = [
    {'customer_id': 1, 'product_id': 1, 'quantity': 10L, 'price_total_quantity': price_total_quantity_values[0]},
    {'customer_id': 2, 'product_id': 1, 'quantity': 5L , 'price_total_quantity': price_total_quantity_values[1]},
    {'customer_id': 3, 'product_id': 2, 'quantity': 15L, 'price_total_quantity': price_total_quantity_values[2]},
    {'customer_id': 1, 'product_id': 2, 'quantity': 10L, 'price_total_quantity': price_total_quantity_values[3]},
    {'customer_id': 2, 'product_id': 3, 'quantity': 5L , 'price_total_quantity': price_total_quantity_values[4]},
    {'customer_id': 3, 'product_id': 3, 'quantity': 15L, 'price_total_quantity': price_total_quantity_values[5]},
]


input_bytes = io.BytesIO('\n'.join(
    '{customer_id},{product_id},{quantity},{price_total_quantity}'.format(**r)
    for r in input_
))


expected = pyrsistent.pset([
    pyrsistent.pmap({'customer_id': 1, 'product_id': 1, 'quantity': 10L, 'price_total_quantity': price_total_quantity_values[0].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[0].normalize().as_tuple()}),
    pyrsistent.pmap({'customer_id': 2, 'product_id': 1, 'quantity': 5L , 'price_total_quantity': price_total_quantity_values[1].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[1].normalize().as_tuple()}),
    pyrsistent.pmap({'customer_id': 3, 'product_id': 2, 'quantity': 15L, 'price_total_quantity': price_total_quantity_values[2].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[2].normalize().as_tuple()}),
    pyrsistent.pmap({'customer_id': 1, 'product_id': 2, 'quantity': 10L, 'price_total_quantity': price_total_quantity_values[3].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[3].normalize().as_tuple()}),
    pyrsistent.pmap({'customer_id': 2, 'product_id': 3, 'quantity': 5L , 'price_total_quantity': price_total_quantity_values[4].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[4].normalize().as_tuple()}),
    pyrsistent.pmap({'customer_id': 3, 'product_id': 3, 'quantity': 15L, 'price_total_quantity': price_total_quantity_values[5].normalize().as_tuple(), 'price_per_unit': price_per_unit_values[5].normalize().as_tuple()}),
])


@pytest.fixture
def database_engine():
    return sa.create_engine('postgresql://qbizinc@localhost/qbizinc')


@pytest.fixture
def rollback_connection(database_engine):
    metadata = database_metadata()
    transaction_table = database_transaction_table(metadata)
    try:
        with database_engine.begin() as conn:
            conn.execute(transaction_table.insert(), input_)
            yield conn
            raise AssertionError()
    except AssertionError:
        pass


@pytest.fixture
def event_log_table(rollback_connection):
    metadata = database_metadata()
    transaction_table = database_transaction_table(metadata)
    table = []
    for row in rollback_connection.execute(transaction_table.select()):
        table.append(row)
    return table


def test_python_imperative(event_log_table):
    actual = []
    for row in python_imperative(event_log_table):
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


def test_python_functional(event_log_table):
    actual = []
    for row in python_functional(event_log_table):
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


def test_sql(rollback_connection):
    sql_ = sql()
    actual = []
    for row in rollback_connection.execute(sql_):
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


def test_map_reduce():
    mrjob_cls = map_reduce()
    mrjob = mrjob_cls()
    mrjob.sandbox(stdin=input_bytes)
    mrjob_runner = mrjob.make_runner()
    actual = set()
    mrjob_runner.run()
    for line in mrjob_runner.stream_output():
        row, count = mrjob.parse_output_line(line)
        assert 1 == count
        values = row.split(',')
        assert 5 == len(values)
        customer_id, product_id, quantity, price_total_quantity, price_per_unit = values
        actual.add(pyrsistent.pmap({
            'customer_id': int(customer_id),
            'product_id': int(product_id),
            'quantity': long(quantity),
            'price_total_quantity': decimal.Decimal(price_total_quantity).normalize().as_tuple(),
            'price_per_unit': decimal.Decimal(price_per_unit).normalize().as_tuple(),
        }))
    actual = pyrsistent.pset(actual)
    assert expected == actual
