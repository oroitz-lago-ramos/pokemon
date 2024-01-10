import pygame
from pygame import mixer
class Sound:
    def __init__(self) -> None:
        mixer.init()
        
    
    def start_menu_music(self):
        mixer.music.load('assets/music/menu.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()
    
    def start_combat_music(self):
        mixer.music.load('assets/music/combat.mp3')  # replace with the path to your combat music file
        mixer.music.set_volume(0.2)
        mixer.music.play()
        
    def stop(self):
        mixer.music.stop()