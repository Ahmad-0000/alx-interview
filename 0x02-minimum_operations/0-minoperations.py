#!/usr/bin/python3
"""
Minimum Operations Problem
"""


def is_prime(number):
    """Determining if a number is prime
    """
    if not number % 2 and number != 2:
        return False
    for i in range(3, number // 2, 2):
        if not number % i:
            return False
    return True

def minOperations(number):
    """Main function
    """
    primes = [2]
    if number <= 0:
        return 0
    if is_prime(number):
        return number
    for i in range(3, number // 2, 2):
        if i * i >= number:
            break
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
