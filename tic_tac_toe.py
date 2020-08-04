#! /usr/bin/python3

from os import system

game_board = ['.','.','.',
              '.','.','.',
              '.','.','.']
player = 1
round_counter = 0

def display_game():
    print(f' {game_board[6]} | {game_board[7]} | {game_board[8]}')
    print('--- --- ---')
    print(f' {game_board[3]} | {game_board[4]} | {game_board[5]}')
    print('--- --- ---')
    print(f' {game_board[0]} | {game_board[1]} | {game_board[2]}\n')


def display_exemple():
    print(f'These are the spaces that the numbers represent')
    print(f' 7 | 8 | 9')
    print(f'--- --- ---')
    print(f' 4 | 5 | 6')
    print(f'--- --- ---')
    print(f' 1 | 2 | 3')


def change_player():
    global player

    if player == 1:
        print("Now it's O turn!")

    if player == -1:
        print("Now it's X turn")

    player = player * -1


def do_a_play():
    global player
    global round_counter

    display_exemple()
    get_play = input('Choose a position between 1 and 9 to play')
    play = int(get_play)

    if game_board[play - 1] == '.':
        if player == 1:
            game_board[play - 1] = 'X'

        if player == -1:
            game_board[play - 1] = 'O'

        round_counter = round_counter + 1

    else:
        system('clear')
        print('You can not play there')
        do_a_play()

    system('clear')


def check_win():

    # Check horizontal win
    if game_board[0] == game_board[1] == game_board[2] != '.' or game_board[3] == game_board[4] == game_board[5] != '.' or game_board[6] == game_board[7] == game_board[8] != '.':
        print(f'We have a winner!')
        exit()

    # Check vertical win
    if game_board[0] == game_board[3] == game_board[6] != '.' or game_board[1] == game_board[4] == game_board[7] != '.' or game_board[2] == game_board[5] == game_board[8] != '.':
        print(f'We have a winner!')
        exit()

    # Check diagonal win
    if game_board[0] == game_board[4] == game_board[8] != '.' or game_board[2] == game_board[4] == game_board[6] != '.':
        print(f'We have a winner!')
        exit()

    # Check draw
    elif round_counter == 9:
        print(f'It is a draw!')
        exit()

    change_player()


while True:
    check_win()
    do_a_play()
    display_game()

