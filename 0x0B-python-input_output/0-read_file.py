#!/usr/bin/python3
"""A function that reads a file
    and print to the stdout
"""


def read_file(filename=""):
    """ read a file to filename
        print to the stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
