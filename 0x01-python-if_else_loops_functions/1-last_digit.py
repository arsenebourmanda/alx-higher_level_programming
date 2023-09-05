#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numLD = abs(number) % 10
if (number < 0):
    numLD = numLD * (-1)
print(f"Last digit of {number} is {numLD} and is", end=" ")
if (numLD > 5):
    print("greater than 5")
elif (numLD == 0):
    print("0")
elif (numLD < 6 and numLD != 0):
    print("less than 6 and not 0")
