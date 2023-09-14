#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dossN = a_dictionary.copy()
    cleL = list(dossN.keys())
    for elt in cleL:
        dossN[elt] *= 2
    return (dossN)
