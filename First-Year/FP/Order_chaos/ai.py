from board import Board
import copy
import random

class Ai:
    def __init__(self, board):
        self.board = board

    def simulate_drop(self, symbol, row, col):
        temp_board = copy.deepcopy(self.board)
        temp_board.drop_piece(symbol, row, col)
        return temp_board

    def strategy(self):
        """
        Determines a strategy for making a move in the game. The function first attempts
        to block the opponent's direct winning opportunity by simulating potential moves on the game board. If no
        blocking move is identified, it selects a random valid location and
        drops a piece there.
        :param self: Instance of the class calling this method.
        :return: A tuple containing the symbol ('0' or 'x') representing the piece symbol dropped by Ai,
        the row index where the piece is placed, and the column index where the piece is placed.
        """
        #stop direct winning
        for row in range(6):
            for col in range(6):
                if self.board.is_valid_location(row, col):
                    temp_board = self.simulate_drop('0', row, col)
                    if temp_board.winning_board():
                        self.board.drop_piece('x', row, col)
                        return 'x', row, col

                    temp_board = self.simulate_drop('x', row, col)
                    if temp_board.winning_board():
                        self.board.drop_piece('0', row, col)
                        return '0', row, col

        #if not => random move
        symbol = random.choice(['0', 'x'])
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        while not self.board.is_valid_location(row, col):
            row = random.randint(0, 5)
            col = random.randint(0, 5)

        self.board.drop_piece(symbol, row, col)
        return symbol, row, col
