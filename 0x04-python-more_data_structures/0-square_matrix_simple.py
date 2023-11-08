#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for a in matrix:
        new_a = []
        for b in a:
            square = b * b
            new_a.append(square)

        result.append(new_a)

    return result
