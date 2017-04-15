import random

class Player(object):

    def __init__(self, player_name, player_type):
        self.name = player_name
        self.type = player_type
        self.attack = int(random.uniform(1, 5))
        self.defence = int(random.uniform(1, 5))
        self.life = int(random.uniform(10, 15))

    def player_type(self, number):
        return {
            1: 'ninja',
            2: 'pirate',
            3: 'viking'
        }[number]
