#!/usr/bin/python3
"""
Coins problem
"""


def makeChange(coins, target):
    """The solution"""
    coins.sort()
    answer = []
    while target > 0:
        i = 0
        while i != len(coins) and target >= coins[i]:
            i += 1
        i -= 1
        target -= coins[i]
        answer.append(coins[i])
    if target == 0:
        return len(answer)
    return -1
