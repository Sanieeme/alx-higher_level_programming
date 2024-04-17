#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    i, j = 0, len(list_of_integers) - 1
    while i < j:
        k = (i + j) // 2
        if list_of_integers[k] < list_of_integers[k + 1]:
            i = k + 1
        else:
            j = k
    return list_of_integers[i]
