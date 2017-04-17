import pytest

from checkio.elementary.fizz_buzz import checkio


class TestFizzBuzz:

    def test_divisible_by_3_and_5(self):
        assert checkio(15) == "Fizz Buzz"

    def test_divisible_by_3(self):
        assert checkio(6) == "Fizz"

    def test_divisible_by_5(self):
        assert checkio(5) == "Buzz"

    def test_not_divisible_by_3_or_5(self):
        assert checkio(7) == "7"
