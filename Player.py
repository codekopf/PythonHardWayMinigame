import random


class Player(object):

    def __init__(self, player_name, player_type):
        self.name = player_name
        self.type = player_type
        self.attack = int(random.uniform(3, 8))
        self.defence = int(random.uniform(3, 8))
        self.life = int(random.uniform(20, 35))


    def to_string(self):
        print "Name: " + self.name + ", Life: " + `self.life` + ", Attack: " + `self.attack` + ", Defence: " + `self.defence`

    def player_type(self, number):
        return {
            1: 'ninja',
            2: 'pirate',
            3: 'viking'
        }[number]
