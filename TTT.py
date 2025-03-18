import copy


class TicTacToe:
    def __init__(self, piece_map = ("X", "O")):
        self.board = [[0, 0, 0] for i in range(3)]
        self.piece_map = piece_map

    # Start of game related functions that can be used in Agent
    
    # Returns all open coordinates that a move can be made in
    @staticmethod
    def get_valid_moves(board):
        valid_coords = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    valid_coords.append((i,j))
        return valid_coords

    # Returns updated board with the move made by the specified player
    @staticmethod
    def play_move(board, move, player):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = player
        return new_board

    # Heuristic function that evaluates best place for next move based on possible winning combinations
    # Outputs score
    @staticmethod
    def heuristic_value(board, player):
        p1 = player
        p2 = [2, 1][player-1]
        check_lists = TicTacToe.get_lists(board)
        score = 0
        for l in check_lists:
            if p1 in l and p2 in l:
                score += 0
            else:
                score += (10*board.count(p1) - (10**board.count(p2)))
        return score

    # Checks if specified player has won based on the board state - returns boolean
    @staticmethod
    def is_winner(board, player):
        return TicTacToe.check_game(board, player)
    
    # Checks if board is full - return boolean
    @staticmethod
    def is_full(board):
        return len(TicTacToe.get_valid_moves(board)) == 0
    
    # End of Agent related functions. Start of Gameplay functions
    
    # Checks if game is finished - return boolean
    @staticmethod
    def game_over(board):
        p1win = TicTacToe.is_winner(board, 1)
        p2win = TicTacToe.is_winner(board, 2)
        return len(TicTacToe.get_valid_moves(board)) == 0 or p1win or p2win
    
    # Checks if specified player has won based on the board state - returns boolean
    @staticmethod
    def check_game(board, player):
        check_lists = TicTacToe.get_lists(board)
        for l in check_lists:
            state = TicTacToe.check_list(l, player)
            if state:
                return state
        return False
    
    @staticmethod
    def check_list(token_list, player):
        if token_list == [player, player, player]:
            return 1
        return 0

    @staticmethod
    def get_lists(board):
        left_diag = []
        right_diag = []
        for i in range(3):
            left_diag.append(board[i][i])
            right_diag.append(board[i][2 - i])

        check_lists = [board[0],
                       board[1],
                       board[2],
                       [board[i][0] for i in range(3)],
                       [board[i][1] for i in range(3)],
                       [board[i][2] for i in range(3)],
                       left_diag,
                       right_diag]
        return check_lists
