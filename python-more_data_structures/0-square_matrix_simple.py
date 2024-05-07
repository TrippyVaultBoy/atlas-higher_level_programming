#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squares = []
    for rows in matrix:
        row = []
        for element in row:
            row.append(element ** 2)
        squares.append(row)
    return squares
