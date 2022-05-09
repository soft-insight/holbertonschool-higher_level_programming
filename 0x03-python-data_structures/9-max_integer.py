#!/usr/bin/python3
def max_integer(my_list=[]):
    my_max = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > my_max:
            my_max = my_list[i]
    return my_max
