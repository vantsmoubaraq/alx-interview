#!/usr/bin/python3

"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for item in data:
        left_most_bit = (item >> 7) & 1
        if left_most_bit == 1:
            return False
    return True