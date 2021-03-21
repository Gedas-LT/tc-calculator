import pytest

from calculator import Calculator

cal = Calculator()

def test_add():
    # Check if result of addition is correct.
    assert cal.add(1, 2) == 3
    assert cal.add(2) == 5

def test_subtract():
    # Check if result of subtraction is correct.
    assert cal.subtract(5, 2) == 3
    assert cal.subtract(1) == 2

def test_multiplicate():
    # Check if result of multiplication is correct.
    assert cal.multiplicate(5, 2) == 10
    assert cal.multiplicate(3) == 30

def test_divide():
    # Check if result of division is correct.
    assert cal.divide(30, 3) == 10
    assert cal.divide(5) == 2

def test_root():
    # Check if result of root is correct.
    assert cal.root(4, 256) == 4
    assert cal.root(2) == 2

def test_memory_reset():
    # Check memory reseting.
    cal.add(4, 5)
    cal.memory_reset()
    assert cal.memory == 0

def test_error_handling():
    # Check error handling.
    assert cal.divide(5, 0) == "You cannot divide by zero!"