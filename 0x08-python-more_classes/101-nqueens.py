#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    def solve(board, col, n):
        if col == n:
            yield list(board)
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[col] = row
                yield from solve(board, col + 1, n)
                board[col] = -1

    board = [-1] * n  # Initialize the board with -1
    solutions = list(solve(board, 0, n))
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception as ex:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        for i, row in enumerate(solution):
            print("[{}, {}]".format(row, i), end="")
            if i != len(solution) - 1:  # Check if it's not the last element in the row
                print(", ", end="")
        print()
