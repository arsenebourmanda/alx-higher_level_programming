#!/usr/bin/python3
for numbA in range(0, 10):
    for numbB in range(numbA + 1, 10):
        if numbA == 8 and numbB == 9:
            print("{}{}".format(numbA, numbB))
        else:
            print("{}{}".format(numbA, numbB), end=", ")
