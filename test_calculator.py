import pytest

from calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1, 2) == 3
    assert cal.add(2) == 5

def test_subtract():
    assert cal.subtract(5, 2) == 3
    assert cal.subtract(1) == 2

def test_multiplicate():
    assert cal.multiplicate(5, 2) == 10
    assert cal.multiplicate(3) == 30

def test_divide():
    assert cal.divide(30, 3) == 10
    assert cal.divide(5) == 2

def test_root():
    assert cal.root(4, 256) == 4
    assert cal.root(2) == 2

def test_memory_reset():
    cal.add(4, 5)
    cal.memory_reset()
    assert cal.memory == 0

def test_error_handling():
    assert cal.divide(5, 0) == "You cannot divide by zero!"