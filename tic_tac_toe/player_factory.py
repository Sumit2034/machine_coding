from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_symbol(self):
        return self.symbol

    @abstractmethod
    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self, board):
        # Implementation for making a move
        pass

    def update(self, board):
        # Implementation to update player with board state
        pass


class PlayerFactory:
    @staticmethod
    def create_player(symbol):
        return HumanPlayer(symbol)
