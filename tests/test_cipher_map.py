import pytest

from checkio.home.cipher_map import recall_password


def test_first_example():
    # given
    grille = ('X...',
              '..X.',
              'X..X',
              '....')
    password = ('itdf',
                'gdce',
                'aton',
                'qrdi')

    # then
    assert recall_password(grille, password) == 'icantforgetiddqd'

def test_second_example():
    # given
    grille = ('....',
              'X..X',
              '.X..',
              '...X')
    password = ('xhwc',
                'rsqx',
                'xqzz',
                'fyzr')

    # then
    assert recall_password(grille, password) == 'rxqrwsfzxqxzhczy'
