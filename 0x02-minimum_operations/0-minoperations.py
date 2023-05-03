#!/usr/bin/python3

"""Module calculates the fewest number of operations"""

import math


def minOperations(n):
    """calculates the fewest number of operations"""
    if n < 1:
        return 0

    # Find the prime factorization of n
    factors = []
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    # Compute the minimum number of operations
    ops = 0
    prev_factor = None
    count = 0
    for factor in factors:
        if factor == prev_factor:
            count += 1
        else:
            ops += count + 1
            count = 1
            prev_factor = factor
    ops += count

    return ops
