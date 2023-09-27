#!/usr/bin/python3


def safe_print_division(a, b):
    """safe print division
    """
    result = None
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except:
        print("Inside result: {}".format(result))
    finally:
        return result
