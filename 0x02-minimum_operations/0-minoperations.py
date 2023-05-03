#!/usr/bin/python3

"""Module calculates the fewest number of operations"""

import math


def minOperations(n):
    """calculates the fewest number of operations"""
    if n <= 1:
        return 0
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    operations = 0
    current = 1
    for factor in factors:
        if factor == current:
            # multiply
            current *= factor
        else:
            # copy and paste
            operations += int(math.log2(current))
            current = factor
    # handle last factor
    operations += int(math.log2(current))
    return operations
