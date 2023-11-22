#!/usr/bin/python3
"""Defining class Square
    Attribute:
    size(int): size of square (Private instance attribute)
    Returns 0 if not soecified"""


class Square:
    def __init__(self, size=0):
        """Initialize square of any size
        Attribute:
            size(int): size of square (Private instance attribute)
        Returns 0 if no size
        Raises:
            TypeError: if size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
