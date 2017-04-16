def non_unique(data):
    """Find non unique elements in a list.

    Args:
        data [list]: A list of elements to check.
    Returns:
        A [list] containing only the elements which are non unique.

    For example:

    >>> non_unique([1, 2, 3, 1, 3])
    [1, 3, 1, 3]
    """
    return [letter for letter in data if data.count(letter) > 1]
