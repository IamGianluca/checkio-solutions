import pytest

from checkio.deprecated.most_wanted_letter import checkio


class TestMostWantedLetter:

    def test_first(self):
        assert checkio("Hello World!") == "l"

    def test_second(self):
        assert checkio("How do you do?")  == "o"

    def test_third(self):
        assert checkio("One") == "e"

    def test_fourth(self):
        assert checkio("Oops!") == "o"

    def test_fifth(self):
        assert checkio("AAaooo!!!!") == "a"

    def test_sixth(self):
        assert checkio("abe") == "a"

    def test_seventh(self):
        assert checkio("a" * 9000 + "b" * 1000) == "a"
