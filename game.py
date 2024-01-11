from display import *
from fight import *
from event_handler import Event_handler
import sys


class Game:
    MENU = 1
    COMBAT = 2
    POKEDEX = 3
    def __init__(self) -> None:
        # Ajouter attribut de type chargement de sauvegarde
        self.data_manager = Data_manager()
        
        self.__combat_started = False
        self.combat_state = None  
        self.__is_running = True #cette variable gere l'etat de la boucle principale
        self.__current_state = Game.MENU
        
        self.sound = Sound()
        self.__previous_state = None
        self.fight = Fight(self)
        self.__display = Display(self) # Ceci instancie la classe display qui permettera de gerer l'affichage
        self.event_handler = Event_handler(self)
            
    def run(self):
        '''Starts the game and main_loop'''
        # Gestion des sauvegardes
        while self.__is_running:
            
            if self.__current_state != self.__previous_state:
                self.choose_music()
            self.__previous_state = self.__current_state
            # Ce if servira a gerer les differents états : par exemple etat Menu alors afficher le menu
            if self.__current_state == self.MENU:
                self.__display.draw_menu()
                self.event_handler.handle_menu_events()
                # Gestion des inputs à faire dans une autre page
                
            elif self.__current_state == self.COMBAT:
                self.fight.start_fight("Salameche", "Bulbizarre")
                self.__display.draw_combat()
                               
                # Gestion des inputs à faire dans une autre page
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
            
            elif self.__current_state == self.POKEDEX:
                self.__display.draw_pokedex()
                               
                # Gestion des inputs à faire dans une autre page
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
        self.quit()
            
    def stop(self):
        '''Turns off the main loop of the game'''
        self.__is_running = False
        
    def quit(self):
        '''Quits the grahpics and the game'''
        # Ajouter la gestion de la sauvegarde à quit
        self.__display.stop()
        sys.exit()
        
    def choose_music(self):
        if self.__current_state == self.MENU:
            self.sound.start_menu_music()
        elif self.__current_state == self.COMBAT:
            self.sound.start_combat_music()
            
    def change_current_state(self,state):
        self.__current_state = state
        if state == self.COMBAT:
            self.__combat_started = True
        
    def get_display(self):
        return self.__display
    
    def combat_started(self):
        return self.__combat_started

    def set_combat_started(self, value):
        self.__combat_started = value