class Engine(object):

    def __init__(self, player, location):
        self.player = player
        self.location = location

    def play(self):
        current_scene = self.location
        next_scene = True

        while next_scene:
            next_scene = current_scene.enter()

            if next_scene != 'finished':
                current_scene = self.location.next_scene(next_scene)
            else:
                break