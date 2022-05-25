#!/usr/bin/python3
"""A class for Square"""


class Square:
    """
    constructor with optional private attribute @size.
    """
    def __init__(self, size = 0):
        """try / except TypeError, ValueError """
        
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
