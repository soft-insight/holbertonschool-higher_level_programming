#!/usr/bin/python3
"""
Function that divides all elements of a matrix by a number.
Test by using this doctest
"""


def matrix_divided(matrix, div):
    """
    Function and exceptions of the
    matrix division by an escalar
    """

    if matrix == []:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    row = len(matrix)

    for i in range(row):
        if type(matrix[i]) is not list:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    for i in range(row):
        if matrix[i] == []:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    col = len(matrix[0])

    for i in range(row):
        if len(matrix[i]) != col:
            raise TypeError("Each row of the matrix must have the same size")

    A = []
    [A.append(matrix[i][j]) for i in range(row) for j in range(col)]

    if type(div) not in {int, float} or div == float('nan'):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(A)):
        if type(A[i]) not in {int, float}:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    B = []
    [B.append(round(i/div, 2)) for i in A]

    C = []
    while B != []:
        C.append(B[:col])
        B = B[col:]

    return C
