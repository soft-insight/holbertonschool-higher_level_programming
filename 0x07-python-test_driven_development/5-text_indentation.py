#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    indent after ., ?, or :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] in {'.', ':', '?'}:
            continue

        print(text[i], end='')
        if text[i] in {'.', ':', '?'}:
            print('\n')
