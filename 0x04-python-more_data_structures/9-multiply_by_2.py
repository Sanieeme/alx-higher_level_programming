#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    lk = list(b_dictionary.keys())
    for n in lk:
        b_dictionary[n] *= 2
    return (b_dictionary)
