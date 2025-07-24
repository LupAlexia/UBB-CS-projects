from services.game import Game

class UI:
    def __init__(self):
        self.__game = Game()
        self.__computer = 2
        self.__human = 1
        self.__turn = self.__human
        self.__tokens = ["\U000026aa", "\U0001f534", "\U000026AB"]
        self.__width = 7
        self.__height = 6

    def is_valid_column(self, column):
        try:
            if column < 1 or column > self.__width:
                raise ValueError("Column out of bounds!")
            if not self.__game.not_full_column(column - 1):
                raise ValueError("Column is full!")
            return True
        except ValueError as e:
            print(e)
            return False

    def human_turn(self):
        column = int(input("Select the column (1-7): "))
        if self.is_valid_column(column):
            column -= 1
            self.__game.human_drop_piece(column)
        else:
            self.human_turn()

    def computer_turn(self):
        self.__game.computer_drop_piece()

    def display_board(self):
        for i in range(self.__width): #header
            print(" " + str(i + 1), end = " ")

        print()
        board = self.__game.display_board()
        for row in board:
            for column in row:
                print(self.__tokens[column], end=" ")
            print()
        print()

    def display_result(self):
        if self.__game.board.check_winner(self.__computer):
            print("Computer won!")
        elif self.__game.board.check_winner(self.__human):
            print("You won!")
        else:
            print("It's a draw!")

    def start(self):
        print("Welcome to Connect 4 game! This is a human player vs computer player game.")
        while not self.__game.game_over():
            if self.__turn == self.__human: # human's turn
                print("Is your turn!")
                self.human_turn()
                self.__turn  = self.__computer
            else:
                print("Is computer's turn!")
                self.computer_turn()
                self.__turn = self.__human

            self.display_board()

        self.display_result()
