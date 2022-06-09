#!/usr/bin/python3
""" Function that returns the dictionary description
    with simple data structure or JSON serialization of an object
"""


def class_to_json(obj):
    '''Function that uses Dictionary description and JSON'''
    return obj.__dict__
