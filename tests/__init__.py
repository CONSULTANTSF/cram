import pytest
from training.relational_algebra.exercise_01_map import *

import sqlalchemy as sa


@pytest.fixture
def database_engine():
    return sa.create_engine('postgresql://qbizinc@localhost/qbizinc')
