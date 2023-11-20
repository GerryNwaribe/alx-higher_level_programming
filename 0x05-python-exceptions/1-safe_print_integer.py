#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int_val = int(value)
        print("{:d}".format(value))
        print()
        return True
    except (ValueError, TypeError):
        return False
