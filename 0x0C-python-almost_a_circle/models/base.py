#!/usr/bin/python3
""" The base class
"""
from os import path
import json


class Base:
    """class Base
        attribute: id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""

        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation
            list dict
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file the JSON string representation
            of list objects
        """

        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(
                [cls.to_dictionary(x) for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ from JSON to string
        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        ... create dictionary
        """

        if cls.__name__ == 'Square':
            dummy = cls(1)

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
