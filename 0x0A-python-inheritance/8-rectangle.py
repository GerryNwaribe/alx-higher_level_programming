#!/usr/bin/python3
"""define class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def __init__(self):
        """initialize"""

    def area(self):
        """ raises an Exception with the
        message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value

        Args:
            name (str): string
            value (int): _description_
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """class Rectangle that inherits from BaseGeometry

        Args:
            width (int): width
            height (int): height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
