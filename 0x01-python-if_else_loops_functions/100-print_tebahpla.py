#!/usr/bin/python3
letter = 'z'

conv = ord(letter)

for alp in range(122, 96, -1) :
    if alp % 2 == 1:
        char = alp - 32
    else:
        char = alp
    print("{:c}".format(char), end="")
        
    conv -= 1
