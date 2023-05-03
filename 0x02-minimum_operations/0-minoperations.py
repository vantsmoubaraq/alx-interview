#!/usr/bin/python3

"""Module calculates the fewest number of operations"""


def minOperations(n):
    """calculates the fewest number of operations"""
    copy_ops = 0
    paste_ops = 0

    if n <= 0 >= float("inf") or type(n) is not int:
        return 0

    while (n > 1):
        max_num = 0
        mod_list = []
        for i in range(1, n):
            if n % i == 0:
                mod_list.append(i)

        max_num = max(mod_list)
        copy_ops += 1
        paste_ops += ((n // max_num) - 1)

        n = max_num

    total = copy_ops + paste_ops
    return total
