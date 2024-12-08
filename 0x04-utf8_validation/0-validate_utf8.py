#!/usr/bin/python3
"""
UTF-8 Validation Problem
"""


def validUTF8(data):
    """Validates if data is a valid utf8-encoded data

    'data' is a list of integers, each of which represents
    a byte in the data sequence, with account for only the 8
    least significant bits
    """
    mask = 128
    temp = 0
    i = 0
    while i < len(data):
        following = 0
        temp = data[i]
        while temp & mask:
            following += 1
            temp = temp << 1
        if following > 4:
            return False
        elif following == 1:
            return False
        try:
            while (following - 1) > 0:
                i += 1
                following -= 1
                temp = data[i]
                j = 0
                while temp & mask:
                    temp = temp << 1
                    j += 1
                if j != 1:
                    return False
        except IndexError:
            return False
        i += 1
    return True
