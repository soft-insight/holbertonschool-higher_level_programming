#!/usr/bin/python3
""" class Square. Heritages from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square
    ... heritages from Rectangle
    ... same attributes with:
                size = with or height
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for Square """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Print a string format """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size attribute """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ *args and **kwargs """

        lst = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns a dict of attributes
            this allows to enter as **kwards to update
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
            }
