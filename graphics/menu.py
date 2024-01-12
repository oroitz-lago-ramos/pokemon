import pygame
import graphics

class Menu:
    def __init__(self, display) -> None:
        self.display = display
        
        self.menu_background = pygame.image.load("assets/images/menu/background.png")
        self.menu_background = pygame.transform.scale(self.menu_background, (graphics.Display.WIDTH, graphics.Display.HEIGHT))
        self.menu_title = pygame.image.load("assets/images/menu/title.png")
        self.menu_title = pygame.transform.scale(self.menu_title,(self.menu_title.get_width() / 2, self.menu_title.get_height() / 2))
        
        self.logo_bounce = 0
        self.bounce_direction = 1
        
        #Ici on initialise les rectangles pour que eventhandler puisse les utiliser
        #Je souhaiterais trouver un meilleur moyen
        self.pokedex_text, self.pokedex_rect = self.draw_text("POKEDEX",17)
        self.combat_text,self.combat_rect = self.draw_text("COMBAT",17)
        self.ajouter_pokedex_text, self.ajouter_pokedex_rect = self.draw_text("AJOUTER POKEMON",16)
        
    def draw(self):
        '''Draws the menu elements'''
        
        # Animation of the logo
        bounce_speed = 0.05
        max_bounce = 5
        if self.logo_bounce > max_bounce:
            self.bounce_direction = -1
        elif self.logo_bounce < -max_bounce:
            self.bounce_direction = 1

        self.logo_bounce += bounce_speed * self.bounce_direction
        
        
        
        self.display.screen.fill('purple')
        self.display.screen.blit(self.menu_background, (0, 0))
        self.display.screen.blit(self.menu_title, (graphics.Display.WIDTH / 2 - self.menu_title.get_width() / 2, 50 + self.logo_bounce))

        self.display.screen.blit(self.pokedex_text, (290, 350))
        self.display.screen.blit(self.combat_text, (460, 350))
        self.display.screen.blit(self.ajouter_pokedex_text, (300, 450))
        
    def draw_text(self,item,font_size):
        font = pygame.font.Font('assets/fonts/PokemonGb-RAeo.ttf', font_size)
        text = font.render(item, True, (0, 0, 0))
        return text, text.get_rect()
        
