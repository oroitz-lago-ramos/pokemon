import pygame
from pygame import mixer
class Sound:
    def __init__(self,game) -> None:
        self.game = game
        
        mixer.init()
        self.click_sound = mixer.Sound('assets/sounds/click.mp3')
        
    
    def start_menu_music(self):
        mixer.music.load('assets/musics/menu.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()
    
    def start_combat_music(self):
        mixer.music.load('assets/musics/combat.mp3')
        mixer.music.set_volume(1)
        mixer.music.play()
        
    def play_click_sound(self):
        self.click_sound.play()
    
    def play_pokeball_sound(self):
        self.click_sound.play()

    def stop(self):
        mixer.music.stop()
        
    def choose_music(self):
        if self.game.current_state() == self.game.MENU:
            self.start_menu_music()
        elif self.game.current_state() == self.game.COMBAT:
            self.start_combat_music()