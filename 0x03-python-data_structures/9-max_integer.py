#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None

    biggest = my_list[0]

    for a in my_list:
        if a > biggest:
            biggest = a
        else:
            return max(my_list)
