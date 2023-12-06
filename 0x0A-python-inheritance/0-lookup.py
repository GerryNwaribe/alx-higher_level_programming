#!/usr/bin/python3
"""define lookup function"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object

    Args:
        obj (_type_): list

    Returns: list object
    """
    return dir(obj)

    """dir() - gets list of attributes of an object"""
