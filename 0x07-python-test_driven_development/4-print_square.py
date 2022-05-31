#!/usr/bin/python3
"""
Function: print square with #
"""


def print_square(size):
    """
    print_square: prints to stdout a square of side 'size'
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        for i in range(size):
            print('#', end="")
        print()
