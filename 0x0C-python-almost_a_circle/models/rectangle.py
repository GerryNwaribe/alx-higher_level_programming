#!/usr/bin/python3
"""import base"""
from models.base import Base


class Rectangle(Base):
    """define class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (int): width
            height (int): height
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    width.setter

    def width(self, value):
        """Setter method for width."""
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    height.setter

    def height(self, value):
        """Setter method for height."""
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    x.setter

    def x(self, value):
        """Setter method for x."""
        self.__x = value

    @property
    def y(self):

        return self.__y

    y.setter

    def y(self, value):
        """Getter method for y."""
        self.__y = value

    @property
    def id(self):
        """Getter method for id."""
        return self.__id

    id.setter

    def id(self, value):
        """Setter method for id."""
        self.__id = value
