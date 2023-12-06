#!/usr/bin/python3
"""Define Class MyList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

    '''def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        sort_list = sorted(self)
        for a in sort_list:
            print(a)'''
