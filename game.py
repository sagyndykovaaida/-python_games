board = [' ' for _ in range(9)]  

def print_board():
    """Prints the current game board."""
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def is_winner(player):
    """Checks if a player has won the game."""
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def is_board_full():
    """Checks if the game board is full."""
    return ' ' not in board

print_board()  # Print the initial game board

while True:
    # Player 1's turn
    print("Player 1's turn (X)")
    move = int(input("Enter a position (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("That position is already taken!")
        continue
    print_board()
    if is_winner('X'):
        print("Player 1 (X) has won!")
        break
    if is_board_full():
        print("The game is a tie!")
        break

    # Player 2's turn
    print("Player 2's turn (O)")
    move = int(input("Enter a position (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'O'
    else:
        print("That position is already taken!")
        continue
    print_board()
    if is_winner('O'):
        print("Player 2 (O) has won!")
        break
    if is_board_full():
        print("The game is a tie!")
        break
