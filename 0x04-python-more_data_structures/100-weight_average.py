#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ars = 0
    bou = 0
    for elt in my_list:
        ars += elt[0] * elt[1]
        bou += elt[1]
    return (ars / bou)
