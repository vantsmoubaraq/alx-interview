#!/usr/bin/python3

"""Module solves lockboxes problem"""


def canUnlockAll(boxes):
    """Solves lockboxes problem"""
    opened = [False] * len(boxes)
    opened[0] = True

    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
