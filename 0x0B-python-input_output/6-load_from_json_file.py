#!/usr/bin/python3
""" A function that creates an Object from a JSON object
"""


def load_from_json_file(filename):
    """Function to create a object form a JSON file
    """
    import json
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
