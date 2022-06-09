#!/usr/bin/python3
"""
Function that generates a list of list
with the coeficients of the binomial expansion
"""


def pascal_triangle(n):
    """
    Pascal triangle
    @n: input the n - 1 expansion
    Returns: list of lists
    """
    if n <= 0:
        return []
    A = [1]
    C = []
    for k in range(n):
        B = []
        B.append(1)
        [B.append(A[i] + A[i+1]) for i in range(len(A) - 1)]
        B.append(1)
        C.append(A)
        A = B
    return (C)
