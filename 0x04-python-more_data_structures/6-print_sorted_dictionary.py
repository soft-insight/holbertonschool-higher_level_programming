#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    A = dict(sorted(a_dictionary.items()))
    for key, value in A.items():
        print(f"{key}: {value}")
