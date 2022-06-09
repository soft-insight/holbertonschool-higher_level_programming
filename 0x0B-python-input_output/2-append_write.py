#!/usr/bin/python3
""" A function that appends a string
    to a text file
"""


def append_write(filename="", text=""):
    """ appends to a file
        if it doesn't exist, create it.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
