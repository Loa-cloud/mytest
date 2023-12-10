import pytest


@pytest.fixture
def return_1():
    return 1

def test_one(return_1):
    #digit = return_1()
    assert return_1 == 1


# протестировать королеву, слона и ладью с помощью фикстуры диагональных и прямых ходов фигуры