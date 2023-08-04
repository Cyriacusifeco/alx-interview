#!/usr/bin/python3
"""
N-Queens module.
"""
import sys


def is_valid(board, row, col, N):
    """
    Function to check if Queen position is valid
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    """
    N-queens position
    """
    def backtrack(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_valid(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
