#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3, 2],
    [4, 5, 6, -1],
    [7, 8, 9, 0]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
