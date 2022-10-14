"Testing main.py"
import os
import pytest
from app1 import new_main


@pytest.fixture(name="my_test_list")
def test_list():
    "Fixture of list"
    my_test_list = ["dog", "rabbit", "melt", "steel", "yEsterday", "yes"]
    return my_test_list


@pytest.fixture(name="my_test_list_no_repeating")
def test_list_no_repeat():
    "Fixture of list without repeating chars"
    my_test_list = ["dank", "yes"]
    return my_test_list


@pytest.fixture(name="my_test_words")
def test_words():
    "Fixture of txt file"
    file_name = "test_words.txt"
    directory = os.path.dirname(__file__)
    my_filename = os.path.join(directory, file_name)

    return my_filename


def test_check_longest(my_test_list):
    "Test check_longest"
    # pylint: disable=E1101:no-member
    value = new_main.check_longest(my_test_list)
    assert value.lower() == "yesterday"


def test_check_repeating(my_test_list, my_test_list_no_repeating):
    "Test check_repeating"
    # pylint: disable=E1101:no-member
    value = new_main.check_repeating(my_test_list)
    assert value == "FOUND"
    value = new_main.check_repeating(my_test_list_no_repeating)
    assert value == "NONE"


def test_format_lines():
    "Test format_lines"
    # pylint: disable=E1101:no-member
    str_rand = "TesT"
    str_lower = "test"
    str_upper = "TEST"
    value = new_main.format_lines(str_rand)
    assert value == "test"
    value = new_main.format_lines(str_lower)
    assert value == "test"
    value = new_main.format_lines(str_upper)
    assert value == "test"


def test_check_contents(my_test_list):
    "Test check_contents"
    # pylint: disable=E1101:no-member
    return_list = []
    value = new_main.check_contents(my_test_list, return_list)
    assert value == "melt"


def test_main(my_test_words):
    "Test main function"
    # pylint: disable=E1101:no-member
    value = new_main.main(my_test_words)
    assert value == "agile"
