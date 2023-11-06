#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    b = len(my_list) - 1
    for a in reversed(my_list):
        print("{:d}".format(a))
