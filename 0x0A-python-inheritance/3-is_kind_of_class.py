#!/usr/bin/python3
"""defines class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of class.
    Args:
        obj: object.
        a_class: class.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
