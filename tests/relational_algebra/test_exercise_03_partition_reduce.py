import pytest


@pytest.mark.dependency(depends=['test_02_reduce_spark'])
def test_03_partition_reduce_python_imperative():
    assert False


@pytest.mark.dependency(depends=['test_03_partition_reduce_python_imperative'])
def test_03_partition_reduce_python_functional():
    assert False


@pytest.mark.dependency(depends=['test_03_partition_reduce_python_functional'])
def test_03_partition_reduce_sql():
    assert False


@pytest.mark.dependency(depends=['test_03_partition_reduce_sql'])
def test_03_partition_reduce_map_reduce():
    assert False


@pytest.mark.dependency(depends=['test_03_partition_reduce_map_reduce'])
def test_03_partition_reduce_spark():
    assert False
