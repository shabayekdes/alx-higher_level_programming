#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """safe print of the list
    """
    if my_list is None or x < 0:
        return (0)
    count = 0
    try:
        while count < x:
            print("{}".format(my_list[count]), end="")
            count += 1
    except IndexError:
        print("")
        return (count)
    print("")
    return (count)
