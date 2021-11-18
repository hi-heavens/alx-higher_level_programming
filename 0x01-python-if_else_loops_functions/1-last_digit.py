#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
    last_digit = last_digit
    comment1 = "Last digit of {} is {} {}"
else:
    last_digit = -number
    last_digit %= 10
    last_digit = -last_digit
    comment1 = "Last digit of {} is {} {}"

if last_digit > 5:
    comment2 = "and is greater than 5"
elif last_digit == 0:
    comment2 = "and is 0"
elif last_digit < 6 and last_digit != 0:
    comment2 = "and is less than 6 and not 0"

print(comment1.format(number, last_digit, comment2))
