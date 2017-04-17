

def index_power(array, n):
    """Find N-th power of the element with index N.

    Args:
        array [list]: The numbers that need to be scanned to find the N-th
        element.
        n [int]: The index of the element we want to raise to the power of N.
    Returns:
        The N-th power of the element in the array with the index N [int]. If
        *n* is outside of the array, then returns -1.
    """
    if len(array) > n:
        return array[n] ** n
    else:
        return -1
