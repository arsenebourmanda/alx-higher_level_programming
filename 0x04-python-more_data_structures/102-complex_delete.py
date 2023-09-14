#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cleL = list(a_dictionary.keys())
    for elt in cleL:
        if value == a_dictionary.get(elt):
            del a_dictionary[elt]
    return (a_dictionary)
