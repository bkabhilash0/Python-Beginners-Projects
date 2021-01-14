import sys
import numpy as np

board = np.array([[1,0,0],
                 [0,1,1],
                 [0,0,1]])

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
        victory(board)

def check_row(board):
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != 0:
            return True
    return False

def check_column(board):
    board = board.transpose()
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != 0:
            return True
    return False

def check_diagnol(board):
    board = [np.diag(board),np.flipud(board).diagonal()]
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != 0:
            return True
    return False

def victory(board):
    # print_board(board)
    print("************************Winner!!!**********************************")
    print("Player 1 Wins the Game")
    sys.exit()


print_board(board)
