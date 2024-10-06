from collections import defaultdict

from models.dice import Dice
from models.entities import Entities


class PlaySnakeLadder:

    def __init__(self, N) -> None:
        self.player_latest_position = {}
        self.entities = Entities.get_instance()
        self.dice = Dice(N)
    
    def play_game(self):
        self.initialize_players_start_value()
        i = -1
        while True:
            i += 1

            if i >= len(self.entities.get_players()):
                i = 0
            player_name = self.entities.get_players()[i]
            dice_number = self.dice.roll()
            end_position = self.player_latest_position[player_name] + dice_number
            result_str = f"{player_name} rolled a {dice_number} and moved from {self.player_latest_position[player_name]}"
            sl = ""

            if self.check_for_dice_number_greater_than_100(end_position):
                if end_position in self.entities.get_snakes():
                    sl = " after Snake dinner"
                    self.player_latest_position[player_name] = self.entities.get_snakes()[end_position]
                elif end_position in self.entities.get_ladders():
                    sl = " after Ladder ride"
                    self.player_latest_position[player_name] = self.entities.get_ladders()[end_position]
                else:
                    self.player_latest_position[player_name] = end_position

                result_str += f" to {self.player_latest_position[player_name]}{sl}"
                print(result_str)
            
            if self.is_player_won(player_name):
                break
        return player_name

            

    def is_player_won(self, player):
        return self.player_latest_position[player] == 100

    def initialize_players_start_value(self):
        for player_name in self.entities.get_players().values():
            self.player_latest_position[player_name] = 0

    def check_for_dice_number_greater_than_100(self, end_position):
        return end_position <= 100


