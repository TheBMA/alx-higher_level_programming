#!/usr/bin/python3
import random
number: int = random.randint(-10000, 10000)
if number == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    if number > 0:
        if (number % 10) == 0:
            print("Last digit of {} is 0 and is 0".format(number))
        elif (number % 10) > 5:
            print("Last digit of {} is {} and is greater than 5"
                  .format(number, (number % 10)))
        else:
            print("Last digit of {} is {} and is less than 6 and not 0"
                  .format(number, (number % 10)))
    else:
        temp = -number
        if (temp % 10) == 0:
            print("Last digit of {} is 0 and is 0".format(number))
        elif (temp % 10) > 5:
            print("Last digit of {} is -{} and is greater than 5"
                  .format(number, (temp % 10)))
        else:
            print("Last digit of {} is -{} and is less than 6 and not 0"
                  .format(number, (temp % 10)))
