from math import expm1
from selectors import SelectSelector
import os
import texttable

class Board:
    def __init__(self, from_file):
        self._text_file = "text_file"

        if from_file:
            self._data = self.load_from_file(self._text_file)
        else:
            self._data = [[" " for i in range(6)] for j in range(6)]

    def __str__(self):
        board = texttable.Texttable()
        board.add_rows(self._data, header=False)
        return board.draw()

    def __eq__(self, other):
        return self._data == other._data

    def drop_piece(self, piece, row, col):
        self._data[row][col] = piece
        self.save_to_file(self._text_file)

    def board_full(self):
        for i in range(6):
            for j in range(6):
                if self._data[i][j] != "x" or self._data[i][j] != "0":
                    return False
        return True

    def is_valid_location(self, row, col):
        return self._data[row][col] == " "

    def winning_board(self):
        # check lines
        for i in range(6):
            for j in range(2):
                if self._data[i][j] == self._data[i][j + 1] == self._data[i][j + 2] == self._data[i][j + 3] == self._data[i][j + 4] != " ":
                    return True
        # check columns
        for j in range(6):
            for i in range(2):
                if self._data[i][j] == self._data[i + 1][j] == self._data[i + 2][j] == self._data[i + 3][j] == self._data[i + 4][j] != " ":
                    return True
        # check diagonals - left ->right
        for i in range(2):
            for j in range(2):
                if self._data[i][j] == self._data[i + 1][j + 1] == self._data[i + 2][j + 2] == self._data[i + 3][j + 3] == self._data[i + 4][j + 4] != " ":
                    return True
        #check diagonal - right -> left
        for i in range(2):
            for j in range(2):
                if self._data[i][5 - j] == self._data[i + 1][5 - j - 1] == self._data[i + 2][5 - j - 2] == self._data[i + 3][5 - j - 3] == self._data[i + 4][5 - j - 4] != " ":
                    return True

    def load_from_file(self, file_name):
        try:
            if not os.path.exists(file_name):
                return []

            with open(file_name, "r") as file:
                lines = file.readlines()

                data = []
                for line in lines:
                    if '|' in line: #skip decorative lines
                        #remove leading/ending |
                        line = line.strip()
                        line = line.strip('|')
                        columns = line.split('|') #split line by columns => the cells
                        row = []
                        for cell in columns:
                            cell = cell.strip()
                            if cell == "":
                                cell = " "
                            row.append(cell)
                        if row:
                            data.append(row)
                return data
        except IOError:
            pass

    def save_to_file(self, file_name):
        try:
            with open(file_name, "w") as file:
                file.write(str(self))
        except IOError:
            pass
