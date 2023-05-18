#!/usr/bin/python3

"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    state = 0
    for num in data:
        bit = 0b10000000
        if not state:
            while (bit & num):
                state += 1
                bit >>= 1
            if state > 4:
                return False
            if state:
                state -= 1
                if state == 0:
                    return False
    return not state
