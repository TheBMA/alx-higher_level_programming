#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
            else:
                j += 1
                continue
    except (ValueError, TypeError):
        j += 1
        pass
    else:
        i += 1
    print()
    return i - j
