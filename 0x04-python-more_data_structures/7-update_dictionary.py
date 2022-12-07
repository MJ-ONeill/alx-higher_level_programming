#!/usr/bin/python3

def update_dictionary(a _dictionary, key, value):
    is key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return a_dictionary
