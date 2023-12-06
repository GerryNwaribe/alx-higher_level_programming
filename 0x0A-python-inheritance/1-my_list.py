#!/usr/bin/python3
"""Define Class MyList"""

class MyList:
    """class MyList that inherits from list"""
    def __init__(self):
        super().__init__()
        
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        sort_list = sorted(self)
        return sort_list
    