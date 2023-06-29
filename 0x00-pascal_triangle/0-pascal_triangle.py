#!/usr/bin/python3
"""
Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        -List[List[int]]: The Pascal's triangle represented as a list of lists of integers.

        -[]: Empty list If n is less than or equal to 0.
    """

    if n <= 0:
        return []
	
    # Initialize the triangle with the first row, [1]
    triangle = [[1]]

    for i in range(1, n):

	# Initialize the new row with the leftmost element, which is always 1
        row = [1]

	# Calculate the value at position (i, j) by summing the corresponding values from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

	# Add the rightmost element of the row, which is always 1
        row.append(1)

	# Add the row to the triangle
        triangle.append(row)

    return triangle
