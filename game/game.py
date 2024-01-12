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

        self.__previous_state = None
        
        self.sound_effects = sounds.Sound_effect(self)
        self.music = sounds.Music(self)
        
        self.fight = game.Fight(self)
        self.display = graphics.display.Display(self)
        self.event_handler = inputs.Event_handler(self)
            
    def run(self):
        '''Starts the game and main_loop'''
        # Gestion des sauvegardes
        while self.__is_running:
            
            
            
            # Ce if servira a gerer les differents états : par exemple etat Menu alors afficher le menu
            if self.__current_state == self.MENU:
                self.display.draw_menu()
                self.event_handler.handle_menu_events()
                
            elif self.__current_state == self.COMBAT:
                self.display.draw_combat()
                self.event_handler.handle_combat_events()
                           
            elif self.__current_state == self.POKEDEX:
                self.display.draw_pokedex()
                self.event_handler.handle_pokedex_events()
                
            if self.__current_state != self.__previous_state:
                self.music.choose_music()
                if self.__current_state == self.MENU:
                    self.display.change_scene(self.display.menu)
                elif self.__current_state == self.COMBAT:
                    self.fight.start_fight("Salameche", "Bulbizarre")
                    self.display.change_scene(self.display.combat)
                elif self.__current_state == self.POKEDEX:
                    self.display.change_scene(self.display.pokedex)
            self.__previous_state = self.__current_state
                
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
        
    
    