#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tup in my_list:
        average += tup[1]
    return float(average / div)
