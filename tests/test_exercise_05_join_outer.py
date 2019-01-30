import pytest


@pytest.mark.dependency(depends=['test_04_join_natural_spark'])
def test_05_join_outer_python_imperative():
    assert False


@pytest.mark.dependency(depends=['test_05_join_outer_python_imperative'])
def test_05_join_outer_python_functional():
    assert False


@pytest.mark.dependency(depends=['test_05_join_outer_python_functional'])
def test_05_join_outer_sql():
    assert False


@pytest.mark.dependency(depends=['test_05_join_outer_sql'])
def test_05_join_outer_map_reduce():
    assert False


@pytest.mark.dependency(depends=['test_05_join_outer_map_reduce'])
def test_05_join_outer_spark():
    assert False
