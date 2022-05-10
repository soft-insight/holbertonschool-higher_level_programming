#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    A = [[matrix[j][i]**2 for i in range(len(matrix[0]))] for j in range(len(matrix))] 
    return A
