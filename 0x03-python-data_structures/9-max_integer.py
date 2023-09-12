#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    new = my_list[0]
    for elt in range(len(my_list)):
        if my_list[elt] > new:
            new = my_list[elt]
    return (new)
