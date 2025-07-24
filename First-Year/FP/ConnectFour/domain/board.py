import numpy as np

class Board:
    def __init__(self):
        self._width = 7
        self._height = 6
        self._board = np.zeros((self._height, self._width), dtype=int)

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    
    def copy(self):
        """
        Makes a copy of the Board object
        :return: a new Board object with the same board state
        """
        new_board = Board()
        new_board.board = self.board.copy()
        return new_board

    def drop_piece(self, column, player):
        """
        Drop a piece for the current player, in the specified column.
        :param column: The column index where the piece is dropped.
        :param player: The player's ID
        :return: none - the function modifies the Board object
        """
        # drop piece in the first empty row
        for row in range(0, self._height):  # start from the bottom row
            if self._board[row, column] == 0:
                self._board[row, column] = player
                break

    def is_full(self):
        """
        Check if the board is full.
        :return: True if full, otherwise False.
        """
        return np.all(self._board != 0) # all elements are non-zero

    def check_winner(self, player):
        """
        Check if the specified player has won - there are four consecutive positions with his id
        :param player: The player's ID (usually 1 or 2).
        :return: True if the player has won, otherwise False.
        """
        # Check horizontal
        for row in range(self._height):
            for col in range(self._width - 3):
                if np.all(self.board[row, col:col + 4] == player):
                    return True

        # Check vertical
        for col in range(self._width):
            for row in range(self._height - 3):
                if np.all(self.board[row:row + 4, col] == player):
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(self._height - 3):
            for col in range(self._width - 3):
                if all(self.board[row + i, col + i] == player for i in range(4)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(3, self._height):
            for col in range(self._width - 3):
                if all(self.board[row - i, col + i] == player for i in range(4)):
                    return True
        return False