"""
The Agent class - uses a single min max function.
The minimax function is used in a generic Game class
"""
class Agent:
    def __init__(self, game, selfPiece, opponentPiece):
        self.game = game
        self.MIN = -float('inf')
        self.MAX = float('inf')
        self.winscore =  10000000
        self.losescore = -10000000
        # SELF PIECE - this is the AI :) 
        self.selfPiece = selfPiece          
        self.opponentPiece = opponentPiece  

    # p = max
    #state = root init.

    def minmaxSearch(game,state):
        return None
    
    def maxVal(game,state,p):
        return None
    
    def minVal(game,state,p):
        return None
    

    def minimax(self, board, depth, maximizingPlayer, alpha, beta):
        #base case        
        if self.game.game_over(board):
            if self.game.is_winner(board, self.selfPiece):
                return None, self.winscore + depth
            elif self.game.is_winner(board, self.opponentPiece):
                return None, self.losescore - depth

        if self.game.is_full(board) or depth == 0:
            heuristic = self.game.heuristic_value(board, self.selfPiece)
            return None, heuristic
        
        #recursive step
        #scores = []
        #scores.append(self.game.heuristic_value(possible_board, self))

        valid_moves = self.game.get_valid_moves(board)
        best_move = None

        if maximizingPlayer:
            highest_val = -float('inf')
        #creates state space with potential boards
            for move in valid_moves: 
                possible_board = self.game.play_move(board, move, self.selfPiece)              
                _, new_val = self.minimax(possible_board, depth - 1, False, alpha, beta)
                
                if new_val > highest_val:
                    highest_val = new_val
                    alpha = max(alpha, highest_val)
                    best_move = move

                # pruning step:
                if beta <= alpha:
                    break
                if highest_val >= beta:
                    return move, eval

            return best_move, highest_val
        # if max player

        else: #minimizing
            minimum = float('inf')

            for move in valid_moves:
                possible_board = self.game.play_move(board, move, self.opponentPiece)
                _, lowest_val = self.minimax(possible_board, depth - 1, True, alpha, beta)

                if lowest_val < minimum:
                    minimum = lowest_val
                    beta = minimum
                    best_move = move
                
                beta = min(beta, minimum)
                if beta <=alpha:
                    break
                if minimum <= alpha:
                    return move, minimum

            return best_move, minimum
