#!/usr/bin/python3

"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    minimum = 2 ** (-8)
    maximum = (2 ** 8) - 1

    for item in data:
        if item < minimum or item > maximum:
            return False
    return True
