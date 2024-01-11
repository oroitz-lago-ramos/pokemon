import pygame
from sound import *

class Display:
    def __init__(self,game) -> None:
        self.__WIDTH = 800
        self.__HEIGHT = 600
        self.game = game
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
        
        
        # Combat assets
        self.sprite_sheet = pygame.image.load('assets/images/combat/combat_sheet.png')
        self.battle_background = self.get_sprite(249, 6, 240, 112)
        self.battle_bottom = self.get_sprite(249, 6, 240, 112)# Replace with the actual position and size of the battle background sprite
    
    def draw_text(self,item,font_size):
        font = pygame.font.Font('assets/fonts/PokemonGb-RAeo.ttf', font_size)
        text = font.render(item, True, (0, 0, 0))
        return text, text.get_rect()
    
    def get_sprite(self, x, y, width, height):
        """Extracts a sprite from the sprite sheet at the given position and size."""
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (self.__WIDTH, 3 * self.__HEIGHT / 4))
        return sprite
        
    def draw_intro(self):
        pass
    
    
        
    def draw_menu(self):
        '''Draws the menu elements'''
        self.screen.fill('purple')
        self.screen.blit(self.menu_background,(0,0))
        self.screen.blit(self.menu_title, (self.__WIDTH / 2 - self.menu_title.get_width() / 2,50))
        
        self.screen.blit(self.pokedex,(290,350))
        self.screen.blit(self.combat,(460,350))
        self.screen.blit(self.ajouter_pokedex,(300,450))
        
        
        pygame.display.update()
        
    
    
    def draw_combat(self):
        if self.game.combat_started():
            self.start_time = pygame.time.get_ticks()  # Store the start time
        self.game.set_combat_started(False)
                
        if pygame.time.get_ticks() - self.start_time < 3100:
            self.screen.fill("black")
            pygame.display.update()
            pygame.time.delay(200)
            self.screen.fill("gray")
            pygame.display.update()
            pygame.time.delay(200)
            self.screen.fill((2,2,2))
            pygame.display.update()
            pygame.time.delay(200)

        self.screen.blit(self.battle_background, (0,0))
        pygame.display.update()
        
        
    def draw_pokedex(self):
        self.screen.fill('purple')
        
        pygame.display.update()
        
        
    def stop(self):
        '''quits pygame graphics'''
        pygame.quit()
        