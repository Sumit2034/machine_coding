import random

class Dice:
    def __init__(self, number_of_dice):
        self.number_of_dice = number_of_dice
        self.MIN = 1

    def roll(self):
        return random.randint(self.MIN, self.number_of_dice)
