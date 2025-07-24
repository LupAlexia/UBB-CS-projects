from ai import Ai
import unittest
import copy
from board import Board


class TestAi(unittest.TestCase):

    def test_simulate_drop(self):
        self._board = Board(False)
        self._ai = Ai(self._board)

        original_board = copy.deepcopy(self._board)
        result = self._ai.simulate_drop('x', 0, 0)

        self.assertEqual(original_board, self._board) #original board should not be modified after simulate function
        self.assertEqual(result._data[0][0], 'x')

    def test_strategy(self):
        self._board = Board(False)
        self._ai = Ai(self._board)

        #make human one step away from winning
        self._board.drop_piece('0',0, 0)
        self._board.drop_piece('0',0, 1)
        self._board.drop_piece('0',0, 2)
        self._board.drop_piece('0',0, 3)
        self._board.drop_piece('0',0, 4)

        symbol, row, column = self._ai.strategy()
        self.assertEqual(symbol, 'x')
        self.assertEqual(self._board._data[0][5], symbol)

        #check random move
        self._board = Board(False)
        self._ai = Ai(self._board)

        symbol, row, column = self._ai.strategy()
        self.assertEqual(self._board._data[row][column], symbol)
        self.assertTrue(0 <= row <= 5)
        self.assertTrue(0 <= column <= 5)

    
    if __name__ == "__main__":
        unittest.main()
