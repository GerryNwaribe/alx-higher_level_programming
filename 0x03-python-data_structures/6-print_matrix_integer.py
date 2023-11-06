#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b, c in enumerate(a):
            if b < len(a) - 1:
                print("{:d}".format(c), end=" ")
            else:
                print("{:d}".format(c), end="")
        print()
