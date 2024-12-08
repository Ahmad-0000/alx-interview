#!/usr/bin/python3
"""
UTF-8 Validation Problem
"""


def validUTF8(data):
    """Validates if data is a valid utf8-encoded data
    """
    for chunck in data:
        chunck = chunck >> 7
        if chunck & 1:
            return False
    return True
