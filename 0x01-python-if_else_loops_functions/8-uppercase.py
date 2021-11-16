#!/usr/bin/python3
def uppercase(str):
    str_length = len(str)
    for length in range(0, str_length):
        letter = str[length]
        conv = ord(letter)
        if conv >= 97 and conv <= 122:
            char = chr(conv - 32)
        else:
            char = str[length]
        print("{:c}".format(char), end="")
    print()
