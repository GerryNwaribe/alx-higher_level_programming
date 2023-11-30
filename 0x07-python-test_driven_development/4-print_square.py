#!/usr/bin/python3
"""function prints # as square"""


def print_square(size):
    """define print_square function

    Args:
        size (int): size of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for a in range(size):
        print('#' * size)
