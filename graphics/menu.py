import pygame
import graphics
import data

class Menu:
    def __init__(self, display) -> None:
        self.display = display
        self.data_manager = data.Data_manager()
        self.text = graphics.Text(self.display)
        self.font_size = 17
        
        self.menu_background = pygame.image.load("assets/images/menu/background.png")
        self.menu_background = pygame.transform.scale(self.menu_background, (graphics.Display.WIDTH, graphics.Display.HEIGHT))
        self.menu_title = pygame.image.load("assets/images/menu/title.png")
        self.menu_title = pygame.transform.scale(self.menu_title,(self.menu_title.get_width() / 2, self.menu_title.get_height() / 2))
        
        self.logo_bounce = 0
        self.bounce_direction = 1
        
        #Ici on initialise les rectangles pour que eventhandler puisse les utiliser
        #Je souhaiterais trouver un meilleur moyen
        self.pokedex_rect = self.text.get_text_rect("POKEDEX",17)
        self.combat_rect = self.text.get_text_rect("COMBAT",17)
        self.unlock_all_rect = self.text.get_text_rect("TOUT DEBLOQUER",16)
        self.restart_rect = self.text.get_text_rect("RECOMMENCER PARTIE",16)
        
    def draw(self):
        '''Draws the menu elements'''
        
        # Animation of the logo
        self.data_manager = data.Data_manager()
        bounce_speed = 0.1
        max_bounce = 5
        if self.logo_bounce > max_bounce:
            self.bounce_direction = -1
        elif self.logo_bounce < -max_bounce:
            self.bounce_direction = 1

        self.logo_bounce += bounce_speed * self.bounce_direction
        
        
        
        self.display.screen.fill('purple')
        self.display.screen.blit(self.menu_background, (0, 0))
        self.display.screen.blit(self.menu_title, (graphics.Display.WIDTH / 2 - self.menu_title.get_width() / 2, 50 + self.logo_bounce))

        self.text.draw_text("POKEDEX", self.font_size, (290, 350),"black")
        self.text.draw_text("COMBAT", self.font_size, (460, 350),"black")
        self.text.draw_text("RECOMMENCER PARTIE", self.font_size, (280, 500),"white")
        if len(self.data_manager.get_pokedex_data()) == len(self.data_manager.get_pokemon_data()):
            self.text.draw_text("TOUT EST DEBLOQUER", self.font_size, (280, 430),"blue")
        else:
            self.text.draw_text("TOUT DEBLOQUER", self.font_size, (300, 430),"red")
    

   
        
