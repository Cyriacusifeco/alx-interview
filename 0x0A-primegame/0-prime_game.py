#!/usr/bin/python3
"""
A module that determines the winner of a primegame.
"""


def sieve_of_eratosthenes(n):
    """
    A function to effeciently find prime numbers up to n.
    """
    # Create a boolean array "prime[0..n]" and initialize
    # all entries as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = [i for i in range(2, n + 1) if prime[i]]
    return primes


def isWinner(x, nums):
    """
    A function that determines the winner of each game.
    """
    # Generate a list of prime numbers up to the maximum n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers less than or equal to n
        prime_count = len([p for p in primes if p <= n])

        # If the count is even, Ben wins. Otherwise, Maria wins.
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
