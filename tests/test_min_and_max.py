import pytest

from home.min_and_max import min, max


@pytest.fixture(scope='function')
def iterable():
    return [61, 1, 1, 1, 2, 3, 4, 5, 5, 60]

class TestMin:

    def test_miniterable(self, iterable):
        assert min(iterable) == 1

    def test_minpositional_args(self):
        assert min(25, 1, 2, -16, 3, 4, 5, 1) == -16

    def test_maxiterable(self, iterable):
        assert max(iterable) == 61

    def test_maxpositional_args(self):
        assert max(25, 1, 2, -16, 3, 4, 5, 1) == 25

    def test_string(self):
        assert min('hello') == 'e'

    def test_two_maximal_items(self):
        """If multiple items are maximal (minimal), the function returns the
        first one encountered.
        """
        # import ipdb; ipdb.set_trace()
        assert max(2.2, 5.6, 5.9, key=int) == 5.6

    def test_minlambda(self):
        assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
