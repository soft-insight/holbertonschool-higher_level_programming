#!/usr/bin/python3
""" A class for a Square"""


class Square:
    """
    constructor for class Square with optional size
    """
    def __init__(self, size=0):
        """Validates size as integer and greater than zero"""
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """this public method returns the area from private size"""
        return self.__size ** 2
