#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        a_dictionary.update({i: a_dictionary[i]*2})

    print(a_dictionary)
