from Ai import *

import pytest

@pytest.fixture
def return_1():
    return 1

@pytest.fixture(scope='class')
def Move():
    self.M = 1
    B = 2
    return 1

def test_one(return_1):
    #digit = return_1()
    assert return_1 == 1

def test_findBestMove(gs, validMoves):
    assert 1 == 1

def test_M(Move):
    assert Move.M == 1


# протестировать королеву, слона и ладью с помощью фикстуры диагональных и прямых ходов фигуры