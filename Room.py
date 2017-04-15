from Arena import Arena

class Room(object):

    rooms = {
        'arena': Arena(),
        'NaN': 'nothing',
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.rooms.get(scene_name)