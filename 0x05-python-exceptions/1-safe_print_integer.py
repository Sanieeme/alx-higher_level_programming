#!/usr/bin/python3

def safe_print_integer(value):
    """prints integers
    Args:
        value: integer
    Return:
        False: TypeError or ValueError
        True: no error
    """
    try:
        print("{:d} ".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
