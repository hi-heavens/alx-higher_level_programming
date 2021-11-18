#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{2:d} + {1:d} = {0:d}".format(add(a, b), b, a))
    print("{2:d} - {1:d} = {0:d}".format(sub(a, b), b, a))
    print("{2:d} * {1:d} = {0:d}".format(mul(a, b), b, a))
    print("{2:d} / {1:d} = {0:d}".format(div(a, b), b, a))
