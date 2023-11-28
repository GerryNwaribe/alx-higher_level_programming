#!/usr/bin/python3
"""define class Rectangle"""


class Rectangle:
    """Define rectangle class"""
    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """_summary_
        Returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (int): value of size
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """_summary_
        Returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (int): value of size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
