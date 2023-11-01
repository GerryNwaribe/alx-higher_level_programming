#!/usr/bin/python3
def print_last_digit(number):
    lst_digit = number % 10
    print("{}".format(lst_digit), end='')
    return (lst_digit)
