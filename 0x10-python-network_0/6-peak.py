#!/usr/bin/python3
"""Define function"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search algorithm.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: The peak value found in the list. If there are multiple peaks, any peak value can be returned.
             If the list is empty, returns None.
    """
    n = len(list_of_integers)

    if n == 0:
        return None

    if n == 1:
        return list_of_integers[0]

    left = 0
    right = n - 1

    while left < right:
        mid = left + (right - left) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
