#!/usr/bin/python3
""" Rectangle heritage from Base class
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor of the Rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attribute(value, 'width')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attribute(value, 'height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attribute(value, 'x')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attribute(value, 'y')
        self.__y = value

    def area(self):
        return self.width * self.height

    def __str__(self):
        s1 = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        s2 = f"- {self.width}/{self.height}"
        return s1 + s2

    def display(self):
        """ print strings for the rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """ *args and **kwargs
        """
        lst = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns a dict of the attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }

    @staticmethod
    def validate_attribute(value, attribute):
        """ function in static method to validate attributes
        """
        if type(value) is not int:
            raise TypeError(attribute + ' must be an integer')

        if value <= 0 and attribute in ('width', 'height'):
            raise ValueError(attribute + ' must be > 0')

        if value < 0 and attribute in ('x', 'y'):
            raise ValueError(attribute + ' must be >= 0')
