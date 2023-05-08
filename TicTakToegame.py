def draw_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def get_player_move(player, board):
    while True:
        try:
            row = int(input(f"{player}, enter row (1-3): ")) - 1
            col = int(input(f"{player}, enter column (1-3): ")) - 1
            if board[row][col] == "-":
                return row, col
            else:
                print("That space is already taken.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 3.")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    # Check for tie
    if "-" not in [val for row in board for val in row]:
        return "Tie"
    return None

def play_game():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    players = ["X", "O"]
    current_player = players[0]
    winner = None
    while not winner:
        draw_board(board)
        move_row, move_col = get_player_move(current_player, board)
        board[move_row][move_col] = current_player
        winner = check_winner(board)
        current_player = players[(players.index(current_player) + 1) % 2]
    draw_board(board)
    if winner == "Tie":
        print("Tie game!")
    else:
        print(f"{winner} wins!")

play_game()
