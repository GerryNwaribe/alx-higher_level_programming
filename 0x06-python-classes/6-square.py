#!/usr/bin/python3
"""define class square"""


class Square:
    """Attribute:
        size(int): size of square (Private instance attribute)
        Returns 0 if not specified"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square of any size
            Attribute:
                size(int): size of square (Private instance attribute)
                Returns 0 if no size
            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """function to print square with # char"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """property to retrive position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter
            Attribute:
            value(int): value of size"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
