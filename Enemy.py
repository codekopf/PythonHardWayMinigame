import random

class Enemy(object):

    def __init__(self):
        monsters = ["krokodile", "Mike Wazowski", "pterodactil"]
        self.type = monsters[random.choice(len(monsters))]
        self.attack = int(random.uniform(1, 5))
        self.defence = int(random.uniform(1, 5))
        self.life = int(random.uniform(10, 15))