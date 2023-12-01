#!/usr/bin/python3
"""function that adds integers"""


def add_integer(a, b=98):
    """Define add integer function

    Args:
        a (int, float): integer to add
        b (int, float): integer to add. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
