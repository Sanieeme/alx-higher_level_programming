#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = list(map(lambda n: list(map(lambda x: x**2, n)), matrix))
    return (squares)
