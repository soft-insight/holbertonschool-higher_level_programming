#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        A = list(a_dictionary.values())
        return [k for k, v in a_dictionary.items() if v == max(A)][0]
