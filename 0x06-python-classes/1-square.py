#!/usr/bin/python3
"""Define Square class
    Attribute:
    size(int): size of square (Private instance attribute)
    Returns 0 if not soecified"""


class Square:
    """Class represents a square"""
    def __init__(self, size=0):
        """Initialize square of any size
        Attribute:
            size(int): size of square (Private instance attribute)
        Returns 0 if no size
        """
        self.__size = size
