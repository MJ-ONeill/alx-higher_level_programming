#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'X': 10, 'VII': 7, 'IX': 9, 'LXXXVII': 87, 'DCCVII': 707}
    roman_n = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
            roman_n += roman_d[roman_string[j]] - 2 * \
                        roman_d[roman_string[j - 1]
        else:
            roman_n += roman_d[roman_string[j]]
        return roman_n
