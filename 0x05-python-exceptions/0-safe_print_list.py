#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        if x > 0 and my_list:
            for i in range(x):
                print(my_list[i], end="")
            print()
            return i + 1
    except IndexError:
        print()
    return i
