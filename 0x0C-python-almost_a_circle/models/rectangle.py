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

    def area(self):
        """funtion for area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        for b in range(self.y):
            print()

        for a in range(self.__height):
            print(" " * self.x, end='')
            print('#' * self.__width)

    def update(self, *args):
        """function that assigns an argument to each attribute"""
        att = ["id", "width", "height", "x", "y"]

        for a in range(len(args)):
            if a < len(att):
                setattr(self, att[a], args[a])

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for x."""
        return self.__y

    @y.setter
    def y(self, value):
        """Getter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """Getter method for id."""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter method for id."""
        if value < 0:
            raise ValueError("id must be > 0")
        self.__id = value

    def __str__(self):
        return (
                "[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height)
                )
