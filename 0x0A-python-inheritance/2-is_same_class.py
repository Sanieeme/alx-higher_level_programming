#!/usr/bin/python3
"""defines a class"""


def is_same_class(obj, a_class):
    """returns true or false.
    Args:
        obj: object.
        a_class: class.
    Return: true or false
    """
    if type(obj) == a_class:
        return (True)
    return (False)
