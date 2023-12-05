#!/usr/bin/python3
def lookup(obj):
    attributes_and_methods = []

    for name in dir(obj):
        if not callable(getattr(obj, name)) or name.startswith("__"):
            attributes_and_methods.append(name)

    return attributes_and_methods
