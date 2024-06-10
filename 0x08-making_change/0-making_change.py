#!/usr/bin/python3
"""Determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
    to meet a given amount total using a greedy approach.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    coin_count = 0

    for coin in coins:
        # Use as many of the current coin as possible
        coin_count += total // coin
        # Reduce the total by the amount of coins used
        total %= coin

    # If total is not zero, it means the remaining amount
    # cannot be achieved with the given coins
    if total != 0:
        return -1

    return coin_count
