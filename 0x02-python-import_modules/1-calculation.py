#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{2:d} + {1:d} = {:d}".format(add(a, b), b, a))
    print("{2:d} - {1:d} = {:d}".format(sub(a, b), b, a))
    print("{2:d} * {1:d} = {:d}".format(mul(a, b), b, a))
    print("{2:d} / {1:d} = {:d}".format(div(a, b), b, a))
