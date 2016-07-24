def index_power(array, n):
    """Find N-th power of the element with index N.

    Args:
        array: An array of numbers we will scan to find the N-th element.
        n: The index of the element we want to raise to the power of N.
    Returns:
        The N-th power of the element in the array with the index N. If N is
        outside of the array, then return -1.
    """
    if len(array) > n:
        return array[n] ** n
    else:
        return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
