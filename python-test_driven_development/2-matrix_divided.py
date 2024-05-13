#!/usr/bin/python3
"""Includes a function that divides all
   elements of a matrix. """


def matrix_divided(matrix, div):
    """Divides all elements of a matrix:
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats

    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message
    Each row of the matrix must have the same size

    div must be a number (integer or float), otherwise raise
    a TypeError exception with the message div must be a number

    div cant be equal to 0, otherwise raise a ZeroDivisionError 
    exception with the message division by zero

    All elements of the matrix should be divided by
    div, rounded to 2 decimal places

    Returns a new matrix"""

    row_length = len(matrix[0])

    for row in matrix:
        for element in row:
            if (( not isinstance(element, int)) and (not isinstance(element, float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = []

    for row in matrix:
        divided_row = []
        for divided in row:
            divided_row.append(divided / div)
        divided_matrix.append(divided_row)

    return divided_matrix
            
