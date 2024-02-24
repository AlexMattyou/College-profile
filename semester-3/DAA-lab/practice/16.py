def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """
    Solve the N-Queens problem recursively using backtracking.
    """
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1):
                return True

            # If placing the queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If the queen cannot be placed in any row of this column, return False
    return False


def print_solution(board):
    """
    Print the solution board.
    """
    for row in board:
        print(" ".join(map(str, row)))


def solve_n_queens_problem(n):
    """
    Solve the N-Queens problem for a given board size.
    """
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens(board, 0):
        print("No solution exists")
        return False

    print("Solution:")
    print_solution(board)
    return True


# Solve the N-Queens problem for 5 queens
solve_n_queens_problem(5)


'''
output:

Solution:
1 0 0 0 0
0 0 0 1 0
0 1 0 0 0
0 0 0 0 1
0 0 1 0 0

'''