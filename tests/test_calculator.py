import pytest
from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_substract():
    assert subtract(3, 2) == 1
