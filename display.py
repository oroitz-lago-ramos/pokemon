import pygame
from sound import *

class Display:
    def __init__(self) -> None:
        self.__WIDTH = 800
        self.__HEIGHT = 600
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption('Pokemon')
        
        # Menu assets (passer par une fonction ou une autre classe qui herite de display?)
        self.menu_background = pygame.image.load("assets/images/menu/background.png")
        self.menu_background = pygame.transform.scale(self.menu_background, (self.__WIDTH, self.__HEIGHT))
        self.menu_title = pygame.image.load("assets/images/menu/title.png")
        self.menu_title = pygame.transform.scale(self.menu_title,(self.menu_title.get_width() / 2, self.menu_title.get_height() / 2))
    
    
    def draw_intro(self):
        pass
    
    def stop(self):
        '''quits pygame graphics'''
        pygame.quit()
        
    def draw_menu(self):
        '''Draws the menu elements'''
        self.screen.fill('purple')
        self.screen.blit(self.menu_background,(0,0))
        self.screen.blit(self.menu_title, (self.__WIDTH / 2 - self.menu_title.get_width() / 2,50))
        pokedex = self.draw_text("POKEDEX",17)
        combat = self.draw_text("COMBAT",17)
        ajouter_pokedex = self.draw_text("AJOUTER POKEMON",16)
        self.screen.blit(pokedex,(290,350))
        self.screen.blit(combat,(460,350))
        self.screen.blit(ajouter_pokedex,(300,450))
        
        
        pygame.display.update()
        
    def draw_text(self,item,font_size):
        font = pygame.font.Font('assets/fonts/PokemonGb-RAeo.ttf', font_size)
        text = font.render(item, True, (0, 0, 0))
        return text
    
    def draw_combat(self):
        self.screen.fill('black')
        
        pygame.display.update()
        