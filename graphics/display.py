import pygame
import graphics

class Display:
    WIDTH = 800
    HEIGHT = 600
        
    def __init__(self,game) -> None:
        self.game = game
        
        
        
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((Display.WIDTH, Display.HEIGHT))
        pygame.display.set_caption('Pokemon')
        
        self.menu = graphics.Menu(self)
        self.combat = graphics.Combat(self)
    
    def screen(self):
        return self.screen
    def display(self):
        return self.display
    
    def draw_menu(self):
        self.menu.draw()
        self.update()
        
    def draw_combat(self):
        self.combat.draw()
        self.update()
    
    def update(self):
        pygame.display.update()
    def quit(self):
        """
 	    Shuts down pygame.
 	    """
        pygame.quit()
