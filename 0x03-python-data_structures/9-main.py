#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [10000000, 90, 2, 13, 340, 5, -13, 30000]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
