#!/usr/bin/python3
"""
Returns the name of the player that won the most
rounds or None if the winner cannot be determined
"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of a game where two players take turns
    choosing a prime number from a set of consecutive integers starting from 1
    up to and including n. The player that cannot make a move loses the game.
    """
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(max_num):
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= max_num:
            if primes[p]:
                for i in range(p * p, max_num + 1, p):
                    primes[i] = False
            p += 1
        return primes

    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if prime_flags[i]:
            count += 1
        prime_counts[i] = count

    marias_wins, bens_wins = 0, 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins > bens_wins:
        return 'Maria'
    elif bens_wins > marias_wins:
        return 'Ben'
    else:
        return None
