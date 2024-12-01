#!/usr/bin/python3
"""
LockBoxes problem
"""


def canUnlockAll(boxes):
    """Checks if "boxes" can be unlocked
    """
    open_boxes_set = set(boxes[0])
    temp_set = open_boxes_set.copy()
    for i in range(len(boxes)):
        for key in temp_set:
            try:
                for j in boxes[key]:
                    open_boxes_set.add(j)
            except IndexError:
                pass
        for k in open_boxes_set:
            temp_set.add(k)
    for i in range(1, len(boxes)):
        if i not in open_boxes_set:
            return False
    return True
