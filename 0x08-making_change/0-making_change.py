#!/usr/bin/python3
"""
Module for making change with the fewest number of coins
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of
    # coins needed for each amount.
    # Initialize with float('inf') to
    # indicate that we don't have a solution yet.
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin_value in coins:
        for amount in range(coin_value, total + 1):
            min_coins[amount] = min(
                    min_coins[amount],
                    min_coins[amount - coin_value] + 1
                    )

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]


if __name__ == "__main__":
    # Test cases
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
