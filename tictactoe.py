# This is the first Milestone project for Python 3 Bootcamp through Udemy

from IPython.display import clear_output

def display_board(board):
    '''
    This function prepares the playing board
    '''
    clear_output()

    print('    |    |')
    print('  ' + board[7] + ' |  ' + board[8] + ' | ' + board[9])
    print('    |    |')
    print('-------------')
    print('    |    |')
    print('  ' + board[4] + ' |  ' + board[5] + ' | ' + board[6])
    print('    |    |')
    print('-------------')
    print('    |    |')
    print('  ' + board[1] + ' |  ' + board[2] + ' | ' + board[3])
    print('    |    |')

def player_input():
    '''
    Sets up the marker for each player
    '''
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Would you like to be 'X' or 'O'? ").upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
    places a marker in the desired position on the board
    '''
    board[position] = marker

def win_check(board, mark):
    '''
    checks for a winner
    '''
    return ((board[7] == mark and board[8] == mark and board[9] == mark or
            board[4] == mark and board[5] == mark and board[6] == mark or
            board[1] == mark and board[2] == mark and board[3] == mark or
            board[1] == mark and board[4] == mark and board[7] == mark or
            board[2] == mark and board[5] == mark and board[8] == mark or
            board[3] == mark and board[6] == mark and board[9] == mark or
            board[1] == mark and board[5] == mark and board[9] == mark or
            board[7] == mark and board[5] == mark and board[3] == mark))

import random

def choose_first():
    '''
    randomly decides who goes first
    '''
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    '''
    checks if space on board is empty
    '''
    return board[position] == ' '

def full_board_check(board):
    '''
    checks if board is full
    '''
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    '''
    asks for player's next position
    '''
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    '''
    asks if they want to play again
    '''
    play_again = input('Would you like to play again? (y/n) ')
    return play_again.lower() == 'y'

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input('Are you ready to play? (yes or no) ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("PLAYER 1 HAS WON")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('STALEMATE')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("PLAYER 2 HAS WON")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('STALEMATE')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break