import random

import pytest

from testing_functions_homework import calculate_discount


class TestDiscount:

    test_args = [(100, 90, 10), (100, 30, 70), (100, 0, 100), (100, 0, 0)]

    @pytest.mark.parametrize('price, discount_percent, expected_result', test_args)
    def test_discount_regular(self, price, discount_percent, expected_result):
        actual_discount = calculate_discount(price, discount_percent)
        assert actual_discount

    def test_negative_discount(self):
        price = random.randint(0, 10**10)
        discount = random.randint(-100, -1)
        with pytest.raises(ValueError):
            actual_discount = calculate_discount(price, discount)
            assert actual_discount

    def test_too_big_discount(self):
        price = random.randint(0, 10**10)
        discount = random.randint(101, 10**10)
        with pytest.raises(ValueError):
            actual_discount = calculate_discount(price, discount)
            assert actual_discount

    def test_too_low_price(self):
        price = random.randint(-10**10, -1)
        discount = random.randint(1, 100)
        with pytest.raises(ValueError):
            actual_discount = calculate_discount(price, discount)
            assert actual_discount
