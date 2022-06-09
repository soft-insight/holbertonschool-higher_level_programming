#!/usr/bin/python3
"""From a class to JSON
"""


class Student():
    """class: Student"""

    def __init__(self, first_name, last_name, age):
        """ attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary of Student"""
        return self.__dict__
