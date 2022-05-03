#!/usr/bin/python3
for i in range(0, 100):
    if len(str(i)) == 1:
        print(f'0{i}', end=', ')
    elif i == len(range(0, 100)) - 1:
        print(i)
    else:
        print(i, end=", ")
