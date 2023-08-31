#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    To get the island perimeter
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4  # Count the four sides of the cell

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract two sides shared

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract two sides shared with the neigh

    return perimeter
