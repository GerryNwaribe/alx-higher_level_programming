#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    string_key = str(key)
    if string_key in a_dictionary:
        del a_dictionary[string_key]
    return a_dictionary
