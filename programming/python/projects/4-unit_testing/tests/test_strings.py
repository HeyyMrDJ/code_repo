from src.strings.strings import *
import pytest

def test_upper():
    assert make_upper('test') == 'TEST'

def test_lower():
    assert make_lower('TEST') == 'test'