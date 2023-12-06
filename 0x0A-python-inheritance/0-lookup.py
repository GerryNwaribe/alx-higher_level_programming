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


def handle_int(self, value):
    print(f"Handling integer: {value}")


def handle_float(self, value):
    print(f"Handling float: {value}")


def handle_list(self, value):
    print(f"Handling list: {value}")


def handle_custom_class(self, value):
    if isinstance(value, MyClass):
        print("Handling an instance of MyClass")
        value.one_meth()
    else:
        print(f"Unknown custom class: {type(value)}")
    """case: int
    case: float
    case: list
    class MyClass(): def one_meth(self): pass pass"""
