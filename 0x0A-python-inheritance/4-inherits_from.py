#!/usr/bin/python3
"""define inherits_from function"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    otherwise False

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
