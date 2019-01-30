import pytest


@pytest.mark.dependency(depends=['test_03_partition_reduce_spark'])
def test_04_join_natural_python_imperative():
    assert False


@pytest.mark.dependency(depends=['test_04_join_natural_python_imperative'])
def test_04_join_natural_python_functional():
    assert False


@pytest.mark.dependency(depends=['test_04_join_natural_python_functional'])
def test_04_join_natural_sql():
    assert False


@pytest.mark.dependency(depends=['test_04_join_natural_sql'])
def test_04_join_natural_map_reduce():
    assert False


@pytest.mark.dependency(depends=['test_04_join_natural_map_reduce'])
def test_04_join_natural_spark():
    assert False
