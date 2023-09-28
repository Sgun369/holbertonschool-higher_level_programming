#!/usr/bin/python3
for f in range(10):
    for s in range(1 + f, 10):
        if f == 8 and s == 9:
            print("{}{}".format(f, s))
        else:
            print("{}{}".format(f, s), end=", ")
