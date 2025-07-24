from domain.board import Board
import numpy as np
import math
import random
from services.ai import ComputerStrategy

class Game:
    def __init__(self):
        self._board = Board()
        self._computer = 2
        self._human = 1
        self._strategy = ComputerStrategy(self._computer, self._human)
        self._width = 7
        self._height = 6

    @property
    def board(self):
        return self._board

    def display_board(self):
        '''
        Flips the board vertically, to get the printable version
        :return: the board that will be printed in the ui module
        '''
        return np.flip(self.board.board, 0)

    def human_drop_piece(self, column):
        '''
        Drops a piece for the human player, in the specified column
        :param column: the given column
        :return: none - the function modifies the current board state
        '''
        self.board.drop_piece(column, self._human)

    def computer_drop_piece(self):
        '''
        Drops a piece for the computer player, in the column determined by the AI strategy
        :return: none - the function modifies the current board state
        '''
        column = self._strategy.make_move(self.board)
        self.board.drop_piece(column, self._computer)

    def not_full_column(self, column):
        '''
        Checks if the given column is full or not
        :param column: the given column
        :return: boolean - true <=> the column is not full
        '''
        return self.board.board[self._height - 1, column] == 0

    def game_over(self):
        '''
        Checks if the game is over <=> the board is full or one of the players won
        :return: boolean - true <=> the game is over
        '''
        return (self.board.is_full() or self.board.check_winner(self._human) or self.board.check_winner(self._computer))