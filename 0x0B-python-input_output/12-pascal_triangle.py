#!/usr/bin/python3
"""defines triangle"""


def pascal_triangle(n):
    """represents triangle"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        t1 = [1]
        for j in range(len(t) - 1):
            t1.append(t[j] + t[j + 1])
        t1.append(1)
        triangles.append(t1)
    return triangles
