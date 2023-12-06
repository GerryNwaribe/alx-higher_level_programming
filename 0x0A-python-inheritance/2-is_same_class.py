#!/usr/bin/python3
"""define is_same_class function"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an
    instance of the specified class,
    otherwise False

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
