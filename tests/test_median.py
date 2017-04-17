import pytest

from checkio.oreilly.median import median


class TestMedian:

    def test_sorted_list(self):
        assert median([1, 2, 3, 4, 5]) == 3

    def test_non_sorted_list(self):
        assert median([3, 1, 2, 5, 3]) == 3

    def test_non_average(self):
        assert median([1, 300, 2, 200, 1]) == 2

    def test_even_length(self):
        assert median([3, 6, 20, 99, 10, 15]) == 12.5

    def test_long_range(self):
        assert median(list(range(1000000))) == 499999.5
