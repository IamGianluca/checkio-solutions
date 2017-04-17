import pytest

from checkio.deprecated.moore_neighbourhood import count_neighbours


class TestMooreNeighbours:

    def test_first(self):
        grid = ((1, 0, 0, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 1),
                (1, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),)
        assert count_neighbours(grid, 1, 2) == 3

    def test_second(self):
        grid = ((1, 0, 0, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 1),
                (1, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),)
        assert count_neighbours(grid, 0, 0) == 1

    def test_third(self):
        grid = ((1, 1, 1),
                (1, 1, 1),
                (1, 1, 1),)
        assert count_neighbours(grid, 0, 2) == 3

    def test_fourth(self):
        grid = ((0, 0, 0),
                (0, 1, 0),
                (0, 0, 0),)
        assert count_neighbours(grid, 1, 1) == 0
