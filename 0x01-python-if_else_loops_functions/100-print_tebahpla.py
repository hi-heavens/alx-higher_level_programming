#!/usr/bin/python3
letter = 'z'

conv = ord(letter)

while conv > 96:
    if(conv % 2 == 1):
        char = conv - 32
    else:
        char = conv
    print("{:c}".format(char), end="")
        conv -= 1
