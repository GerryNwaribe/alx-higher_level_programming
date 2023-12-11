#!/usr/bin/python3
"""define class Base"""


class Base:
    """initializing class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int, None): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
