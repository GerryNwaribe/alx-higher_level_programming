def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: Peak value found in the list.

    """
    n = len(list_of_integers)

    if n == 0:
        return None

    if n == 1:
        return list_of_integers[0]

    mid = n // 2
    _md = list_of_integers[mid]
    _previous = list_of_integers[mid - 1]

    if (mid == 1):
        return (_md if _md > _previous else  _previous)

    # Check if the middle element is a peak
    _next = list_of_integers[mid + 1]
    if (mid == 0 or _md >= _previous) and (mid == n - 1 or _md >= _next):
        return _md

    # If the middle element is not a peak, recursively search in the left and right halves
    if mid > 0 and _previous > _md:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
    