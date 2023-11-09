#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if not my_list:
        return []

    result = list(map(lambda a: a * number, my_list))

    return result
