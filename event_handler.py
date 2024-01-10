import pygame
from game import *
from button import *

class Event_handler:
    def __init__(self, game):
        self.game = game
        self.menu_buttons = [
            Button(290, 350, *self.game.get_display().pokedex_rect.size, lambda: self.game.change_current_state(self.game.POKEDEX)),            
            Button(460, 350, *self.game.get_display().combat_rect.size, lambda: self.game.change_current_state(self.game.COMBAT))            
           
           ]

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menu_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        button.click()