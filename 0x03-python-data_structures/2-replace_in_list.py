#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    b = len(my_list)
    for a in my_list:
        if idx < 0:
            return my_list
        elif idx >= b:
            return my_list
        else:
            my_list[idx] = element
            return my_list
