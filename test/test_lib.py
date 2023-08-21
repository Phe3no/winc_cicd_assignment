from static.python.calculations import add, substract, multiply, divide, remainder
import sys
sys.path.append("..")


def test_add():
    assert add(2, 2) == 4
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(-2, -3) == -5


def test_substract():
    assert substract(2, 2) == 0
    assert substract(2, 3) == -1
    assert substract(2, -3) == 5
    assert substract(-2, -3) == 1


def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(2, 3) == 6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6


def test_divide():
    assert divide(2, 2) == 1
    assert divide(2, 4) == 0.5
    assert divide(4, -2) == -2
    assert divide(-8, -2) == 4


def test_remainder():
    assert remainder(3, 2) == 1
    assert remainder(3, -2) == -1
    assert remainder(-19, 3) == 2
    assert remainder(-19, -3) == -1
