#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    A = list(a_dictionary.values())
    return list(a_dictionary.keys())[A.index(max(A))]


