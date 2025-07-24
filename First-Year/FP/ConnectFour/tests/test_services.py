import random
import unittest
from services.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.computer = 2
        self.human = 1

    def test_human_drop_piece(self):
        self.game.board.board.fill(0)
        column = 3
        self.game.human_drop_piece(column)
        row = 0  # The first row should be filled
        self.assertEqual(self.game.board.board[row, column], 1, f"Human piece was not placed correctly at ({row}, {column}).")  # Human ID is 1

    def test_computer_drop_piece(self):
        self.game.board.board.fill(0)
        self.game.computer_drop_piece()
        # Ensure that a column has been updated with a computer piece (ID 2), we don't know which column that is
        self.assertTrue((self.game.board.board == 2).any(), "Computer did not drop the piece on the board!")

    def test_not_full_column(self):
        self.game.board.board.fill(0)
        # Test that a column is not full initially
        column = 4
        self.assertTrue(self.game.not_full_column(column), f"Expected column {column} to be not full, but it is full.")

        # Fill the column and test again
        for _ in range(6):
            self.game.human_drop_piece(column)
        self.assertFalse(self.game.not_full_column(column), f"Expected column {column} to be full after dropping pieces, but it is not.")

    def test_game_over(self):
        #Full board
        self.game.board.board.fill(0)
        self.assertFalse(self.game.game_over())
        self.game.board.board.fill(1)
        self.assertTrue(self.game.game_over(), "Expected game to be over when the board is full, but it is not.")

        #Human won
        self.game.board.board.fill(0)
        for column in range(4):
            self.game.human_drop_piece(column)
        self.assertTrue(self.game.game_over(), "Expected game to be over when the human wins, but it is not.")

        #Computer won
        self.game.board.board.fill(0)
        for col in range(4):
            self.game.board.drop_piece(col, self.game._computer)
        self.assertTrue(self.game.game_over(), "Expected game to be over when the computer wins, but it is not.")





