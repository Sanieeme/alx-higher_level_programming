#!/usr/bin/python3
def safe_print_integer(value):
    """prints integers
    Args:
        value: integer
    Return: error when falls
    """
    try:
        print("{:d} ".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
