#!/usr/bin/python3
"""define lookup function"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object

    Args:
        obj (_type_): list

    Returns: list object
    """
    attributes_and_methods = []

    for name in dir(obj):
        if not callable(getattr(obj, name)) or name.startswith("__"):
            attributes_and_methods.append(name)

    return attributes_and_methods
