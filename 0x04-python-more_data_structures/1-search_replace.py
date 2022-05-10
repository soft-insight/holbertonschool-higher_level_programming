#!/usr/bin/python3
def search_replace(my_list, search, replace):
    A = my_list.copy()
    idx = [i for i in range(len(my_list)) if my_list[i] == search]
    for i in range(len(idx)):
        A[idx[i]] = replace
    return A
