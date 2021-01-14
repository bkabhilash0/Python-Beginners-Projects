import sys
import numpy as np
import random

board = np.array([["0","0","0"],
                 ["0","0","0"],
                 ["0","0","0"]])

def print_board(board):

    print("-------------")
    for i in range(len(board)):
        print("|",end=" ")
        for j in board[i]:
            print(j,end=" ")
            print("|",end=" ")
        print()
        print("-------------")
    if check_row(board) or check_column(board) or check_diagnol(board):
        return True

def check_row(board):
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != "0":
            victory(list(set(i))[0])
            return True
    return False

def check_column(board):
    board = board.transpose()
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != "0":
            return True
    return False

def check_diagnol(board):
    board = [np.diag(board),np.flipud(board).diagonal()]
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != "0":
            return True
    return False

def victory(player):
    print("************************Winner!!!**********************************")
    print(f"Player {player} Wins the Game")
    sys.exit()

def main(board):
    running = True
    print_board(board)
    while running:
        p_1 = random.randint(0,2)
        p_2 = random.randint(0,2)
        o_1 = random.randint(0,2)
        o_2 = random.randint(0,2)
        if board[p_1][p_2] != "X" and board[p_1][p_2] != "Y":
            board[p_1][p_2] = "X"
        else:
            continue
        if board[o_1][o_2] != "X" and board[o_1][o_2] != "Y":
            board[o_1][o_2] = "Y"
        else:
            continue
        isVictory = print_board(board)
        if isVictory:
            victory(board)

main(board)
