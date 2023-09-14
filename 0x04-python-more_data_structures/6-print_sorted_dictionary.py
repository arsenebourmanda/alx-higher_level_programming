#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordreL = list(a_dictionary.keys())
    ordreL.sort()
    for elt in ordreL:
        print("{}: {}".format(elt, a_dictionary.get(elt)))
