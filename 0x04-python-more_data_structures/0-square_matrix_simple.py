#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix[0])
    b = len(matrix)
    A = [[matrix[j][i]**2 for i in range(a)] for j in range(b)]
    return A
