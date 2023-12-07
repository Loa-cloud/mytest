import pytest


@pytest.fixture
def return_1():
    return 3

def test_one():
    digit = return_1()
    assert digit == 1