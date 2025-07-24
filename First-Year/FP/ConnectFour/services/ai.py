from domain.board import Board
import numpy as np
import math
import random

class ComputerStrategy():
    def __init__(self, computer_id, human_id):
        """
        Initialize the AI strategy.
        :param computer_id: ID of the computer player (e.g., 2)
        :param human_id: ID of the opponent (e.g., 1)
        """
        self.computer = computer_id
        self.human = human_id
        self.width = 7
        self.height = 6

    def score_position(self, board):
        '''
        Evaluate the given board state and assign a score for the AI to use.
        :param board: Current state of the game board.
        :return: the score of the given board state - the sum of scores of all windows
        '''
        score = 0

        # Center column preference
        center_column = list(board.board[:, self.width // 2]) # list with all elements of center column
        center_count = center_column.count(self.computer)
        score += center_count * 3  # Central positions are more valuable

        # Score horizontal
        for row in range(self.height):
            row_array = list(board.board[row, :]) # all elements of current row
            for col in range(self.width - 3):
                window = row_array[col:col + 4] #every horizontal four position window of the row
                score += self.evaluate_window(window)

        # Score vertical
        for col in range(self.width):
            col_array = list(board.board[:, col])
            for row in range(self.height - 3):
                window = col_array[row:row + 4] #every vertical four position window of the column
                score += self.evaluate_window(window)

        # Score positive diagonals
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                window = [board.board[row + i][col + i] for i in range(4)]
                score += self.evaluate_window(window)

        # Score negative diagonals
        for row in range(3, self.height):
            for col in range(self.width - 3):
                window = [board.board[row - i][col + i] for i in range(4)]
                score += self.evaluate_window(window)

        return score

    def evaluate_window(self, window):
        '''
        Evaluate a specific window of four positions and assign a score.
        :param window: the given window of four positions
        :return: the score of the window
        '''
        score = 0
        if window.count(self.computer) == 4:
            score += 100
        elif window.count(self.computer) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(self.computer) == 2 and window.count(0) == 2:
            score += 2

        if window.count(self.human) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def get_valid_columns(self, board):
        '''
        Get a list of all columns where a piece can be dropped.
        :param board: Current state of the game board.
        :return: list of column indexes that are not full
        '''
        return [col for col in range(self.width) if board.board[self.height - 1, col] == 0]

    def get_next_open_row(self, board, col):
        """
        Get the next available row in the specified column.
        :param board: Current state of the game board.
        :param col: index of the given column
        :return: index of first available row
        """
        for row in range(self.height):
            if board.board[row][col] == 0:
                return row

    def drop_piece_simulated(self, board, row, col, piece):
        '''
        Simulate dropping a piece on a temporary board.
        :param board: Current state of the game board.
        :param row: index of the given row
        :param col: index of the given column
        :param piece: id of the player that drops the piece
        :return: none - the function modifies the current board state
        '''
        board.board[row][col] = piece

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """
        The Minimax algorithm with alpha-beta pruning - finds the best move the AI can do next, by evaluating the scores of possible board states
        :param board: Current state of the game board.
        :param depth: Remaining depth to explore in the game tree - the number of moves to simulate into the future
        :param alpha: Best score the maximizer(AI player) can guarantee so far.
        :param beta: Best score the minimizer(human player) can guarantee so far.
        :param maximizing_player: Boolean indicating if it's the AI's turn (True for AI).
        :return: A tuple (column, score) indicating the best that AI can do and its score.
        """
        valid_columns = self.get_valid_columns(board)

        if depth == 0: # no more moves to simulate
            return (None, self.score_position(board))

        if board.check_winner(self.computer):
            return (None, 1000000)
        elif board.check_winner(self.human):
            return (None, -1000000)
        elif board.is_full():  # Draw
            return (None, 0)

        if maximizing_player: # AI's turn
            value = -math.inf
            best_column = None
            for col in valid_columns:
                temp_board = board.copy()
                row = self.get_next_open_row(temp_board, col)
                self.drop_piece_simulated(temp_board, row, col, self.computer)
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    best_column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return best_column, value
        else:
            value = math.inf
            best_column = None
            for col in valid_columns:
                temp_board = board.copy()
                row = self.get_next_open_row(temp_board, col)
                self.drop_piece_simulated(temp_board, row, col, self.human)
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    best_column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_column, value

    def make_move(self, board):
        '''
        Determine the best move for the computer, by calling minimax function.
        :param board: Current state of the game board.
        :return: the index of the column where AI should drop the piece
        '''
        column, _ = self.minimax(board, 4, -math.inf, math.inf, True)
        return column