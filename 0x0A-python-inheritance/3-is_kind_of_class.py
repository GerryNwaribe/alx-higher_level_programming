#!/usr/bin/python3
"""define is_kind_of_class funtion"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj (_type_):object
        a_class (_type_): class

    Returns:
        True if its and instance
        False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
