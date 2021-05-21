from python_settings import settings

class Board:

    def __init__(self):
        '''
        Initializes a board object. This object contains the contents for the current game state of the board.
        It essentially does the moving and winner checks but does not contain any of the game attributes 
        (e.g: players, current_turn, etc).
        '''
        self.board = self.initialize_new_board()

    def move(self, player_move: int, player_color: int):
        '''
        Makes a move based off player_move and player_color. Error checking is done before this
        function is called, so row is guaranteed to be available and the board[row][player_move - 1] is updated
        to reflect the move.
        '''
        row = self.column_available(player_move)
        self.board[row][player_move - 1] = player_color

    # ===== Move Validation Checking ===== #
    def valid_move(self, player_move) -> bool:
        '''
        Returns a bool:
            True if the player_move is a valid move that can be made. The requirements for validity
            is to be a column integer that ranges from [1-7] and the column has to be available,
            meaning the column can not be full. False otherwise.
        '''
        return player_move and player_move.isnumeric() and \
            self.in_bounds(int(player_move)) and self.column_available(int(player_move)) != settings.INVALID_COLUMN

    def in_bounds(self, player_move):
        '''
        Returns a bool:
            True if the player_move integer is within the range of [1-7], meaning it is a valid
            column argument. False otherwise.
        '''
        return player_move > 0 and player_move <= settings.COLS

    def column_available(self, column: int) -> int:
        '''
        Returns an int representing either a valid row that the player_move can be made in or INVALID_COLUMN
        to represent that the move can not be made in this column.
        '''
        for i in range(1, settings.ROWS + 1):
            if self.board[settings.ROWS - i][column - 1] == settings.EMPTY:
                return settings.ROWS - i
        
        return settings.INVALID_COLUMN

    # ===== Winner/Tie Checks ===== #
    def winner(self) -> bool:
        '''
        Returns a bool:
            True if any of the four in a row checks pass, meaning there is a winner on the board.
        '''
        return self.check_vertical() or self.check_horizontal() or self.check_diagonal_left() or self.check_diagonal_right()

    def tie(self):
        '''
        Returns a bool:
            True if there is a tie on the board, meaning there is no winner which is checked by self.winner() before this function
            is checked. A tie in Connect Four means every slot is full and there is no four in a row anywhere on the board.
            This function does that by checking if every piece on the top row is not empty, if it is not then we know there is 
            no more available columns for moves.
            False otherwise.
        '''
        for j in range(settings.COLS):
            if self.board[0][j] == settings.EMPTY:
                return False

        return True

    # ===== Four in a Row Checks ===== #
    def check_vertical(self) -> bool:
        '''
        Returns a bool:
            True if there is four in a row -- in a vertical line in the board that is not an empty slot but a piece color.
            False otherwise.
        '''
        for i in range(settings.ROWS - 3):
            for j in range(settings.COLS):
                if self.board[i][j] != settings.EMPTY and self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                    return True

        return False

    def check_horizontal(self) -> bool:
        '''
        Returns a bool:
            True if there is four in a row -- in a horizontal line in the board that is not an empty slot but a piece color.
            False otherwise.
        '''
        for i in range(settings.ROWS):
            for j in range(settings.COLS - 3):
                if self.board[i][j] != settings.EMPTY and self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                    return True
        
        return False
    
    def check_diagonal_right(self) -> bool:
        '''
        Returns a bool:
            True if there is four in a row -- in a diagonal right line towards the bottom right of the board; that is not an empty slot but a piece color.
            False otherwise.
        '''
        for i in range(settings.ROWS - 3):
            for j in range(settings.COLS - 3):
                if self.board[i][j] != settings.EMPTY and self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                    return True

        return False

    def check_diagonal_left(self) -> bool:
        '''
        Returns a bool:
            True if there is four in a row -- in a diagonal left line towards the bottom left of the board; that is not an empty slot but a piece color.
            False otherwise.
        '''
        for i in range(3, settings.ROWS):
            for j in range(settings.COLS - 3):
                if self.board[i][j] != settings.EMPTY and self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3]:
                    return True
        
        return False

    # ===== Display Methods ===== #
    def display(self):
        '''
        Prints the current board and displays to the user.
        '''
        print(self)
    
    def __repr__(self):
        '''
        Override the __repr__ method so that we are able to print a displayable board
        for the user.
        '''
        board_str = ""

        for i in range(settings.ROWS):
            row_str = "|"

            for j in range(settings.COLS):
                if self.board[i][j] == settings.RED:
                    row_str += 'R'
                elif self.board[i][j] == settings.YELLOW:
                    row_str += 'Y'
                else:
                    row_str += ' '
                
                row_str += '|'

            board_str += f'{row_str}\n'

        board_str += '---------------'

        return board_str

    # Initialization Method #
    def initialize_new_board(self) -> list:
        '''
        Initializes a new board and assigns to self.board. This function is called at initialization
        and when the player wishes to play again.
        '''
        new_board = []

        for i in range(settings.ROWS):
            new_row = []

            for j in range(settings.COLS):
                new_row.append(settings.EMPTY)

            new_board.append(new_row)
        
        self.board = new_board

        return self.board