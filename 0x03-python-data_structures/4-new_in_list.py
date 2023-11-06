#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        b = len(my_list) - 1
        cp_my_list = my_list[:]

        if idx < 0:
            return my_list[:]
        elif idx >= b:
            return my_list[:]
        else:
            cp_my_list = my_list[:]
            cp_my_list[idx] = element
            return cp_my_list
