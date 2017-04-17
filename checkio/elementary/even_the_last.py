

def checkio(array):
    """Sums even-indexes elements and multiply them at the last.

    Args:
        array [list]: The numbers we want to process.
    Returns:
        The sum of even-indexes elements, multiplied by the last
        element of the array [float].
    """
    if not array:
        return 0
    return sum(array[::2]) * array[-1]
