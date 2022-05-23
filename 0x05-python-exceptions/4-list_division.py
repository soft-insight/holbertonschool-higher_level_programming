#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    A = []
    try:
        for i in range(list_length):
            try:
                A.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print('division by 0')
                A.append(0)
            except TypeError:
                print('wrong type')
                A.append(0)
    except IndexError:
        print('out of range')
    finally:
        return A
