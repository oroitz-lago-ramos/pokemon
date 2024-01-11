from pygame import mixer

class Sound:
    def __init__(self, game):
        self.game = game
        mixer.init()

    def stop(self):
        mixer.music.stop()