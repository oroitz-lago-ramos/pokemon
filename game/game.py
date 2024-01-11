import sys
import game
import graphics
import inputs
import sounds
import data

import pygame #temporaire
class Game:
    MENU = 1
    COMBAT = 2
    POKEDEX = 3
    def __init__(self) -> None:
        # Ajouter attribut de type chargement de sauvegarde
        
        self.__combat_started = False
        self.combat_state = None 
        
        
       
         
        self.__is_running = True #cette variable gere l'etat de la boucle principale
        self.__current_state = Game.MENU

        self.data_manager = data.Data_manager()
        self.__previous_state = None
        self.sound = sounds.Sound(self)
        
        self.fight = game.Fight(self)
        self.display = graphics.display.Display(self)
        self.event_handler = inputs.Event_handler(self)
            
    def run(self):
        '''Starts the game and main_loop'''
        # Gestion des sauvegardes
        while self.__is_running:
            
            if self.__current_state != self.__previous_state:
                self.sound.choose_music()
            self.__previous_state = self.__current_state
            
            # Ce if servira a gerer les differents états : par exemple etat Menu alors afficher le menu
            if self.__current_state == self.MENU:
                self.display.draw_menu()
                self.event_handler.handle_menu_events()
                
            elif self.__current_state == self.COMBAT:
                self.fight.start_fight("Salameche", "Bulbizarre")
                self.display.draw_combat()
                               
                # Gestion des inputs à faire dans une autre page
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
            
                
            
            elif self.__current_state == self.POKEDEX:
                pass
                
        self.quit()
            
    def stop(self):
        '''Turns off the main loop of the game'''
        self.__is_running = False
        
    def quit(self):
        '''Quits the grahpics and the game'''
        # Ajouter la gestion de la sauvegarde à quit
        self.display.quit()
        sys.exit()
        
    
            
    def change_current_state(self,state):
        self.__current_state = state
        if state == self.COMBAT:
            self.__combat_started = True
    def current_state(self):
        return self.__current_state
    
    def combat_started(self):
        return self.__combat_started
    def set_combat_started(self, value):
        self.__combat_started = value
        
    
    