#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 0:
        return (None)
    large = my_list[0]
    for n in my_list:
        if n > large:
            large = n
    return (large)
