import inputs
import pygame

class Event_handler:
    def __init__(self, game, display, fight) -> None:
        self.game = game
        self.display = display
        self.fight = fight
        
        self.menu_buttons = [
            inputs.Button(290, 350, *self.display.menu.pokedex_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.POKEDEX, self.game.sound_effects.play_click_sound)),            
            inputs.Button(460, 350, *self.display.menu.combat_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.COMBAT, self.game.sound_effects.play_click_sound)),
            inputs.Button(300, 430, *self.display.menu.unlock_all_rect.size, lambda: self.execute_multiple(self.display.pokedex.unlock_all_pokemon, None, self.game.sound_effects.play_click_sound)),
            inputs.Button(280, 500, *self.display.menu.restart_rect.size, lambda: self.execute_multiple(self.display.pokedex.restart_game, None, self.game.sound_effects.play_click_sound))
           ]
        self.pokedex_buttons = [
            inputs.Button(700,510,50,50, lambda: self.execute_multiple(self.game.change_current_state, self.game.MENU, self.game.sound_effects.play_click_sound)),
            inputs.Button(450, 470, *self.display.pokedex.pokemon_selected_rect.size, lambda: self.execute_multiple(self.display.pokedex.select_pokemon,None,self.game.sound_effects.play_click_sound))

        ]
        
        self.combat_buttons = [
            inputs.Button(565, 488, *self.display.combat.attack_rect.size, lambda: self.execute_multiple(self.fight.set_attack_selected, True, self.game.sound_effects.play_click_sound)),
            inputs.Button(593, 545, *self.display.combat.run_rect.size, lambda: self.execute_multiple(self.game.change_current_state, self.game.MENU, self.game.sound_effects.play_click_sound))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.fight.combat_state == 'select_attack':
                    for button in self.combat_buttons:
                        if button.is_clicked(pygame.mouse.get_pos()):
                            button.click()
                else:
                    self.game.sound_effects.play_click_sound()
                    self.fight.waiting_for_player = False
    
    def handle_pokedex_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
                
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    self.game.change_current_state(self.game.MENU)
                elif event.key == pygame.K_DOWN:
                    if self.display.pokedex.offset + 12 < len(self.display.pokedex.pokemon_list):
                        self.display.pokedex.offset += 1
                elif event.key == pygame.K_UP:
                    if self.display.pokedex.offset > 0:
                        self.display.pokedex.offset -= 1
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.pokedex_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        button.click()
        
                        
    def execute_multiple(self, func1, arg1, func2):
        if arg1 == None:
            func1()
        else:
            func1(arg1)
        if func2 != None:
            func2()
        
            
    def load_pokedex_buttons(self):
        for i in range(len(self.display.pokedex.pokemon_names_list)):
            self.pokedex_buttons.append(inputs.Button(60, 100 + i * 40, *self.display.pokedex.rect_list[i].size, lambda i=i: self.execute_multiple(self.display.pokedex.show_pokemon_info, i, self.game.sound_effects.play_click_sound)))