#!usr/bin/python3
""" from json to string
"""
import json


def to_json_string(my_obj):
    """ input an JSON object
        returns a string
    """
    return json.dumps(my_obj)
