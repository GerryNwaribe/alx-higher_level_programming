#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for a in sort:
        value = a_dictionary[a]
        print("{}: {}".format(sort, value))
