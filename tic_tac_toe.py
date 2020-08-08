#! /usr/bin/python3

from os import system

def display_game(game_board):
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


def change_player(player):

    if player == 1:
        print("Now it's O turn!")

    if player == -1:
        print("Now it's X turn")

    return player * -1

def do_a_play(player, round_counter):

    display_exemple()
    get_play = input('Choose a position between 1 and 9 to play')
    play = int(get_play)

    if game_board[play - 1] == '.':
        if player == 1:
            game_board[play - 1] = 'X'

        if player == -1:
            game_board[play - 1] = 'O'

        round_counter += 1

    else:
        system('clear')
        print('You can not play there')
        do_a_play(player.round_counter)

    system('clear')


def check_win(game_board):

    horizontal_win = game_board[0] == game_board[1] == game_board[2] != '.' or game_board[3] == game_board[4] == game_board[5] != '.' or game_board[6] == game_board[7] == game_board[8] != '.'
    vertical_win   = game_board[0] == game_board[3] == game_board[6] != '.' or game_board[1] == game_board[4] == game_board[7] != '.' or game_board[2] == game_board[5] == game_board[8] != '.'
    diagonal_win   = game_board[0] == game_board[4] == game_board[8] != '.' or game_board[2] == game_board[4] == game_board[6] != '.'

    win  = horizontal_win or vertical_win or diagonal_win
    draw = round_counter == 9

    if win:
        return 'winner'

    elif draw:
        return 'draw'

    else:
        return False

player = 1
round_counter = 0

game_board = ['.','.','.',
              '.','.','.',
              '.','.','.']

while True:

    player = change_player(player)

    print(player)

    result = check_win(game_board)

    if result:
        print(f'Game over! We have a {result}')
        break

    do_a_play(player, round_counter)

    display_game(game_board)

