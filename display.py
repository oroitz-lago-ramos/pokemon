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
        
        #Ici on initialise les rectangles pour que eventhandler puisse les utiliser
        #Je souhaiterais trouver un meilleur moyen
        self.pokedex, self.pokedex_rect = self.draw_text("POKEDEX",17)
        self.combat,self.combat_rect = self.draw_text("COMBAT",17)
        self.ajouter_pokedex, self.ajouter_pokedex_rect = self.draw_text("AJOUTER POKEMON",16)
    
    
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
        
        self.screen.blit(self.pokedex,(290,350))
        self.screen.blit(self.combat,(460,350))
        self.screen.blit(self.ajouter_pokedex,(300,450))
        
        
        pygame.display.update()
        
    def draw_text(self,item,font_size):
        font = pygame.font.Font('assets/fonts/PokemonGb-RAeo.ttf', font_size)
        text = font.render(item, True, (0, 0, 0))
        return text, text.get_rect()
    
    def draw_combat(self):
        self.screen.fill('black')
        
        pygame.display.update()
        
    def draw_pokedex(self):
        self.screen.fill('purple')
        
        pygame.display.update()
        