import pygame
import graphics

class Display:
    WIDTH = 800
    HEIGHT = 600
        
    def __init__(self,game,fight) -> None:
        self.game = game
        self.fight = fight
        
        
        
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((Display.WIDTH, Display.HEIGHT))
        pygame.display.set_caption('Pokemon')
        
        self.menu = graphics.Menu(self)
        self.combat = graphics.Combat(self, fight)
        self.pokedex = graphics.Pokedex(self)
    
    def screen(self):
        return self.screen
    def display(self):
        return self.display
    
    def change_scene(self, next_scene):
        self.transition(next_scene)  # Call the transition function
        self.current_scene = next_scene
    def draw_menu(self):
        self.menu.draw()
        self.update()
        
    def draw_combat(self):
        self.combat.update_combat()
        self.update()
        
    def draw_pokedex(self):
        self.pokedex.draw()
        self.update()
    
    def update(self):
        pygame.display.update()
    def quit(self):
        """
 	    Shuts down pygame.
 	    """
        pygame.quit()

    def transition(self, next_screen):
        transition_surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        transition_surface.fill((0, 0, 0))

        for alpha in range(0, 300, 5): 
            transition_surface.set_alpha(alpha)
            self.screen.blit(transition_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(1)

        next_screen.draw()  

        for alpha in range(300, 0, -5):  
            transition_surface.set_alpha(alpha)
            next_screen.draw()  
            self.screen.blit(transition_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(1)