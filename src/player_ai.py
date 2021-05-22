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
            Returns a better move based off the minimax algorithm and our evaluation function based off piece positioning.
        '''
        move_dict = dict()
        highest_value = self.minimax(deepcopy(board), settings.MAX_DEPTH, self.color, move_dict)

        for move in move_dict.keys():
            if move_dict[move] == highest_value:
                return str(move)

        return str(-1)

    def minimax(self, board, depth, maximizing_player, move_dict) -> int:
        '''
        Minimax algorithm that is a decision rule for evaluating the best move to make on the current board.
        Minimizes the possible loss for a worst case scenario. Recursive algorithm for choosing the next move
        and returns multiple values using our evaluate function for different board states. The AI wants to get
        the maximum valued move and minimize the opposing player's.

        Returns:
            An integer representing the highest value of the moves that can be made on the board state. At MAX_DEPTH,
            we add those possible column moves to move_dict and assign the value to the respective column that led to it.
            We return the max value and use it in best_move to find the respective column and make the move.
        '''
        if depth == 0 or board.gameover():
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
                board_copy.move(moves[i], maximizing_player)
                value = max(value, self.minimax(board_copy, depth - 1, next_player, move_dict))

                # Only reaches here top level and adds the value of each move to the move_dict so that we can access it later
                if depth == settings.MAX_DEPTH:
                    move_dict[moves[i]] = value

        # AI is looking for the min value that can be gained from the opposing player
        else:
            value = inf

            for i in range(len(moves)):
                board_copy = deepcopy(board)
                board_copy.move(moves[i], maximizing_player)
                value = min(value, self.minimax(board_copy, depth - 1, next_player, move_dict))

        return value

    def evaluate(self, board):
        '''
        Evaluates the current board state and returns an integer score for that board state.
        This score reflects the value of the board for the AI and is compared with other board
        values. The AI is looking for the highest value that can be gained for itself, so the scoring
        is as follows:

        utility: settings.UTILITY_VALUE (138) since the sum of self.evaluation_table is 276 (138 * 2)
        award: Adds value of self.evaluation_table[i][j] if piece_color is equal to the AI's, subtracts otherwise.

        This allows an evaluation to lead to:
            < 0 if the opposing player has a better board position
            == 0 if both players have an equal position
            > 0 if this current player has a better position
        
        Unless there is a win condition on the board:
            If the win is positive for the evaluator, there is a huge gain,
            but if the win is for the opposing player, there is a huge loss.

        Returns:
            An integer: utility + award
        '''
        utility = settings.UTILITY_VALUE
        award = 0

        # boards that have a winner() result in the highest gain/loss since they take priority
        if board.get_winner() == self.color:
            award += settings.WINNER_AWARD
        elif board.get_winner() == self.opposite_player(self.color):
            award -= settings.WINNER_AWARD

        # adds/subtracts piece colors on the board depending on their position
        for i in range(settings.ROWS):
            for j in range(settings.COLS):
                if board[i, j] == self.color:
                    award += self.evaluation_table[i][j]
                elif board[i, j] == self.opposite_player(self.color):
                    award -= self.evaluation_table[i][j]
        
        return utility + award

    def opposite_player(self, color_arg):
        '''
        Returns the opposite_player of the color_arg:
            color_arg = settings.RED    -> Return: settings.YELLOW
            color_arg = settings.YELLOW -> Return: settings.RED
        '''
        if color_arg == settings.RED:
            return settings.YELLOW
        else:
            return settings.RED