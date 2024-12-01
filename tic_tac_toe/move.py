from abc import ABC, abstractmethod

class MoveStrategy(ABC):
    @abstractmethod
    def is_valid_move(self, board, x, y):
        pass


class WinStrategy(ABC):
    @abstractmethod
    def check_win(self, board, symbol):
        pass


class DefaultMoveStrategy(MoveStrategy):
    def is_valid_move(self, board, x, y):
        # Checking if the cell is empty (in Python, assume '' is an empty cell)
        return board.get_cell(x, y) == ''


class DefaultWinStrategy(WinStrategy):
    def check_win(self, board, symbol):
        size = board.get_size()
        
        # Check rows and columns
        for i in range(size):
            if self.check_row(board, symbol, i) or self.check_column(board, symbol, i):
                return True
        
        # Check diagonals
        return self.check_diagonal(board, symbol) or self.check_anti_diagonal(board, symbol)

    def check_row(self, board, symbol, row):
        for i in range(board.get_size()):
            if board.get_cell(row, i) != symbol:
                return False
        return True

    def check_column(self, board, symbol, col):
        for i in range(board.get_size()):
            if board.get_cell(i, col) != symbol:
                return False
        return True

    def check_diagonal(self, board, symbol):
        for i in range(board.get_size()):
            if board.get_cell(i, i) != symbol:
                return False
        return True

    def check_anti_diagonal(self, board, symbol):
        size = board.get_size()
        for i in range(size):
            if board.get_cell(i, size - 1 - i) != symbol:
                return False
        return True
