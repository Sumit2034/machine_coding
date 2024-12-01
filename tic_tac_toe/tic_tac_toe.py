from tic_tac_toe.board import Board
from tic_tac_toe.game_controller import GameController
from tic_tac_toe.move import DefaultMoveStrategy, DefaultWinStrategy
from tic_tac_toe.player_factory import PlayerFactory


class TicTacToe:
    def __init__(self):
        game_controller = GameController()  # Singleton game controller
        self.board = Board(3)
        self.player1 = PlayerFactory.create_player('X')
        self.player2 = PlayerFactory.create_player('O')
        self.current_player = self.player1
        self.move_strategy = DefaultMoveStrategy()
        self.win_strategy = DefaultWinStrategy()
        self.board.add_observer(self.player1)
        self.board.add_observer(self.player2)

    def play_game(self):
        while True:
            print(f"Player {self.current_player.get_symbol()}'s turn")
            x = int(input("Enter row (0, 1, or 2): "))
            y = int(input("Enter column (0, 1, or 2): "))

            # Validate move
            if self.move_strategy.is_valid_move(self.board, x, y):
                # Update board
                self.board.update_board(x, y, self.current_player.get_symbol())

                # Check for win
                if self.win_strategy.check_win(self.board, self.current_player.get_symbol()):
                    print(f"Player {self.current_player.get_symbol()} wins!")
                    break

                # Check for draw
                if self.is_draw():
                    print("Game is a draw!")
                    break

                # Switch player
                self.switch_player()
            else:
                print("Invalid move! Try again.")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def is_draw(self):
        for i in range(self.board.get_size()):
            for j in range(self.board.get_size()):
                if self.board.get_cell(i, j) == '':  # Empty cell is represented by ''
                    return False
        return True


# Assuming the GameController singleton and related classes are defined
if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
