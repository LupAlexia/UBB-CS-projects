import unittest
import numpy as np
from domain.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_drop_piece(self):
        self.board.drop_piece(3, 1)
        self.assertEqual(self.board.board[0, 3], 1,"The piece should be dropped in the first available row of the specified column.")

        self.board.drop_piece(3, 2)
        self.assertEqual( self.board.board[1, 3], 2,"The next piece should stack on top of the first in the same column.")

    def test_is_full(self):
        self.assertFalse(self.board.is_full(), "A newly initialized board should not be full." )

        # Fill the board completely
        for col in range(7):
            for row in range(6):
                self.board.drop_piece(col, 1)

        self.assertTrue(
            self.board.is_full(), "The board should be full after all spots are filled."
        )

    def test_check_winner_horizontal(self):
        for col in range(4):
            self.board.drop_piece(col, 1)

        self.assertTrue(
            self.board.check_winner(1), "Human player should win with a horizontal line of four."
        )

    def test_check_winner_vertical(self):
        for _ in range(4):
            self.board.drop_piece(3, 2)

        self.assertTrue(
            self.board.check_winner(2), "Computer player should win with a vertical line of four."
        )

    def test_check_winner_diagonal_positive(self):
        self.board.drop_piece(0, 1)
        self.board.drop_piece(1, 2)
        self.board.drop_piece(1, 1)
        self.board.drop_piece(2, 2)
        self.board.drop_piece(2, 2)
        self.board.drop_piece(2, 1)
        self.board.drop_piece(3, 2)
        self.board.drop_piece(3, 2)
        self.board.drop_piece(3, 2)
        self.board.drop_piece(3, 1)

        self.assertTrue(
            self.board.check_winner(1), "Human player should win with a positive diagonal line of four."
        )

    def test_check_winner_diagonal_negative(self):
        self.board.drop_piece(3, 1)
        self.board.drop_piece(2, 2)
        self.board.drop_piece(2, 1)
        self.board.drop_piece(1, 2)
        self.board.drop_piece(1, 2)
        self.board.drop_piece(1, 1)
        self.board.drop_piece(0, 2)
        self.board.drop_piece(0, 2)
        self.board.drop_piece(0, 2)
        self.board.drop_piece(0, 1)

        self.assertTrue(
            self.board.check_winner(1), "Computer player should win with a negative diagonal line of four."
        )

    def test_copy(self):
        self.board.drop_piece(0, 1)
        copied_board = self.board.copy()
        self.assertEqual(
            copied_board.board[0, 0], 1, "The copied board should preserve the original board state."
        )

        copied_board.drop_piece(0, 2)
        self.assertNotEqual(
            self.board.board[1, 0], 2,
            "Modifying the copied board should not affect the original board."
        )
