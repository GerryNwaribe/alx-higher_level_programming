#!/usr/bin/python3
"""define class Rectangle"""


class Rectangle:
    """Define rectangle class
        number_of_instance increases for each rectangle created and decreases
        when a rectangle is deleted
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
            print_symbol - prints #
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """_summary_
            Returns area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """_summary_
            Returns perimeter of rectangle
        """
        result = (self.__width + self.__height) * 2
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return result

    def __str__(self):
        """Return a string representation of the rectangle."""
        list_var = []
        if self.__width == 0 or self.__height == 0:
            return list_var
        for a in range(self.__height):
            for b in range(self.__width):
                list_var.append(str(self.print_symbol))
            if a != self.__height-1:
                list_var.append('\n')
        return "".join(list_var)

    def __repr__(self):
        """Return a string representation of the object that
        can be used with eval()"""
        if self.__width == 0 or self.__height == 0:
            print()
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print message if rectangle instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
