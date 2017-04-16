import pytest

from home.non_unique_elements import non_unique


class TestNonUniqueElements:

    def test_list_output(self):
        assert isinstance(non_unique([1]), list)

    def test_simple_case(self):
        assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3]

    def test_all_uniques(self):
        assert non_unique([1, 2, 3, 4, 5]) == []

    def test_all_duplicates(self):
        assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

    def test_simple_case2(self):
        assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
