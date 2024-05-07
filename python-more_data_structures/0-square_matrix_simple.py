#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        row = []
        for element in row:
            row.append(element ** 2)
        squares.append(row)
    return squares
