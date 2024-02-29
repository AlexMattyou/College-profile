def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -10 + depth
    elif check_winner(board, "O"):
        return 10 - depth
    elif check_draw(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_optimal_move(board):
    optimal_move = None
    best_score = float('-inf')
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            optimal_move = (row, col)
    return optimal_move

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        print("Computer is making its move...")
        optimal_move = get_optimal_move(board)
        board[optimal_move[0]][optimal_move[1]] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("Sorry, you lose!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()