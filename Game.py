"""
The Game class.
This is the template of a Game object. Every Game must implement these functions
"""
import pygame
import random
import sys
import math
import numpy
from TTT import TicTacToe
from Connect4 import ConnectFour
from Agent import Agent


# We use this to track who the player is
class Player():
    HUMAN = 1
    AI = 2

def getInput():
    row = int(input("Row:"))
    col = int(input("Col:"))
    return (row, col)

def display(board, charmap):
    for row in board:
        print("|", end="")
        for col in row:
            if col != 0:
                print(charmap[col-1], end="|")
            else:
                print(" ", end="|")
        print()

def TTT(turn):
    game = TicTacToe()
    board = game.board
    agent = Agent(game, Player.AI, Player.HUMAN) #do not change
    display(board, game.piece_map)
    while not(game.game_over(board)):
        if turn == Player.HUMAN:
            print("Your turn")
            yourmove = ()
            while yourmove not in game.get_valid_moves(board):
                yourmove = getInput()
            board = game.play_move(board, yourmove, Player.HUMAN)
            display(board, game.piece_map)
            turn +=1

        elif turn == Player.AI and not(game.game_over(board)):
            aimove, minimax_score = agent.minimax(board, 8, True,  -float('inf'),  float('inf'))
            print("AI plays:", aimove, "Value:", minimax_score)
            board = game.play_move(board, aimove, Player.AI)
            display(board, game.piece_map)
            print("-----------------------")
            turn -=1

    if game.is_winner(board, Player.AI):
        print("AI wins!!")
    elif game.is_winner(board, Player.HUMAN):
        print("Human wins!!")
    elif game.is_full(board):
        print("Tie - board is full")

def update_c4_boards(board, game, player, col, turn):
    ROW_COUNT, COLUMN_COUNT = board.shape
    if board[ROW_COUNT-1][col] == 0:
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                board[r][col] = player
                break

        if game.is_winner(board, player):
            game.player_wins(player) # Display message on screen
            
        turn += 1
        if player == Player.AI:
            turn = turn % 2 # turn is only 1 or 2

        print(numpy.flip(board, 0))
        game.draw_board(board)
    return turn

def C4(turn, c4board):
    game = ConnectFour()
    board = game.board
    if len(sys.argv) == 3: # updates the board with test case
        board = c4board
    pygame.init()
    game.draw_board(board)
    pygame.display.update()
    agent = Agent(game, Player.AI, Player.HUMAN) # do not change

    while not(game.game_over(board)):
        for event in pygame.event.get():
            game.pygame_helper(board, event, turn)
            if event.type == pygame.MOUSEBUTTONDOWN and turn == Player.HUMAN:
                next_move = game.p1_helper(event)
                turn = update_c4_boards(board, game, Player.HUMAN, next_move, turn)
                print("Human plays at column:", next_move)
                print()

        if turn == Player.AI and not(game.game_over(board)):				
            next_move, minimax_value = agent.minimax(board, 6, True, -math.inf, math.inf)
            turn = update_c4_boards(board, game, Player.AI, next_move, turn)
            print("AI plays at column:", next_move, "Value:", minimax_value)
            print()
    
    if game.is_winner(board, Player.HUMAN):
        print("HUMAN wins!!")
    elif game.is_winner(board, Player.AI):
        print("AI wins!!")
    print()
    pygame.time.wait(3000)


if __name__ == "__main__":
    turn = random.randint(Player.HUMAN, Player.AI)

    if len(sys.argv) == 3 and sys.argv[1] == 'C4':
        filename = 'Tests/' + sys.argv[2]
        with open(filename) as f:
            turn = int(f.readline())
        c4board = numpy.genfromtxt(filename, dtype=int, encoding=None, delimiter=" ", skip_header=1)
        c4board = numpy.flip(c4board, 0)
        C4(turn, c4board)
    elif len(sys.argv) == 3 and sys.argv[1] == 'TTT':
        print('Cannot run TTT with the local tests')
    elif len(sys.argv) == 2 and sys.argv[1] == 'TTT':
        TTT(turn)
    elif len(sys.argv) == 2 and sys.argv[1] == 'C4':
        C4(turn, [])
    else:
        print('Incorrect input, check the homework spec on how to run these files')
