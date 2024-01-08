import pygame

class Display:
    def __init__(self) -> None:
        self.__WIDTH = 800
        self.__HEIGHT = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption('Pokemon')
    
    def stop(self):
        pygame.quit()
        
    def draw_menu(self):
        self.screen.fill('purple')
        
        
        pygame.display.update()