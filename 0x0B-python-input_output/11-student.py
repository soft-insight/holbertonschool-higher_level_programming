#!/usr/bin/python3
""" Class Student that defines a student
"""


class Student:
    """ Description of a student
    """

    def __init__(self, first_name, last_name, age):
        '''Student contructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Dictionary representation of a student'''
        if type(attrs) is list:
            d = self.__dict__
            return(dict(
                ([name, value] for name, value in d.items() if name in attrs)))
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all items in Json"""

        for i in json.keys():
            self.__dict__[i] = json[i]
