from imaplib import Flags

import game
from game import Game

class Ui:
    def __init__(self):
        self.game = None
        self.turn = 0 # 0 = human 1 = ai

    def start_game(self):
        print("Choose an option:")
        print("1. Resume an existing game")
        print("2. Start a new game")

        choice = int(input("> "))
        if choice == 2:
            self.game = Game(False)
        else:
            self.game = Game(True)

        print(self.game.board)
        while not (self.game.ai_won() or self.game.human_won()):
            if self.turn == 0: # human turn
                print("Human's turn: ")
                symbol = input("choose a symbol: x or 0: ")
                row = input("row = ")
                col = input("col = ")

                try:
                    row = int(row)
                    col = int(col)
                    if symbol not in ['x', '0']:
                        raise ValueError("Invalid symbol")
                    if row < 1 or row > 6 or col < 1 or col > 6:
                        raise ValueError("Row and column should be integers between 1 and 6")

                    self.game.human_drop_piece(symbol, row, col)
                    self.turn = 1
                    print(self.game.board)
                except ValueError as e:
                    print(e)
            else: # Ai turn
                print("Ai's turn: ")
                self.game.ai_drop_piece()
                self.turn = 0
                print(self.game.board)

        self.print_result()

    def print_result(self):
        if self.game.ai_won():
            print("AI won!")
        elif self.game.human_won():
            print("Human won!")

