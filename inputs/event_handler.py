import inputs
import pygame

class Event_handler:
    def __init__(self, game):
        self.game = game
        self.menu_buttons = [
            inputs.Button(290, 350, *self.game.display.menu.pokedex_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.POKEDEX, self.game.sound.play_click_sound)),            
            inputs.Button(460, 350, *self.game.display.menu.combat_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.COMBAT, self.game.sound.play_click_sound)) 
           ]

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menu_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        button.click()
                        
    def execute_multiple(self, func1, arg1, func2):
        func1(arg1)
        func2()