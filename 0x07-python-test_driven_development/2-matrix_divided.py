#!/usr/bin/python3
"""This module defines a matrix_divided()"""


def matrix_divided(matrix, div):
    """This function divides each element of a list of matrix

        Args:
            matrix: the matrix to be divided by a number
            div: the number to divide the matrix
        Return:
            list of list: a new matrix which is the result of division
                of matrix by div rounded to 2 decimal places
    """
    new_matrix = []
    _typeError1 = "matrix must be a matrix (list of lists) of integers/floats"
    _typeError2 = "Each row of the matrix must have the same size"
    _typeError3 = "div must be a number"
    _zeroError = "division by zero"
    if not isinstance(matrix, list):
        raise TypeError(_typeError1)
    for n in matrix:
        if not isinstance(n, list):
            raise TypeError(_typeError1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            val = matrix[i][j]
            row_length = len(matrix[0])
            if len(matrix[i]) != row_length:
                raise TypeError(_typeError2)
            if not (isinstance(val, int) or isinstance(val, float)):
                raise TypeError(_typeError1)
    if div == 0:
        raise ZeroDivisionError(_zeroError)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(_typeError3)
    i = j = 0
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            element = round(matrix[i][j] / div, 2)
            row.append(element)
        new_matrix.append(row)
    return new_matrix
