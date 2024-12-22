#!/usr/bin/python3
"""
Coins problem
"""


def makeChange(coins, total):
    """The solution"""
    if not coins:
        return -1
    if total <= 0:
        return 0
    coins.sort()
    answer = []
    while total > 0:
        i = 0
        while i != len(coins) and total >= coins[i]:
            i += 1
        i -= 1
        total -= coins[i]
        answer.append(coins[i])
    if total == 0:
        return len(answer)
    return -1
