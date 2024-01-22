#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if (i != j) and (i*j != 72):
            print("{:d}{:d}".format(i, j), end= ", ")
print("89")
