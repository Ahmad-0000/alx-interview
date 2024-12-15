#!/usr/bin/python3
"""
I don't know why do I assigned these problems
"""


def get_primes(n):
    """Getting the prime numbers in the range from 2 to n
    """
    if n < 2:
        return []
    primes = [True for _ in range(n + 1)]
    i = 2

    while i * i <= n:
        if primes[i]:
            for _ in range(i * i, n + 1, i):
                primes[_] = False
        i += 2
    i = 2
    while i < n + 1:
        if primes[i]:
            primes[i] = i
        i += 1
    primes = [i for i in primes if i]
    return primes


def isWinner(x, nums):
    """To determine who is the winner
    """
    if x < 1:
        return "Ben"
    M = 0
    B = 0
    for _ in range(x):
        primes = get_primes(nums[_])
        if primes == []:
            B += 1
        else:
            D = 0
            while primes:
                primes.pop()
                D += 1
            if D % 2:
                M += 1
            else:
                B += 1
    return "Ben" if B > M else "Maria"
