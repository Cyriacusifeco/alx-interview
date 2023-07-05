#!/usr/bin/python3
"""
An algorithm to determine if a list of boxes can be unlocked
based on the keys in the unlocked ones. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys
(index of the next box) to the other boxes.
"""


def canUnlockAll(boxes):
    """
    A method that returns True if all the boxes can be unlocked
    and False otherwise.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track the state of each box
    unlocked[0] = True  # The first box is unlocked initially

    keys = [0]  # Start with the keys from the first box

    while keys:
        box = keys.pop()  # Get the next box to open

        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)  # Check if all boxes are unlocked
