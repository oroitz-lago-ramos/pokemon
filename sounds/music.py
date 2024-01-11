from pygame import mixer
import sounds

class Music(sounds.Sound):
    def __init__(self, game):
        super().__init__(game)

    def start_menu_music(self):
        mixer.music.load('assets/musics/menu.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play()

    def start_combat_music(self):
        mixer.music.load('assets/musics/combat.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play()

    def choose_music(self):
        if self.game.current_state() == self.game.MENU:
            self.start_menu_music()
        elif self.game.current_state() == self.game.COMBAT:
            self.start_combat_music()