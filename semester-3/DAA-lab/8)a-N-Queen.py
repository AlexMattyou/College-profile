def isSafe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def util(board, col, N):
    if col == N:
        return True
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            if util(board, col + 1, N):
                return True
            board[i][col] = 0  # Backtrack
    return False

def solveQ(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not util(board, 0, N):
        print("Solution does not exist.")
        return
    print("Solution for N =", N, "queens:")
    for row in board:
        print(" ".join(map(str, row)))

solveQ(8)
solveQ(4)
