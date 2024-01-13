#!/usr/bin/python3
""" defines class"""


def inherits_from(obj, a_class):
    """returns True if the obj is instance of class that inherited
    (directly or indirectly).
    Args:
        obj: oject.
        a_class: class.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
