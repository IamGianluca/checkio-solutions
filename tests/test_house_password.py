import pytest

from checkio.deprecated.house_password import checkio


class TestHousePassword:

    def test_first(self):
        assert not checkio('A1213pokl')

    def test_second(self):
        assert checkio('bAse730onE4')

    def test_third(self):
        assert not checkio('asasasasasasasaas')

    def test_fourth(self):
        assert not checkio('QWERTYqwerty')

    def test_fifth(self):
        assert not checkio('123456123456')

    def test_sixth(self):
        assert checkio('QwErTy911poqqqq')
