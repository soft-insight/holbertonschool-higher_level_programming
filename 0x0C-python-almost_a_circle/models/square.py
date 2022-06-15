#!/usr/bin/python3
""" class Square. Heritages from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Print a string format
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''getter size
        '''
        return self.width

    @size.setter
    def size(self, value):
        """Setter size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Args and kwargs
        """
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
