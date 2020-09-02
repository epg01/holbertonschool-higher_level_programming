#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Number_Last = int(str(number)[-1])
if number < 0:
    Number_Last *= -1

if Number_Last == 0:
    str1 = Number_Last
elif Number_Last > 5:
    str1 = "greater than 5"
elif Number_Last < 6:
    str1 = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, Number_Last, str1))
