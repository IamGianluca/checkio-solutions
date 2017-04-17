import pytest

from checkio.elementary.index_power import index_power


class TestIndexPower:

    def test_square(self):
        assert index_power([1, 2, 3, 4], 2) == 9

    def test_cube(self):
        assert index_power([1, 3, 10, 100], 3) == 1000000

    def test_zero_power(self):
        assert index_power([0, 1], 0) == 1

    def test_index_error(self):
        assert index_power([1, 2], 3) == -1
