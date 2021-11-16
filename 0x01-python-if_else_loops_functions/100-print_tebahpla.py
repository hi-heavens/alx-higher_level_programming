#!/usr/bin/python3
letter = 'z'

conv = ord(letter)

for alp in range(122, 96, -1) :
    if alp % 2 == 1:
        print("{:c}".format(alp - 32), end="")
    else:
        print("{:c}".format(alp), end="")
        
    conv -= 1
