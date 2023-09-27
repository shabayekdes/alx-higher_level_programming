#!/usr/bin/python3

def safe_print_integer(value):
    """safe print integer
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
