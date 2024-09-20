import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")

# Function to check for available spots on the board
def available_spots(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Function to check for winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

# Function to check for a draw
def is_draw(board):
    return " " not in [cell for row in board for cell in row]

# Minimax function to calculate the best move
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):  # AI wins
        return 1
    if check_winner(board, "X"):  # Human wins
        return -1
    if is_draw(board):  # It's a draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in available_spots(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Alpha-Beta pruning
        return best_score
    else:
        best_score = math.inf
        for (i, j) in available_spots(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Alpha-Beta pruning
        return best_score

# Function to get the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in available_spots(board):
        board[i][j] = "O"
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Function to play Tic-Tac-Toe
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and AI is O.")
    print_board(board)

    # Game loop
    while True:
        # Human player's turn
        while True:
            try:
                row, col = map(int, input("\nEnter your move (row and column from 1 to 3): ").split())
                if board[row-1][col-1] == " ":
                    board[row-1][col-1] = "X"
                    break
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError):
                print("Please enter row and column as two integers between 1 and 3.")

        print_board(board)

        # Check if the human won
        if check_winner(board, "X"):
            print("You win!")
            break

        # Check for a draw
        if is_draw(board):
            print("It's a draw!")
            break

        # AI's turn
        print("\nAI's turn:")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print_board(board)

        # Check if the AI won
        if check_winner(board, "O"):
            print("AI wins!")
            break

        # Check for a draw
        if is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
