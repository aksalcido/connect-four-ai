import unittest
import os
from python_settings import settings
from board import Board

os.environ["SETTINGS_MODULE"] = 'settings' 

class TestBoard(unittest.TestCase):
    '''
    Tests the board object for Connect Four.
    '''
    def setUp(self):
        self.board1 = Board()
        self.board2 = Board()

    def test_move(self):
        # Vertical Top Check #
        self.board1.move(1, settings.YELLOW)
        self.board1.move(2, settings.RED)
        self.board1.move(1, settings.YELLOW)
        self.board1.move(2, settings.RED)
        self.assertEqual(False, self.board1.check_vertical())

        self.board1.move(1, settings.RED)
        self.board1.move(1, settings.RED)
        self.board1.move(1, settings.RED)
        self.board1.move(1, settings.RED)
        self.assertEqual(True, self.board1.check_vertical())

        # Vertical Bottom Check #
        self.assertEqual(False, self.board2.check_vertical())
        self.board2.move(1, settings.RED)
        self.assertEqual(False, self.board2.check_vertical())
        self.board2.move(2, settings.YELLOW)
        self.board2.move(1, settings.RED)
        self.assertEqual(False, self.board2.check_vertical())
        self.board2.move(2, settings.YELLOW)
        self.board2.move(1, settings.RED)
        self.assertEqual(False, self.board2.check_vertical())
        self.board2.move(2, settings.YELLOW)
        self.board2.move(1, settings.RED)
        self.assertEqual(True, self.board2.check_vertical())

    def test_check_vertical(self):
        self.assertEqual(False, self.board1.check_vertical())
        self.board1.board[5][0] = settings.RED
        self.board1.board[4][0] = settings.RED
        self.board1.board[3][0] = settings.RED
        self.board1.board[2][0] = settings.RED
        self.assertEqual(True, self.board1.check_vertical())

        self.assertEqual(False, self.board2.check_vertical())
        self.board2.board[0][6] = settings.YELLOW
        self.board2.board[1][6] = settings.YELLOW
        self.board2.board[2][6] = settings.YELLOW
        self.board2.board[3][6] = settings.YELLOW
        self.assertEqual(True, self.board2.check_vertical())


    def test_check_horizontal(self):
        self.assertEqual(False, self.board1.check_horizontal())
        self.board1.board[0][0] = settings.RED
        self.board1.board[0][1] = settings.RED
        self.board1.board[0][2] = settings.RED
        self.board1.board[0][3] = settings.RED
        self.assertEqual(True, self.board1.check_horizontal())

        self.assertEqual(False, self.board2.check_horizontal())
        self.board2.board[5][3] = settings.YELLOW
        self.board2.board[5][4] = settings.YELLOW
        self.board2.board[5][5] = settings.YELLOW
        self.board2.board[5][6] = settings.YELLOW
        self.assertEqual(True, self.board2.check_horizontal())

    def test_check_diagonal_left(self):
        self.assertEqual(False, self.board1.check_diagonal_left())
        self.board1.board[0][6] = settings.RED
        self.board1.board[1][5] = settings.RED
        self.board1.board[2][4] = settings.RED
        self.board1.board[3][3] = settings.RED
        self.assertEqual(True, self.board1.check_diagonal_left())

        self.assertEqual(False, self.board2.check_diagonal_left())
        self.board2.board[5][0] = settings.YELLOW
        self.board2.board[4][1] = settings.YELLOW
        self.board2.board[3][2] = settings.YELLOW
        self.board2.board[2][3] = settings.YELLOW
        self.assertEqual(True, self.board2.check_diagonal_left())

    def test_check_diagonal_right(self):
        self.assertEqual(False, self.board1.check_diagonal_right())
        self.board1.board[2][0] = settings.RED
        self.board1.board[3][1] = settings.RED
        self.board1.board[4][2] = settings.RED
        self.board1.board[5][3] = settings.RED
        self.assertEqual(True, self.board1.check_diagonal_right())

        self.assertEqual(False, self.board2.check_diagonal_right())
        self.board2.board[5][6] = settings.YELLOW
        self.board2.board[4][5] = settings.YELLOW
        self.board2.board[3][4] = settings.YELLOW
        self.board2.board[2][3] = settings.YELLOW
        self.assertEqual(True, self.board2.check_diagonal_right())

    def test_tie(self):
        self.assertEqual(False, self.board1.winner())
        self.assertEqual(False, self.board1.tie())

        self.board1.board[5][0] = settings.YELLOW
        self.board1.board[5][1] = settings.RED
        self.board1.board[5][2] = settings.RED
        self.board1.board[5][3] = settings.YELLOW
        self.board1.board[5][4] = settings.YELLOW
        self.board1.board[5][5] = settings.RED
        self.board1.board[5][6] = settings.YELLOW

        self.board1.board[4][0] = settings.RED
        self.board1.board[4][1] = settings.RED
        self.board1.board[4][2] = settings.YELLOW
        self.board1.board[4][3] = settings.RED
        self.board1.board[4][4] = settings.RED
        self.board1.board[4][5] = settings.RED
        self.board1.board[4][6] = settings.YELLOW

        self.board1.board[3][0] = settings.YELLOW
        self.board1.board[3][1] = settings.YELLOW
        self.board1.board[3][2] = settings.RED
        self.board1.board[3][3] = settings.YELLOW
        self.board1.board[3][4] = settings.YELLOW
        self.board1.board[3][5] = settings.RED
        self.board1.board[3][6] = settings.YELLOW

        self.assertEqual(False, self.board1.winner())
        self.assertEqual(False, self.board1.tie())

        self.board1.board[2][0] = settings.RED
        self.board1.board[2][1] = settings.RED
        self.board1.board[2][2] = settings.RED
        self.board1.board[2][3] = settings.YELLOW
        self.board1.board[2][4] = settings.YELLOW
        self.board1.board[2][5] = settings.YELLOW
        self.board1.board[2][6] = settings.RED

        self.board1.board[1][0] = settings.YELLOW
        self.board1.board[1][1] = settings.YELLOW
        self.board1.board[1][2] = settings.RED
        self.board1.board[1][3] = settings.YELLOW
        self.board1.board[1][4] = settings.RED
        self.board1.board[1][5] = settings.RED
        self.board1.board[1][6] = settings.YELLOW

        self.board1.board[0][0] = settings.RED
        self.board1.board[0][1] = settings.RED
        self.board1.board[0][2] = settings.YELLOW
        self.board1.board[0][3] = settings.RED
        self.board1.board[0][4] = settings.YELLOW
        self.board1.board[0][5] = settings.YELLOW
        self.board1.board[0][6] = settings.RED

        self.assertEqual(False, self.board1.winner())
        self.assertEqual(True, self.board1.tie())

    def test_column_available(self):
        self.assertEqual(5, self.board1.column_available(1))
        self.assertEqual(5, self.board1.column_available(3))
        self.assertEqual(5, self.board1.column_available(7))

    def test_initialize_new_board(self):
        for i in range(settings.ROWS):
            for j in range(settings.COLS):
                self.assertEqual(self.board1.board[i][j], settings.EMPTY)

        self.board1.move(1, settings.YELLOW)
        self.board1.move(2, settings.RED)
        self.board1.move(1, settings.YELLOW)
        self.board1.move(2, settings.RED)

        self.board1.initialize_new_board()

        for i in range(settings.ROWS):
            for j in range(settings.COLS):
                self.assertEqual(self.board1.board[i][j], settings.EMPTY)


if __name__ == '__main__':
    unittest.main()