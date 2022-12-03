#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reversed order."""
    if isinstance(my_list, list):
        my_list.reversed()
        for i in my_list:
            print("{:d}".format(i))
