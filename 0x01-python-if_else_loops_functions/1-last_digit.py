#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    n = abs(number) % 10
else:
    n = (abs(number) % 10) * -1
print('Last digit of {} is {} '.format(number, n), end='')
if n > 5:
    print('and is greater than 5')
elif (n < 6) and (n != 0):
    print('and is less than 6 and not 0')
else:
    print('and is 0')
