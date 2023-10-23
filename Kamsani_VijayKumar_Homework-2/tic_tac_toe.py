"""
Homework 2
Problem 4
Author: Vijay Kumar Kamsani
"""

# Function to print the tic-tac-toe board
def print_board(board):
    print("-------------")
    #a = "|"
    for row in board:
        print("|", "|".join(row), "|", sep="")
        print("-------------")


# Function to check if any player has won
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "   ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "   ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "   ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "   ":
        return True

    return False


# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        if "   " in row:
            return False
    return True


# Function to play the tic-tac-toe game
def play_game():
    board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
    player = "X"
    turn = 0
    while True:
        print_board(board)
        if turn % 2 == 0:
            row = int(input("Enter the row (0, 1 or 2) for player X: "))
            col = int(input("Enter the column (0, 1 or 2) for player X: "))
        else:
            row = int(input("Enter the row (0, 1 or 2) for player O: "))
            col = int(input("Enter the column (0, 1 or 2) for player O: "))
        turn += 1

        if board[row][col] == "   ":
            board[row][col] = " "+player+" "
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board):
            print_board(board)
            print(player, "Player won")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


# Start the game
if __name__ == '__main__':
    play_game()
