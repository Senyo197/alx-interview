#!/usr/bin/python3
"""
N-Queens Solver

This module provides functions to solve the N-Queens problem, which involves
placing N queens on an NxN chessboard such that no two queens threaten each
other. The module includes functions to validate queen positions, place queens
on the board, and find all possible solutions for a given board size.

Functions:
    is_valid_position(board, row, col):
        Checks if a position is valid for placing a queen on the board.

    put_next_queen(board, row):
        Tries to place a queen on the next row of the board at a valid position

    find_nqueens_solution(board, solutions=[]):
        Solves the N-Queens problem for a given board and appends the solutions
        to the given list.

    find_solutions(n):
        Runs the N-Queens solver for a given board size and prints the
        solutions.

Example:
    To solve the N-Queens problem for a board of size 8, run the script as
    follows:
    $ python3 nqueens.py 8
"""

import sys


def is_valid_position(board, row, col):
    """
    Checks if placing a queen at the specified position is valid.

    Args:
        board (list of list of int): The chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    b_size = len(board)
    if sum(board[row]) != 0 or sum([board[i][col] for i in range(b_size)]) !=
    0:
        return False

    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r, c = r + i, c + j
            if board[r][c]:
                return False
    return True


def put_next_queen(board, row):
    """
    Attempts to place a queen on the next row at a valid position.

    Args:
        board (list of list of int): The chessboard.
        row (int): The row index.

    Returns:
        bool: True if a queen was placed, False otherwise.
    """
    st, end = 0, len(board)
    if sum(board[row]) == 1:
        st = board[row].index(1) + 1
        board[row] = [0 for col in range(end)]

    for col in range(st, end):
        if is_valid_position(board, row, col):
            board[row][col] = 1
            return True
    return False


def find_nqueens_solution(board, solutions=[]):
    """
    Solves the N-Queens problem and appends solutions to the list.

    Args:
        board (list of list of int): The chessboard.
        solutions (list of list of list of int): The list to store solutions.
    """
    n = len(board)
    row = 0
    while row < n:
        if put_next_queen(board, row):
            row += 1
        else:
            if row - 1 < 0:
                break
            row -= 1
        if row == n:
            solutions.append([[row, board[row].index(1)] for row in range(n)])
            row -= 1

    if row == 0:
        return

    solutions.append([[row, board[row].index(1)] for row in range(n)])
    idx = board[0].index(1)
    if idx > -1:
        board = [[0 for _ in range(n)] for row in range(n)]
        board[0][idx] = 1
        find_nqueens_solution(board, solutions)


def find_solutions(n):
    """
    Finds and prints all solutions for the N-Queens problem of size n.

    Args:
        n (int): The size of the board.
    """
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    find_nqueens_solution(board, solutions)
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        find_solutions(n)

    except ValueError:
        print('N must be a number')
        sys.exit(1)
