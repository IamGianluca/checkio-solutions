import pytest

from checkio.electronic_station.the_longest_palindromic import \
        longest_palindromic


class TestLongestPalindromic:

    def test_longest(self):
        assert longest_palindromic("artrartrt") == "rtrartr"

    def test_first(self):
        assert longest_palindromic("abacada") == "aba"

    def test_the_a(self):
        assert longest_palindromic("aaaa") == "aaaa"

    def test_non_palindrome(self):
        assert longest_palindromic("abc") == "a"
