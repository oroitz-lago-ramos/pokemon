from display import *
import sys


class Game:
    MENU = 1
    def __init__(self) -> None:
        # Ajouter attribut de type chargement de sauvegarde
        self.__display = Display() # Ceci instancie la classe display qui permettera de gerer l'affichage
        self.__is_running = True #cette variable gere l'etat de la boucle principale
        self.__current_state = Game.MENU
        self.sound = Sound()
        self.choose_music()
            
    def run(self):
        '''Starts the game and main_loop'''
        # Gestion des sauvegardes
        while self.__is_running:
            
            # Ce if servira a gerer les differents états : par exemple etat Menu alors afficher le menu
            if self.__current_state == self.MENU:
                self.__display.draw_menu()
                
                
                
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