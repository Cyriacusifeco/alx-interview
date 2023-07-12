#!/usr/bin/python3
"""
Algorithm to find minimum number of operations
"""


def minOperations(n):
    """
    Returns the number of operations. The algorithm
    essentially sums all the prime factorizations of n.
    Remember: One is not a prime number.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n = n // divisor
        else:
            divisor += 1

    return operations
