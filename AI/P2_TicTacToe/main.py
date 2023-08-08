#!/usr/bin/env python
"""TicTacToe Opponent with Minimax Algorithm"""

__author__ = "Devansh Parapalli"

BOARD = "---------"
PLAYER = "X"
COMPUTER = "O"

_DRAW_MSG = "Game Drawn !"

class InvalidMove(Exception):
    """ Raised when an invalid move is made """

def print_board(board):
    print(f"    A   B   C  \n"
        f"1 | {board[0]} | {board[1]} | {board[2]} |\n"
        f"2 | {board[3]} | {board[4]} | {board[5]} |\n"
        f"3 | {board[6]} | {board[7]} | {board[8]} |\n")

def notation_to_index(inp_str):
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
    if letter not in "ABC":
        raise ValueError("Invalid Column")
    if number not in [1, 2, 3]:
        raise ValueError("Invalid Row")
    
    # Convert to index
    return (number - 1) * 3 + ("ABC".index(letter)) 

def index_to_notation(index):
    # Convert to letter
    letter = "ABC"[index % 3]
    # Convert to number
    number = index // 3 + 1
    return f"{letter}{number}"

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

def make_move(index, player):
    global BOARD
    if BOARD[index] == "-":
        BOARD = BOARD[:index] + player + BOARD[index+1:]
    else:
        raise InvalidMove(f"[] Invalid move at index {index}")

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


def computer():
    global BOARD
    # find best move
    best_val = -1000
    best_move = -1
    
    for i in range(9):
        if BOARD[i] == "-":
            BOARD = BOARD[:i] + COMPUTER + BOARD[i+1:]
            move_val = minimax(BOARD, 0, False)
            BOARD = BOARD[:i] + "-" + BOARD[i+1:]
            if move_val > best_val:
                best_val = move_val
                best_move = i
    
    print("[] Minimax's Turn")
    print(f"[] Minimax: Best Move - {index_to_notation(best_move)}")
    make_move(best_move, COMPUTER)

def player():
    global BOARD
    while True:
        print("[] Player's Turn")
        try:
            index = notation_to_index(input("[x] Enter your move: "))
            make_move(index, PLAYER)
            break
        except InvalidMove as e:
            print(e)
        except ValueError:
            print("[] Invalid input! Try again")

def check_and_terminate():
    status = check_status(BOARD)
    if status not in [None, "D"]:
        print(f"[] {'Computer' if status == COMPUTER else 'Player'} won!")
        return True
    elif status == "D":
        print(_DRAW_MSG)
        return True
    return False

if __name__ == "__main__":
    isPlayerFirst = input("[x] Player First ? (y/N): ").lower() == "y"
    print_board(BOARD)
    while True:
        player() if isPlayerFirst else computer()
        print_board(BOARD)
        if check_and_terminate(): break
        computer() if isPlayerFirst else player()
        print_board(BOARD)
        if check_and_terminate(): break