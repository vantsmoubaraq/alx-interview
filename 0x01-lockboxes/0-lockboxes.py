#!/usr/bin/python3

"""Module solves lockboxes problem"""


def canUnlockAll(boxes):
    """Solves lockboxes problem"""
    opened = []
    added = 0

    for i in range(len(boxes[0])):
        if boxes[0][i] != 0:
            opened.append(boxes[0][i])
    return lookup(opened, boxes, added)


def lookup(opened_list, boxes, added):
    """Looks for keys"""
    staged_list = []
    for i in range(len(opened_list[added:])):
        staged_list.extend(boxes[opened_list[added:][i]])

    len_opened = len(opened_list)
    for key in staged_list:
        if key not in opened_list and 0 < key < len(boxes):
            opened_list.append(key)
    len_after = len(opened_list)
    added = len_after - (len_after - len_opened)

    if len_after == len_opened:
        if len(opened_list) + 1 == len(boxes):
            return True
        else:
            return False

    staged_list.clear()
    return lookup(opened_list, boxes, added)
