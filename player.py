from python_settings import settings

class Player:
    
    def __init__(self, color):
        '''
        Initializes a Player object that possesses their piece color and total win count.
        The player takes input from their respective user and returns the move to get
        validated.
        '''
        self.color = color
        self.wins = 0

    def get_move(self, **kwargs) -> str:
        '''
        Takes input from the respective player and return it to be validated. This function
        will be called until a valid move is made. None of the validation is done on the Player
        object's side.
        '''
        user_move = input("Input an int column from [1-7]: ")
        return user_move

    def get_color(self) -> int:
        '''
        Return the piece color that the player object has ownership of.
        '''
        return self.color

    def get_wins(self) -> int:
        '''
        Return the total number of wins for the respective player.7u
        '''
        return self.wins

    def add_win(self) -> None:
        '''
        Increments the total wins, this function is only called after a win is made for the
        respective player.
        '''
        self.wins += 1
    