#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    b = len(my_list) - 1
    for a in range(b, -1, -1):
        print("{:d}".format(my_list[a]))
