import sounds
from pygame import mixer

class Sound_effect(sounds.Sound):
    def __init__(self, game):
        super().__init__(game)
        self.click_sound = mixer.Sound('assets/sounds/click.mp3')
        # self.pokeball_sound = mixer.Sound('/assets/sounds/pokeball.wav')

    def play_click_sound(self):
        self.click_sound.play()

    # def play_pokeball_sound(self):
    #     self.pokeball_sound.play()