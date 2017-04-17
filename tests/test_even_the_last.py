import pytest

from checkio.elementary.even_the_last import checkio


class TestEvenTheLast:

    def test_first(self):
        assert checkio([0, 1, 2, 3, 4, 5]) == 30

    def test_second(self):
        assert checkio([1, 3, 5]) == 30

    def test_third(self):
        assert checkio([6]) == 36

    def test_empty_array(self):
        assert checkio([]) == 0
