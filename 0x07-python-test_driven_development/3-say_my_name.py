#!/usr/bin/python3

"""

This module contains a function that prints a name

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name> <last name>)

    Args:
        first_name (str): The first name to be printed
        last_name (str): The last name to be printed

    Raises:
        TypeError: If either the first_nmae and last_name are n ot strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
