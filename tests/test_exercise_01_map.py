import pytest
from . import *
from training.exercise_01_map.python_imperative import *
from training.exercise_01_map.python_functional import *
from training.exercise_01_map.sql import *
from training.exercise_01_map.map_reduce import *
from training.exercise_01_map.spark import *

from mrjob.inline import InlineMRJobRunner
import pyrsistent

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


@pytest.mark.dependency()
def test_01_map_python_imperative(event_log_table):
    try:
        actual_ = python_imperative(event_log_table)
    except NotImplementedError:
        print('''
Please see the ./training/exercise_01_map/python_imperative.py and complete the python_imperative() function.
        ''')
        assert False
    actual = []
    for row in actual_:
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


@pytest.mark.dependency(depends=['test_01_map_python_imperative'])
def test_01_map_python_functional(event_log_table):
    try:
        actual_ = python_functional(event_log_table)
    except NotImplementedError:
        print('''
Please see the ./training/exercise_01_map/python_functional.py and complete the python_functional() function.
        ''')
        assert False
    actual = []
    for row in actual_:
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


@pytest.mark.dependency(depends=['test_01_map_python_functional'])
def test_01_map_sql(rollback_connection):
    try:
        sql_ = sql()
    except NotImplementedError:
        print('''
Please see the ./training/exercise_01_map/sql.py and complete the sql() function.
        ''')
        assert False
    actual = []
    for row in rollback_connection.execute(sql_):
        row_ = dict(row)
        row_['price_total_quantity'] = row_['price_total_quantity'].normalize().as_tuple()
        row_['price_per_unit'] = row_['price_per_unit'].normalize().as_tuple()
        actual.append(pyrsistent.pmap(row_))
    actual = pyrsistent.pset(actual)
    assert expected == actual


@pytest.mark.dependency(depends=['test_01_map_map_reduce'])
def test_01_map_map_reduce():
    try:
        mrjob_cls = map_reduce()
    except NotImplementedError:
        print('''
Please see the ./training/exercise_01_map/map_reduce.py and complete the map_reduce() function.
        ''')
        assert False
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


@pytest.mark.dependency(depends=['test_01_map_map_reduce'])
def test_01_map_spark():
    assert False
