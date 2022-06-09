#!/usr/bin/python3
""" A function that writes a string
    to a text file
"""


def write_file(filename="", text=""):
    """ write to a file
        if it doesn't exist, create it.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
