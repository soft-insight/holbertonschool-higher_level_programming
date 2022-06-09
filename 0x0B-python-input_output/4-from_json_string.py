#!/usr/bin/python3
""" from strin to JSON object
"""


def from_json_string(my_str):
    """ imput a string
        returns a JSON object
    """
    import json
    return json.loads(my_str)
