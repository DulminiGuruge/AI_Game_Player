"""
Tic Tac Toe game with an AI Player 
"""

import math
import copy

X = "X"
O = "O"
EMPTY = '_'

board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# Function to print the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i] [2], "|")
        print("-------------")


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter_X = 0
    counter_O = 0
    
    for row in board:
        counter_X += row.count('X')
        counter_O += row.count('O')

    if counter_X > counter_O:
        return 'O'
    else:
        return 'X'    
                     
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(3):
        for cell in range(3):
            if board[row][cell]== EMPTY:                
                possible_actions.add((row,cell))

    #print(possible_actions)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    valid_moves = [0,1,2]
    row = action[0]
    cell = action[1]

    if row not in valid_moves or cell not in valid_moves:
        raise Exception("Not a valid move")
    if board[row][cell] != EMPTY:
        raise Exception("The cell is not empty")


    board_copy = copy.deepcopy(board)
    board_copy[row][cell] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """ for i in range(3):
        if EMPTY in board[i]:
            break
        return "tie" """
    #check horizontally
    if board [0][0] == board[0][1] and board[0][1] == board[0][2] :
        if board[0][0] != EMPTY:
            return board[0][0]
        
    
    elif board [1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] != EMPTY:
            return board[1][0]
    
    elif board [2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] != EMPTY:
            return board[2][0]

    #check vertically

    elif board [0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] != EMPTY:
            return board[0][0]
    
    elif board [0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] != EMPTY:
            return board[0][1]
    
    elif board [0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] != EMPTY:
            return board[0][2]

    #check diagonally

    elif board [0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    
    elif board [0][2] == board[1][1] and  board[1][1] == board[2][0]:
        if board[0][2] != EMPTY:
            return board[0][2]
    

    else:
        
        return None

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if  len(actions(board))== 0:
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def find_max(board, depth, alpha,beta):
    
    
    if terminal(board) or depth == 0:
        return utility(board),None
    move = None
    maxVal = float('-inf')
    for action in actions(board):
           
            value,act = find_min(result(board,action), depth-1, alpha, beta)
           
            maxVal = max( maxVal, value) 
            alpha = max( alpha, maxVal)
            move = action
            if beta <= alpha:
                break
    return maxVal, move
  
        

def find_min(board, depth, alpha,beta):
       
    if terminal(board) or depth == 0:
        return utility(board),None
    
    move = None
    minVal = float('inf')
    for action in actions(board) :
            
            value, act = find_max(result(board,action), depth-1, alpha, beta)
            minVal = min( minVal, value) 
            beta = min( beta, minVal)
            move = action
            if beta <= alpha:
                break
    return minVal, move
     
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = find_max(board,9, float('-inf'), float('inf') )
            return move
        else:
            value, move = find_min(board,9,  float('-inf'), float('inf'))
            return move
     

# Main game loop
while True:
    print_board(board)
    
   
    
    if winner(board) is not None:
        print("Player", winner(board), "wins!")
        break
    if terminal(board):
        print("It is a tie")

    
    if player(board)=='O':
        # Player O's turn
        while True:
            move = int(input("Enter O's move (0-8): ")) 
            result(board,(move//3,move%3))
           
            if board[move//3][move%3] == EMPTY:
                board[move//3][move%3] = O
                break
            else:
                print("Invalid move! Try again.")
    else:
        # Player X's turn
        move = minimax(board)
       # print(move)
        board[move[0]][move[1]] = X

    
