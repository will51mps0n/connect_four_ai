import numpy
import pygame
import sys
import math
import copy

ROW_COUNT = 6
COLUMN_COUNT = 7

class ConnectFour:
    def __init__(self):
        self.board = numpy.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    
    # Returns all open columns that a move can be made in
    @staticmethod
    def get_valid_moves(board):
        open_cols = []
        for col in range(COLUMN_COUNT):
            if board[ROW_COUNT-1][col] == 0:
                open_cols.append(col)
        return open_cols

    # Returns updated board with the move made by the specified player
    @staticmethod
    def play_move(board, move, player):
        new_board = copy.deepcopy(board)
        for i in range(ROW_COUNT):
            if board[i][move] == 0:
                new_board[i][move] = player
                break
        return new_board

    # Heuristic function that evaluates best place for next move based on possible winning combinations
    # Outputs score
    @staticmethod
    def heuristic_value(board, player):
        score = 0
        ## Score center column
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(player)
        score += center_count * 3

        ## Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += ConnectFour.evaluate_window(window, player)

        ## Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += ConnectFour.evaluate_window(window, player)

        ## Score posiive sloped diagonal
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += ConnectFour.evaluate_window(window, player)

        ## Score negative sloped diagonal
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += ConnectFour.evaluate_window(window, player)

        return score
    
    # Checks if specified player has won based on the board state - returns boolean
    @staticmethod
    def is_winner(board, player):
        return ConnectFour.check_game(board, player)
    
    # Checks if board is full - return boolean
    @staticmethod
    def is_full(board):
        return len(ConnectFour.get_valid_moves(board)) == 0
    
    # Checks if game is finished - return boolean
    @staticmethod
    def game_over(board):
        p1winner = ConnectFour.is_winner(board, 1)
        p2winner = ConnectFour.is_winner(board, 2)
        full_board = len(ConnectFour.get_valid_moves(board)) == 0
        return p1winner or p2winner or full_board
    
    # Calculate the score of a specific window - return float
    @staticmethod
    def evaluate_window(window, player):
        score = 0
        opponent = 1
        if player == 1:
            opponent = 2

        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opponent) == 3 and window.count(0) == 1:
            score -= 4

        return score
    
    # Checks if specified player has won based on the board state - returns boolean
    @staticmethod
    def check_game(board, player):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == player and \
                        board[r][c + 1] == player and \
                        board[r][c + 2] == player and \
                        board[r][c + 3] == player:
                    return True
        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == player and \
                        board[r + 1][c] == player and \
                        board[r + 2][c] == player and \
                        board[r + 3][c] == player:
                    return True
        # Check positively sloped diagonals for a win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == player and\
                        board[r + 1][c + 1] == player and\
                        board[r + 2][c + 2] == player and \
                        board[r + 3][c + 3] == player:
                    return True
        # Check negatively sloped diagonals for a win
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == player and \
                        board[r - 1][c + 1] == player and \
                        board[r - 2][c + 2] == player and \
                        board[r - 3][c + 3] == player:
                    return True

        return False


    '''
    Following functions are used for UI of the game 
    '''
    @staticmethod
    def draw_board(board):        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    @staticmethod
    def pygame_helper(board, event, turn):
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

    @staticmethod
    def p1_helper(event):
        pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))

        return col
    
    @staticmethod
    def player_wins(player):
        myfont = pygame.font.SysFont("monospace", 75)
        if player == 1:
            label = myfont.render("Human wins!!", 1, WHITE)
        else:
            label = myfont.render("AI wins!!", 1, WHITE)
        text_rect = label.get_rect(center=(screen.get_width()/2, 50))
        screen.blit(label, text_rect)
    
#Variables used for UI of C4 board - NOT IMPORTANT FOR AGENT
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
WINDOW_LENGTH = 4
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
