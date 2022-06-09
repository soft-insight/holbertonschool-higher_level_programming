#!/usr/bin/python3
""" function that saves JSON to text file
"""


def save_to_json_file(my_obj, filename):
    """ input: JSON object
        filename: the file to write
    """
    import json
    jsonStr = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(jsonStr)
