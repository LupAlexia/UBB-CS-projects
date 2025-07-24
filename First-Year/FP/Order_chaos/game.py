from board import Board
from ai import Ai

class Game:
    def __init__(self, from_file):
        self.board = Board(from_file)
        self.turn = 0 # 0 = human 1 = ai
        self.game_over = False
        self.ai = None

    def human_drop_piece(self, symbol, row, col):
        if not self.board.is_valid_location(row - 1, col - 1):
            raise ValueError("There is already a piece in that location")
        self.board.drop_piece(symbol, row - 1, col - 1)

    def ai_drop_piece(self):
        self.ai = Ai(self.board)
        symbol, row, column = self.ai.strategy()
        self.board.drop_piece(symbol, row, column)

    def human_won(self):
        return self.board.winning_board()
    def ai_won(self):
        return self.board.board_full()

