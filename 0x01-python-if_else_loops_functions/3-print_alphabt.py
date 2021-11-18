#!/usr/bin/python3

for alpha in range(ord('a'), 123):
    if alpha == ord('q') or alpha == ord('e'):
        continue
    print("{:c}".format(alpha), end="")
