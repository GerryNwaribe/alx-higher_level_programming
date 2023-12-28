#!/usr/bin/python3
"""import base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square inheriting from rectangle

    Args:
        Rectangle (class): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """overloading __str__ method

        Returns:
             return [Square] (<id>) <x>/<y> - <size>
        """
        return (
                "[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size)
                )
