import inputs
import pygame

class Event_handler:
    def __init__(self, game, display, fight) -> None:
        self.game = game
        self.display = display
        self.fight = fight
        
        self.menu_buttons = [
            inputs.Button(290, 350, *self.display.menu.pokedex_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.POKEDEX, self.game.sound_effects.play_click_sound)),            
            inputs.Button(460, 350, *self.display.menu.combat_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.COMBAT, self.game.sound_effects.play_click_sound)) 
           ]
        self.pokedex_buttons = [
            inputs.Button(700,510,50,50, lambda: self.execute_multiple(self.game.change_current_state, self.game.MENU, self.game.sound_effects.play_click_sound))
        ]
        

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menu_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        button.click()
                        
    def handle_combat_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
    
    def handle_pokedex_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.pokedex_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        button.click()
        
                        
    def execute_multiple(self, func1, arg1, func2):
        func1(arg1)
        if func2 != None:
            func2()
            
    def load_pokedex_buttons(self):
        for i in range(len(self.display.pokedex.pokemon_list)):
            self.pokedex_buttons.append(inputs.Button(60, 100 + i * 40, *self.display.pokedex.rect_list[i].size, lambda i=i: self.execute_multiple(self.display.pokedex.show_pokemon_info, i, self.game.sound_effects.play_click_sound)))