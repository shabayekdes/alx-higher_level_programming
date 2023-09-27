#!/usr/bin/python3
def safe_function(fct, *args):
    """safe function
    """
    import sys

    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
