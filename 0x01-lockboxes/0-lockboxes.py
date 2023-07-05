#!/usr/bin/python3


def canUnlockAll(boxes):
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
