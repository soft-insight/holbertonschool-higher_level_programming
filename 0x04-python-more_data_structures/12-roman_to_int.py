#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or None:
        return 0
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = [roman_string[i] for i in range(len(roman_string))]
    integersRoman = [symbol.get(j) for j in roman]
    return sum(integersRoman)
