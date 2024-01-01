#!/usr/bin/python3
"""define class Base"""

import json
"""import json"""
import csv
"""import csv"""

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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        dict_list = list(map(lambda obj: obj.to_dictionary(), list_objs))
        json_string = cls.to_json_string(dict_list)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """define function
        Args:
            json_string (_type_): string representing
            a list of dictionaries

        Returns:
            returns the list of
            the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            instance: Instance with attributes set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
    
    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file.

        Returns:
            list: List of instances.
        """
        class_name = cls.__name__
        filename = f"{class_name}.csv"

        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                instances = []
                for row in csv_reader:
                    if class_name == 'Rectangle':
                        instances.append(cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]),
                                                    x=int(row[3]), y=int(row[4])))
                    elif class_name == 'Square':
                        instances.append(cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])))
                return instances
        except FileNotFoundError:
            return []
