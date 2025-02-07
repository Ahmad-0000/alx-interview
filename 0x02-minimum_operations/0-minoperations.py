#!/usr/bin/python3
"""
Minimum Operations Problem
"""

primes = [2]


def is_prime(number):
    """Determining if a number is prime
    """
    limit = number // 2
    if not number % 2 and number != 2:
        return False
    for i in range(3, limit, 2):
        if not number % i:
            return False
    return True


def minOperations(number):
    """Main function
    """
    limit = number // 2
    if number > 100000:
        limit = number // 400
    if number > 1000000000:
        limit = number // 100000
    if number <= 1:
        return 0
    if is_prime(number):
        return number
    for i in range(3, limit, 2):
        if is_prime(i):
            primes.append(i)
    total = 0
    i = 0
    while i < len(primes) and number > 0:
        if not number % primes[i]:
            total += primes[i]
            number /= primes[i]
            i = 0
            continue
        i += 1
    return total
