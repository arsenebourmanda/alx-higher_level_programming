#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numLD = abs(number) % 10
if (numLD > 5):
    print(f"Last digit of {number} is {numLD} and is greater than 5")
elif (numLD == 0):
    print(f"Last digit of {number} is {numLD} and is 0")
elif (numLD < 6 and numLD != 0):
    print(f"Last digit of {number} is {numLD} and is less than 6 and not 0")

