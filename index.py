import Engine
import Room
import Player

print "Plase insert your name:"
player_name = raw_input()

print """
Whom you choose to be?
 [1] Ninja
 [2] Pirate
 [3] Viking
"""
select_number = True
while(select_number):
    player_type = int(raw_input())
    print player_type
    if player_type >= 1 and player_type <= 3:
        select_number = False
    else:
        print "Please select one of the warrior type"

location = Room('arena')
player = Player(player_name, player_type)
game = Engine(player, location)
game.play()



# TODO
# * have a workable demo
# * create inventory for Hero
# * enemies and heores can have
# * set hero's name
# * set hero's type
# *** classic story vs. arena combat