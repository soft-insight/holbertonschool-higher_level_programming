#!/usr/bin/python3
""" add_integer: adds two integers.
    @a: int 1
    @b: int 2
    Floats are casted to integers.
"""


def add_integer(a, b=98):
    """
    function that adds two integers:
        * the default value of b is 98.
        * a doesn't have default value.
        * floats are converted to int:
            only the integer part of the float is consider.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
