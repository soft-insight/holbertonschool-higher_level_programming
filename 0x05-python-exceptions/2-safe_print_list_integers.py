#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        my_list[x]
        j = 0
        for i in range(x + 1):
            try:
                print('este es j: ', j)
                print(int(my_list[i]))
                j += 1
            except ValueError:
                continue
        return j
    except IndexError:
        j = 0
        for i in my_list:
            try:
                print(int(i))
                j += 1
            except ValueError:
                continue
        return j
