class Fight(object):

    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def autofight(self):

        death = False
        while not death:

            ## Player attack
            demage = self.monster.defence - self.player.attack
            if demage < 0:
                print self.player.name + " made " + `abs(demage)`
                self.monster.life -= abs(demage)
            else:
                print "No demage"

            print self.player.name + " life is " + `self.player.life`

            ## Monster attack
            demage = self.player.defence - self.monster.attack
            if demage < 0:
                print self.monster.name + " made " + `abs(demage)`
                self.player.life -= abs(demage)
            else:
                print "No demage"

            print self.monster.name + " life is " + `self.monster.life`

            if self.player.life <= 0 or self.monster.life <= 0:
                death = True
