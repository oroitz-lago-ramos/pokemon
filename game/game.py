import sys
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
    
    # def get_display(self):
    #     return self.__display   
            
    def run(self):
        '''Starts the game and main_loop'''
        # Gestion des sauvegardes
        while self.__is_running:
            
            # Ce if servira a gerer les differents états : par exemple etat Menu alors afficher le menu
            if self.__current_state == self.MENU:
                pass
                # Gestion des inputs à faire dans une autre page
                
            elif self.__current_state == self.COMBAT:
                pass
                               
                # Gestion des inputs à faire dans une autre page
                
            
            elif self.__current_state == self.POKEDEX:
                pass
                               
                # Gestion des inputs à faire dans une autre page
                
        self.quit()
            
    def stop(self):
        '''Turns off the main loop of the game'''
        self.__is_running = False
        
    def quit(self):
        '''Quits the grahpics and the game'''
        # Ajouter la gestion de la sauvegarde à quit
        # self.__display.stop()
        sys.exit()
        
    
            
    def change_current_state(self,state):
        self.__current_state = state
        if state == self.COMBAT:
            self.__combat_started = True
        
    
    