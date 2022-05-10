#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    
    A = my_list.copy()
    A[idx] = element
    return A