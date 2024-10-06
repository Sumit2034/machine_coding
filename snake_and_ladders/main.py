from models.entities import Entities
from service.play_snake_ladder import PlaySnakeLadder

def main():
    entities = Entities.get_instance()

    no_of_snakes = int(input("Enter number of snakes: "))
    while no_of_snakes > 0:
        start_position = int(input("Enter snake start position: "))
        end_position = int(input("Enter snake end position: "))
        entities.set_snake(start_position, end_position)
        no_of_snakes -= 1

    no_of_ladders = int(input("Enter number of ladders: "))
    while no_of_ladders > 0:
        start_position = int(input("Enter ladder start position: "))
        end_position = int(input("Enter ladder end position: "))
        entities.set_ladders(start_position, end_position)
        no_of_ladders -= 1

    no_of_players = int(input("Enter number of players: "))
    for i in range(no_of_players):
        player = input("Enter player name: ")
        entities.set_player(i, player)

    play_snake_and_ladder = PlaySnakeLadder(6)
    winner = play_snake_and_ladder.play_game()
    print(f"{winner} wins the game")

if __name__ == "__main__":
    main()