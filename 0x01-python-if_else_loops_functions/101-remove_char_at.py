#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    print("{}{}".format(str[:n], str[n+1:]))
