#!usr/bin/python3
""" from json to string
"""


def to_json_string(my_obj):
    """ input an JSON object
        returns a string
    """
    import json
    return json.dumps(my_obj)
