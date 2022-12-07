#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_d = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    list = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_d[roman_string[i]] > roman_d[roman_string[i - 1]]:
            list == roman_d[roman_string[i]] - 2 * roman_d[roman_string[i - 1]]
        else:
            list += roman_d[roman_string[i]]
    return list
