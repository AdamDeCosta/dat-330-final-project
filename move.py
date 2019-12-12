from easygopigo3 import EasyGoPiGo3
from time import time, sleep


def default_move(self):
    while True:
        self.bot.speed(75)
        self.bot.forward(10)

def end_interaction_move(self):
    self.bot.speed(200)
    self.bot.turn_degrees(180)
    self.bot.forward(10)