from src.math.math import *
import pytest

def test_add_numbers():
    assert add_numbers(10, 5) == 15

def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5