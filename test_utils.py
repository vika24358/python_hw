import random

import pytest

from math_utils import add_two_numbers, get_two_time_string


def test_add_two_numbers():
    number1 = 2
    number2 = 3
    expected = 5.0
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected, 'Strange!'


def test_add_two_numbers_zero():
    number1 = 0
    number2 = 0
    expected = 0.0
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected, 'Strange!'


def test_add_two_numbers_negative():
    number1 = -10
    number2 = 9
    expected = -1
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected, 'Strange!'


testing_args = [(2, 3, 5.0),
                (0, 0, 0.0),
                (-10, 9, -1)]


@pytest.mark.parametrize('number1, number2, expected', testing_args)
def test_add_two_numbers_combined(number1, number2, expected):
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected, 'Strange!'


def test_add_two_numbers_random():
    number1 = random.randint(1, 10**10)
    number2 = random.randint(1, 10**10)
    actual_result = add_two_numbers(number1, number2)
    assert actual_result


class TestAddTwoNumbers:
    def test_add_two_numbers(self):
        number1 = 2
        number2 = 3
        expected = 5.0
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected, 'Strange!'

    def test_add_two_numbers_zero(self):
        number1 = 0
        number2 = 0
        expected = 0.0
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected, 'Strange!'

    def test_add_two_numbers_negative(self):
        number1 = -10
        number2 = 9
        expected = -1
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected, 'Strange!'

    testing_args = [(2, 3, 5.0),
                    (0, 0, 0.0),
                    (-10, 9, -1)]

    @pytest.mark.parametrize('number1, number2, expected', testing_args)
    def test_add_two_numbers_combined(self, number1, number2, expected):
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected, 'Strange!'

    def test_add_two_numbers_random(self):
        number1 = random.randint(1, 10 ** 10)
        number2 = random.randint(1, 10 ** 10)
        actual_result = add_two_numbers(number1, number2)
        assert actual_result


def test_new_func():
    given = 6
    actual_result = get_two_time_string
