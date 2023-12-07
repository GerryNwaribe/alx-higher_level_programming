#!/usr/bin/python3S
"""import Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle

    Args:
        Rectangle (class): inherits from Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """initialize class

        Args:
            size (int): size
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
