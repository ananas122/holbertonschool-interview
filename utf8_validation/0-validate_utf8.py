#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    nb_octets_restants = 0
    for nombre in data:
        if nb_octets_restants == 0:
            if (nombre >> 5) == 0b110:
                nb_octets_restants = 1
            elif (nombre >> 4) == 0b1110:
                nb_octets_restants = 2
            elif (nombre >> 3) == 0b11110:
                nb_octets_restants = 3
            elif (nombre >> 7):
                return False
        else:
            if (nombre >> 6) != 0b10:
                return False
            nb_octets_restants -= 1
    return nb_octets_restants == 0
