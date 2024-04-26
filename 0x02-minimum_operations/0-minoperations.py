#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly n H
    characters in the file.
    """
    if n < 2:
        return 0

    i = 2
    while i < n + 1:
        if n % i == 0:
            return minOperations(n // i) + i
        i = i + 1
