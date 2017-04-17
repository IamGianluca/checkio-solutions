import pytest

from checkio.home.pawn_brotherhood import safe_pawns


class TestPawnBrotherhood:

    def test_first(self):
        assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6

    def test_second(self):
        assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    def test_third(self):
        assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 7

    def test_fourth(self):
        assert safe_pawns({"a8","b7","c6","d5","e4","f3","g2","h1"}) == 7
