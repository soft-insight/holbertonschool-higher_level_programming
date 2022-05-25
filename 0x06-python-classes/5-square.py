#!/usr/bin/python3
"""
A class Square:
    * accessing to private attibute.
    * raise exception if __size < 0 or not an int
    * @properties
"""


class Square:
    """A class for  a square,
        with two methods:
        - constructor with private attibute __size
        - and the area
    """

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
