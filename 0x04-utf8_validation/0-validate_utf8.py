#!/usr/bin/python3
"""
UTF-8 Validation Problem
"""

def validUTF8(data):
    """Validates if data is a valid utf8-encoded data
    """
    for chunck in data:
        if chunck > 128:
            return False
        elif chunck < 0:
            return False
    return True
