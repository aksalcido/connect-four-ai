from python_settings import settings
from random import randint
from board import Board
from player import Player
from player_ai import PlayerAI

class ConnectFour:

    def __init__(self, player1, player2):
        '''
        Initializes a ConnectFour game object. This object contains both players, the board, and all of the
        game attributes associated to the game state. The game is ran through this object.
        '''
        # Connect Four Objects #
        self.board = Board()
        self.player1 = self.create_player(player1, settings.RED)
        self.player2 = self.create_player(player2, settings.YELLOW)
        
        # Game Settings #
        self.current_turn_player = self.decide_first_move()
        self.gameover = False
        self.last_winner = None
        self.tie = False

    def play(self) -> None:
        '''
        Runs the entirity of the Connect Four game in this method.
        '''
        print("Connect Four Started")
        
        while not self.gameover:
            self.board.display()
            self.progress_turn()

        self.board.display()

    def progress_turn(self) -> None:
        '''
        Handles an individual turn at a time. Each turn in Connect Four consists of
        an input from the Player and winner check after each move. If the check determines
        that there is still no winner OR tie, then the next_turn is called and displayed.
        '''
        self.handle_move()
        self.check_for_gameover()

        if not self.gameover:
            self.next_turn()
            self.display_next_turn()
    
    def handle_move(self) -> None:
        '''
        Handles the move aspect of each turn. Takes input from user and validates it
        until it is a proper move that can be made on the board. Once the move is
        validated, the move is made on the board to reflect the move changes.
        '''
        player_move = None

        while not self.board.valid_move(player_move):
            player_move = self.current_turn_player.get_move(board=self.board)
        
        self.board.move(int(player_move), self.current_turn_player.get_color())
    
    def next_turn(self) -> None:
        '''
        Switches the current_turn_player attribute to reflect the opposite player
        after the current player makes a move. Only called if the game is not over.
        '''
        if self.current_turn_player == self.player1:
            self.current_turn_player = self.player2
        else:
            self.current_turn_player = self.player1

    # ===== Game Ending Functions ===== #
    def check_for_gameover(self) -> None:
        '''
        Checks if there is a winner OR tie on the board. If there is, sets the attribute
        gameover to True. The game will proceed to end.
        '''
        if self.board.winner():
            self.gameover = True
        else:
            self._check_for_tie()
    
    def _check_for_tie(self) -> None:
        '''
        Checks if there is a tie on the board. If there is, sets the attribute
        gameover to True. The game will proceed to end with no winners.
        '''
        if self.board.tie():
            self.gameover = True
            self.tie = True

    # ===== Display Functions ===== #
    def display_next_turn(self) -> None:
        '''
        Displays the next turn, this function is called after the current_turn_player is changed
        hence displaying the next player's turn.
        '''
        if self.current_turn_player.get_color() == settings.RED:
            print("Player1 (RED)'s Turn to Move")
        else:
            print("Player2 (YELLOW)'s Turn to Move")

    def display_game_results(self) -> None:
        '''
        Handles and displays the game results. Game can end in Win or Tie, so both cases
        are handled depending on if a tie was found or not.
        '''
        if self.tie:
            self._handle_and_display_tie()
        else:
            self._handle_and_display_winner()

    def _handle_and_display_winner(self) -> None:
        '''
        If winner, last_winner is assigned to the player that made the last move since
        a winning game state was verified after their last move. Their win count
        is then incremented and the player that won is announced.
        '''
        self.last_winner = self.current_turn_player
        self.current_turn_player.add_win()

        if self.current_turn_player.get_color() == settings.RED:
            print("Player1 (RED) Wins!")
        else:
            print("Player2 (YELLOW) Wins!")

    def _handle_and_display_tie(self) -> None:
        '''
        last_winner is assigned to None since neither players ended with a win. It is then
        announced that the game ended in a Tie.
        '''
        self.last_winner = None
        print("Tie!")

    def display_overall_results(self) -> None:
        ''' 
        Displays all of the current wins for both players. This function is called
        after a game has been completed.
        '''
        print('-' * 30)
        print("Current Wins: ")
        player1_ai = ""
        player2_ai = ""
        print(f"Player1 ({self.player1.get_player_str()}): {self.player1.get_wins()} --- Player2 ({self.player2.get_player_str()}): {self.player2.get_wins()}")
        print('-' * 30)


    # ===== Initialization Methods ===== #
    def create_player(self, player, piece_color) -> Player or PlayerAI:
        '''
        Creates a Player object that will be playing Connect Four. The Player object will 
        either be a human player of type 'Player' or an AI of type 'PlayerAI.'
        '''
        if player == settings.HUMAN_PLAYER:
            return Player(piece_color)
        else:
            return PlayerAI(piece_color)

    def decide_first_move(self) -> Player:
        '''
        Rolls a random int representing the piece colors red or yellow.
        Whichever random int is returned by randint gets to make the first move.
        '''
        randomize_turn = randint(settings.RED, settings.YELLOW)
        
        if randomize_turn == settings.RED:
            print("Player1 -- (RED) is first!")
            return self.player1
        else:
            print("Player2 -- (YELLOW) is first!")
            return self.player2
        
    def restart(self) -> None:
        '''
        Restarts and resets the gamestate. Essentially initializing a new board,
        choosing a new player to move first, and setting attributes back to their original
        state.
        '''
        self.board.initialize_new_board()
        self.current_turn_player = self.decide_first_move()
        self.gameover = False
        self.tie = False
    
    # ===== Get Methods ===== #
    def get_last_winner(self) -> None or Player or PlayerAI:
        '''
        Returns the last_winner:
            None if no last_winner occured or a player object.
        '''
        return self.last_winner