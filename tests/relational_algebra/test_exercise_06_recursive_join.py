import pytest


@pytest.mark.dependency(depends=['test_05_join_outer_spark'])
def test_06_recursive_join_python_imperative():
    assert False


@pytest.mark.dependency(depends=['test_06_recursive_join_python_imperative'])
def test_06_recursive_join_python_functional():
    assert False


@pytest.mark.dependency(depends=['test_06_recursive_join_python_functional'])
def test_06_recursive_join_sql():
    assert False


@pytest.mark.dependency(depends=['test_06_recursive_join_sql'])
def test_06_recursive_join_map_reduce():
    assert False


@pytest.mark.dependency(depends=['test_06_recursive_join_map_reduce'])
def test_06_recursive_join_spark():
    assert False
