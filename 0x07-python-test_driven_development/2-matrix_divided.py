#!/usr/bin/python3
"""function to divide matrix"""


def matrix_divided(matrix, divisor):
    """matrix_divided:

    Args:
        matrix: List of lists representing a matrix of integers/floats
        divisor: Number to divide each elm in the matrix by

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: ach row of the matrix must have the same size
        TypeError: divisor must be a number
        ZeroDivisionError: division by zero

    Returns:
        Returns a new matrix with elms divided by the divisor.
    """
    num_columns = len(matrix[0])

    if any(not isinstance(elm, (int, float)) for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if any(len(row) != num_columns for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(divisor) not in (int, float):
        raise TypeError("divisor must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elm / divisor, 2) for elm in row] for row in matrix]

    return new_matrix
