#!/usr/bin/python3
"""
Prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`
"""


def text_indentation(text):
    """
    Prints a text with indentation
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    i = 0
    new_string = ''
    starting = True

    while i < len(text):
        if text[i] == ' ' and starting is True:
            i += 1
            continue

        starting = False

        if text[i] in {'.', '?', ':'}:
            new_string += text[i]
            new_string += '\n'
            new_string += '\n'
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1

            continue

        if i < len(text):
            new_string += text[i]
            i += 1

    print(new_string, end='')
