#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        number %= 10
        print(number, end="")
        return number
    else:
        number = -number
        number %= 10
        print(number, end="")
        return number