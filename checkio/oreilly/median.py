

def median(data):
    """Compute the median.

    Args:
        data [list]: The list of elements we want to use to compute the median.
    Returns:
        The median [float].
    """
    ordered = sorted(data)
    offset = len(ordered) // 2
    sum_of_central_elements = ordered[offset] + ordered[-(offset + 1)]
    return sum_of_central_elements / 2
