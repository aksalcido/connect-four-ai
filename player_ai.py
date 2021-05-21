from python_settings import settings
from player import Player
from random import randint

# Initialize settings.py as environment variable
import os
os.environ["SETTINGS_MODULE"] = 'settings' 

class PlayerAI(Player):
    
    def __init__(self, color, difficulty = settings.EASY):
        self.difficulty = difficulty
        super().__init__(color)

    def get_move(self, **kwargs) -> str:
        '''
        Overrides get_move() from the parent class 'Player' and returns
        a move based off the board and difficulty mode of the AI.
        '''
        board = kwargs['board']

        if self.difficulty == settings.EASY:
            return self.random_move(board)
        if self.difficulty == settings.MEDIUM:
            return self.better_move(board)
        else:
            return self.best_move(board)

    def random_move(self, board) -> str:
        '''
        Easy Difficulty: 
            Returns a random column move.
        '''
        return str(randint(1, settings.COLS))

    def better_move(self, board) -> str:
        '''
        Medium Difficulty:
            Returns a better move.
        '''
        pass

    def best_move(self, board) -> str:
        '''
        Hard Difficulty:
            Returns the best move.
        '''
        pass