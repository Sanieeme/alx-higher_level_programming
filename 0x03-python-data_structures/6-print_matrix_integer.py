#!/usr/bin/python30
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for n in matrix:
        if len(n) == 0:
            print()
        for num in range(len(n)):
            print("{:d}".format(n[num]), end="\n"if num is len(n) - 1 else " ")
