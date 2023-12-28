#!/usr/bin/python3
"""define class Base"""

import json
"""import json"""


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
