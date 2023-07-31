# Tic Tac Toe : Minimax Approach
from os import system, name


BOARD = "---------"
PLAYER = "X"
COMPUTER = "O"

class InvalidMove(Exception):
    """ Raised when an invalid move is made """


def print_board(board):
    print(f"    A   B   C  \n"
        f"1 | {board[0]} | {board[1]} | {board[2]} |\n"
        f"2 | {board[3]} | {board[4]} | {board[5]} |\n"
        f"3 | {board[6]} | {board[7]} | {board[8]} |\n")

def process_inputs(inp_str):
    if len(inp_str) != 2:
        raise ValueError("Enter 1 letter and 1 number")
    try:
        # A1
        letter = inp_str[0].upper()
        number = int(inp_str[1])
    except ValueError:
        # 1A
        number = int(inp_str[0])
        letter = inp_str[1].upper()
    
    # Bounds check
    if letter not in ["A", "B", "C"]:
        raise ValueError("Invalid Column")
    if number not in [1, 2, 3]:
        raise ValueError("Invalid Row")
    
    # Convert to index
    return (number - 1) * 3 + ("ABC".index(letter)) 

def check_status(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]

    # Check draw
    if "-" not in board:
        return "D"

    # If none of the above, return None, game will continue
    return None

def make_move(board, index, player):
    if board[index] == "-":
        board = board[:index] + player + board[index+1:]
        return board
    else:
        raise InvalidMove(f"Invalid move at index {index}")

def minimax(board, depth, is_max):
    
    # If terminal, then return score
    if check_status(board) == PLAYER:
        return depth - 10
    if check_status(board) == COMPUTER:
        return 10 - depth
    if check_status(board) == "D":
        return 0

    # 
    if is_max:
        best_val = -1000
        for i in range(9):
            if board[i] == "-":
                board = board[:i] + COMPUTER + board[i+1:]
                value = minimax(board, depth+1, False)
                best_val = max(best_val, value)
                board = board[:i] + "-" + board[i+1:]
        return best_val
    else:
        best_val = 1000
        for i in range(9):
            if board[i] == "-":
                board = board[:i] + PLAYER + board[i+1:]
                value = minimax(board, depth+1, True)
                best_val = min(best_val, value)
                board = board[:i] + "-" + board[i+1:]
        return best_val


def make_computer_move(board):
    # find best move
    best_val = -1000
    best_move = -1
    
    for i in range(9):
        if board[i] == "-":
            board = board[:i] + COMPUTER + board[i+1:]
            move_val = minimax(board, 0, False)
            board = board[:i] + "-" + board[i+1:]
            if move_val > best_val:
                best_val = move_val
                best_move = i
    
    return make_move(board, best_move, COMPUTER)

if __name__ == "__main__":
    # Print initial board, so layout is clear
    print_board(BOARD)
    while True:
        
        while True:
            print("[] Player's Turn")
            try:
                index = process_inputs(input("Enter your move: "))
                BOARD = make_move(BOARD, index, PLAYER)
                break
            except InvalidMove as e:
                print(e)
            except ValueError:
                print("Invalid input! Try again")
        
        print_board(BOARD)
        status = check_status(BOARD)
        if status not in [None, "D"]:
            print(f"{status} won!")
            break
        elif status == "D":
            print("Game Drawn!")
            break
        
        print("[] Minimax's Turn")
        # make computer move
        BOARD = make_computer_move(BOARD)
        
        print_board(BOARD)
        status = check_status(BOARD)
        if status not in [None, "D"]:
            print(f"{status} won!")
            break
        elif status == "D":
            print("Game Drawn!")
            break
