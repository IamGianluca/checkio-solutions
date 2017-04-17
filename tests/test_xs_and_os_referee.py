import pytest

from checkio.oreilly.xs_and_os_referee import checkio


class TestReferee:

    def test_xs_wins(self):
        assert checkio(['X.O', 'XX.', 'XOO']) == 'X'

    def test_os_wins(self):
        assert checkio(['OO.', 'XOX', 'XOX']) == 'O'

    def test_draw(self):
        assert checkio(['OOX', 'XXO', 'OXX']) == 'D'

    def test_xs_wins_again(self):
        assert checkio(['O.X', 'XX.', 'XOO']) == 'X'
