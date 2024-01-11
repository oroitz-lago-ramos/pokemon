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
        self.combat_background_sheet = pygame.image.load('assets/images/combat/combat_sheet.png')
        self.combat_elements_sheet = pygame.image.load('assets/images/combat/combat_elements_sheet.png')
        self.battle_background = self.get_sprite(self.combat_background_sheet, 249, 6, 240, 112, (self.__WIDTH, 3 * self.__HEIGHT / 4))
        self.battle_bottom = self.get_sprite(self.combat_elements_sheet, 297, 56, 240, 48, (self.__WIDTH, 1 * self.__HEIGHT / 4))

        #Trouver les memes tailles de sprites afin de enlever le pygame transform et ces variables là
        
    
    def draw_text(self,item,font_size):
        font = pygame.font.Font('assets/fonts/PokemonGb-RAeo.ttf', font_size)
        text = font.render(item, True, (0, 0, 0))
        return text, text.get_rect()
    
    def get_sprite(self, sheet, x, y, width, height, transform_scale):
        """Extracts a sprite from the sprite sheet at the given position and size."""
        sprite = pygame.Surface((width, height))
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, transform_scale)
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
        self.player_pokemon_sprite = self.game.fight.player_pokemon.get_pokemon_sprite()
        self.player_pokemon_sprite = pygame.transform.scale(self.player_pokemon_sprite, (self.player_pokemon_sprite.get_width() * 2, self.player_pokemon_sprite.get_height() *2))
        
        self.enemy_pokemon_sprite = self.game.fight.enemy_pokemon.get_pokemon_sprite()
        self.enemy_pokemon_sprite = pygame.transform.scale(self.enemy_pokemon_sprite, (self.enemy_pokemon_sprite.get_width() / 10, self.enemy_pokemon_sprite.get_height() / 10))
        
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
        self.screen.blit(self.player_pokemon_sprite, (-10,160))
        
        
        self.screen.blit(self.enemy_pokemon_sprite, (510, 70))
        
        
        
        self.screen.blit(self.battle_bottom,(0, 3 * self.__HEIGHT / 4))
        
        pygame.display.update()
        
        
    def draw_pokedex(self):
        self.screen.fill('purple')
        
        pygame.display.update()
        
        
    def stop(self):
        '''quits pygame graphics'''
        pygame.quit()
        