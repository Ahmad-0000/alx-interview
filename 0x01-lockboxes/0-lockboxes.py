#!/usr/bin/python3
"""
LockBoxes problem
"""


def canUnlockAll(boxes):
    """Checks if "boxes" can be unlocked
    """
    open_boxes_keys = set(boxes[0])
    temp_set = set(boxes[0])
    for box_idx, box in enumerate(boxes):
        if box_idx not in temp_set:
            pass
        else:
            for new_key in box:
                open_boxes_keys.add(new_key)
                if new_key < box_idx and new_key not in temp_set:
                    try:
                        previous_box = boxes[new_key].copy()
                        for k in previous_box:
                            open_boxes_keys.add(k)
                    except IndexError:
                        pass
        temp_set = open_boxes_keys.copy()
    for i in range(1, len(boxes)):
        if i not in open_boxes_keys:
            return False
    return True
