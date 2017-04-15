import random


class Monster(object):

    def __init__(self):
        monsters = ["krokodile", "Mike Wazowski", "pterodactil"]
        self.name = random.choice(monsters)
        self.attack = int(random.uniform(1, 5))
        self.defence = int(random.uniform(1, 5))
        self.life = int(random.uniform(10, 15))

    def to_string(self):
        print "Name: " + self.name + ", Life: " + `self.life` + ", Attack: " + `self.attack` + ", Defence: " + `self.defence`