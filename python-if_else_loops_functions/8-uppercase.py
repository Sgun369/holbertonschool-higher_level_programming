#!/usr/bin/python3
def uppercase(str):
    up = ""
    for char in str:
        if 'a' <= char <= 'z':
            upchar = chr(ord(char) - 32)
        else:
            upchar = char
        up += upchar
    print("{}".format(up))

