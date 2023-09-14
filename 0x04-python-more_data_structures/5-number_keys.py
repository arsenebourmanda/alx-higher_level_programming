#!/usr/bin/python3
def number_keys(a_dictionary):
    valeur = 0
    cleL = list(a_dictionary.keys())
    for elt in cleL:
        valeur += 1
    return (valeur)
