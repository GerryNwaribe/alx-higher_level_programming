 def __repr__(self):
        """Return a string representation of the object."""
        if self.__width == 0 or self.__height == 0:
            print()
        return f"Rectangle({self.__width}, {self.__height})"