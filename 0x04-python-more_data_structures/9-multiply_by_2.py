#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    A = a_dictionary.copy()
    for i in A:
        A.update({i: A[i]*2})

    return A
