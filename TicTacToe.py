# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:29:24 2019

@author: eugen
"""

#while loop when players have yet to win or draw

#need a containment to see whether position != ' '

#indexing to replace positions in string

#win condition is ... refer to paper

#player turn
print('Players, Choose positions 0 to 8:')
print(7 * '=')
print('|0|1|2| \n|3|4|5| \n|6|7|8|')
print(7 * '=')
print()

lst = [' '] * 9
#print(lst)

def print_board():
    print(7 * '=')
    for i in range(0, len(lst), 3):
        new_string = '|' + lst[i] + '|' + lst[i+1] + '|' + lst[i+2] + '|'
        print(new_string)
    print(7 * '=')
print_board()

player_turn = 'X'
def player_input():
    global player_turn
    user_index = int(input('Player {}, choose position :'.format(player_turn)))
    while lst[user_index] != ' ':
        user_index = int(input('Player {}, choose position :'.format(player_turn)))
    if player_turn == 'X':
        lst[user_index] = 'X'
    else:
        lst[user_index] = 'O'

def change_turn():
    global player_turn
    if player_turn == 'X':
        player_turn = 'Y'
    else:
        player_turn = 'X'

win = 'False'
def win_condition():
    global lst
    global win
    #check row
    for i in range(0, 9, 3):
        if lst[i:i+3] == ['X', 'X', 'X'] or lst[i:i+3] == ['O', 'O', 'O']:
            win = True
    #check column
    for i in range(0, 3, 3):
        check_string = lst[i] + lst[i+3] + lst[i+6]
        if check_string == ['X', 'X', 'X'] or check_string == ['O', 'O', 'O']:
            win = True
            
    #check diagonal
    diagonal_1 = lst[0] + lst[4] + lst[8]
    diagonal_2 = lst[2] + lst[4] + lst[6]
    if diagonal_1 == ['X', 'X', 'X'] or diagonal_1 == ['O', 'O', 'O']:
        win = True 
    if diagonal_2 == ['X', 'X', 'X'] or diagonal_2 == ['O', 'O', 'O']:
        win = True

draw = 'False'
def draw_condition():
    global draw
    for elem in lst:
        if elem == ' ':
            return
    draw = True

win = False
draw = False
player_turn = 'Y'
while win == False and draw == False: #be careful of Demorgan’s law
    change_turn()
    player_input()
    print_board()
    win_condition()
    draw_condition()


if win == True:
    print(player_turn, 'wins!')
elif draw == True:
    print('This game is a draw!')
    


    