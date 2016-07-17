def checkio(array):
    """Sums even-indexes elements and multiply at the last.

    Args:
        array: An array containing the numbers we want to scan through.
    Returns:
        An integer value representin the sum of even-indexes elements,
        multiplied by the last element of the array.
    """

    if not array:
        return 0
    return sum(array[::2]) * array[-1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
