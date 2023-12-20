#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        nums = a / b
    except ZeroDivisionError:
        nums = None
    finally:
        print("Inside result: {}". format(nums))
    return (nums)
