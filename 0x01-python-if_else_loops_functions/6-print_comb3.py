#!/usr/bin/python3
for num in range(10):
    for i in range((num + 1), 10):
        if num == 8 and i == 9:
            print("{:d}{:d}".format(num, i))
        else:
            print("{:d}{:d},".format(num, i), end=" ")
