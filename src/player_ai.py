from python_settings import settings
from math import inf
from copy import deepcopy
from random import randint
from player import Player

# Initialize settings.py as environment variable
import os
os.environ["SETTINGS_MODULE"] = 'settings' 

class PlayerAI(Player):
    
    def __init__(self, color, difficulty = settings.MEDIUM, player_str = settings.AI_STR):
        self.difficulty = difficulty
        super().__init__(color, player_str)

        # self.evaluation_table[i][j]: indicates the number of four connected positions including the space [i][j]
        self.evaluation_table = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3]
        ]

    def get_move(self, **kwargs) -> str:
        '''
        Overrides get_move() from the parent class 'Player' and returns
        a move based off the board and difficulty mode of the AI.
        '''
        board = kwargs['board']

        if self.difficulty == settings.EASY:
            return self.random_move(board)

        elif self.difficulty == settings.MEDIUM:
            return self.best_move(board)

    # ===== Easy Difficulty ===== #
    def random_move(self, board) -> str:
        '''
        Easy Difficulty: 
            Returns a random column move.
        '''
        return str(randint(1, settings.COLS))

    # ===== Medium Difficulty ===== #
    def best_move(self, board) -> str:
        '''
        Medium Difficulty:
            Returns a better move.
        '''
        highest_value = self.minimax(deepcopy(board), settings.MAX_DEPTH, self.color)

        print(highest_value)

        return str(self.random_move(board))

    def minimax(self, board, depth, maximizing_player):
        if depth == 0:
            return self.evaluate(board)
        
        # List of all available columns
        moves = board.all_moves()
        # Next Player that will be used in minimax alg
        next_player = self.opposite_player(maximizing_player)

        # AI is looking for the max value that can be gained
        if maximizing_player == self.color:
            value = -inf
            
            for i in range(len(moves)):
                board_copy = deepcopy(board)
                board_copy.move(i, maximizing_player)
                value = max(value, self.minimax(board_copy, depth - 1, next_player))

        # AI is looking for the min value that can be gained from the opposing player
        else:
            value = inf

            for i in range(len(moves)):
                board_copy = deepcopy(board)
                board_copy.move(i, maximizing_player)
                value = min(value, self.minimax(board_copy, depth - 1, next_player))

        return value

    def opposite_player(self, color_arg):
        if color_arg == settings.RED:
            return settings.YELLOW
        else:
            return settings.RED

    def evaluate(self, board):
        '''
        Utility: 138 since the sum of self.evaluation_table is 276 (2 x 138).
        This allows an evaluation to lead to:
            < 0 if the opposing player has a better board position
            == 0 if both players have an equal position
            > 0 if this current player has a better position
        '''
        utility = 138
        award = 0

        for i in range(settings.ROWS):
            for j in range(settings.COLS):
                if board.board[i][j] == self.color:
                    award += self.evaluation_table[i][j]
                else:
                    award -= self.evaluation_table[i][j]
        
        return utility + award