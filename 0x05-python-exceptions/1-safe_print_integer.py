#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value in range(-9999, 9999):
            print("{:d}".format(value))
            print()
            return True
    except IndexError:
        return False
