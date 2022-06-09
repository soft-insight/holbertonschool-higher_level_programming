#!/usr/bin/python3
""" function that saves JSON to text file
"""


import json


def save_to_json_file(my_obj, filename):
    """ input: JSON object
        filename: the file to write
    """
    with open(filename, 'w', encoding='utf-8') as f:
        jsonStr = json.dumps(my_obj)
        f.write(jsonStr)
