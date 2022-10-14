"Testing main.py"
import pytest
from app1 import main


@pytest.fixture(name="my_test_list")
def test_list():
    "test"
    my_test_list = ["dank", "memes", "melt", "steel", "beems", "yes", "yes"]
    return my_test_list


def test_check_duplicte(my_test_list):
    "Testing check_duplicate"
    # pylint: disable=E1101:no-member
    value = main.check_duplicate(my_test_list)

    assert value == "yes"
