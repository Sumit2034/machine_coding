class Board:
    def __init__(self, size):
        self.board = [['' for _ in range(size)] for _ in range(size)]  # 2D board initialized with empty strings
        self.observers = []  # List to store the player observers

    def add_observer(self, player):
        self.observers.append(player)

    def notify_observers(self):
        for player in self.observers:
            player.update(self)

    def update_board(self, x, y, symbol):
        self.board[x][y] = symbol  # Update the board with the player's symbol
        self.notify_observers()  # Notify all players about the board update

    def get_cell(self, x, y):
        return self.board[x][y]

    def get_size(self):
        return len(self.board)
