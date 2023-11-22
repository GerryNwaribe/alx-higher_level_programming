#!/usr/bin/python3
"""define class square"""


class Square:
    """Attribute:
        size(int): size of square (Private instance attribute)
        Returns 0 if not specified"""
    def __init__(self, size=0):
        """Initialize square of any size
            Attribute:
                size(int): size of square (Private instance attribute)
                Returns 0 if no size
            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        """function to calculate area of a square
            Returns 0 if no size is given
            Returns area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """proprety to retrieve size
            Attribute:
                value(int): value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter
            Attribute:
                value(int): value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
