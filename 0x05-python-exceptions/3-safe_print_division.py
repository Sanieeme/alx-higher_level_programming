#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints results

    Args:
        a: integer
        b: integer

    Returns:
        results
    """
    nums = 0
    try:
        nums = a / b
    except ZeroDivisionError:
        nums = None
    finally:
        print("Inside result: {}". format(nums))
        return (nums)
