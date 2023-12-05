#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for n in matrix:
        if len(n) == 0:
            print()
