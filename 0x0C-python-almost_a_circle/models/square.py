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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """*args is the list of arguments - no-keyworded arguments
            **kwargs can be thought of as a
            double pointer to a dictionary: key/value
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """define function

        Returns:
            returns the dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """overloading __str__ method

        Returns:
             return [Square] (<id>) <x>/<y> - <size>
        """
        return (
                "[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size)
                )
