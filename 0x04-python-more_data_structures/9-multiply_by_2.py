#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    lk = list(dictionary.keys())
    for n in lk:
        dictionary[n] *= 2
        return (dictionary)
