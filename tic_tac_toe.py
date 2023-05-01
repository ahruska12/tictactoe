

board = ['-'] * 9
current_player = 'X'

def print_board():
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            if board[move - 1] != '-':
                raise ValueError
            return move - 1
        except ValueError:
            print("Invalid move, try again.")

def check_win():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return True
    for i in range(3):
        col = [board[i+j*3] for j in range(3)]
        if col == ['X', 'X', 'X'] or col == ['O', 'O', 'O']:
            return True
    diag1 = [board[0], board[4], board[8]]
    diag2 = [board[2], board[4], board[6]]
    if diag1 == ['X', 'X', 'X'] or diag1 == ['O', 'O', 'O'] or diag2 == ['X', 'X', 'X'] or diag2 == ['O', 'O', 'O']:
        return True
    return False

def play_game():
    global board, current_player
    while True:
        print_board()
        print(f"It's {current_player}'s turn.")
        move = get_move()
        board[move] = current_player
        if check_win():
            print_board()
            print(f"{current_player} wins!")
            break
        elif '-' not in board:
            print_board()
            print("Tie game!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
