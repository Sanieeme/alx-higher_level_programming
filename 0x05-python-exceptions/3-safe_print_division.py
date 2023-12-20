#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints results

    Returns:
        num
    """
    try:
        nums = a / b
    except ZeroDivisionError:
        nums = None
    finally:
        print("Inside result: {}". format(nums))
        return (nums)
