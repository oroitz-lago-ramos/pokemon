import data
import pygame

class Pokedex:
    def __init__(self, display) -> None:
        self.display = display
        self.data_manager = data.Data_manager()
        self.data = self.data_manager.pokemon_data
        
        self.background = pygame.image.load('assets/images/pokedex/pokedexbg.png')
        
    def draw(self):
        self.display.screen.fill('green')
        self.display.screen.blit(self.background, (0,0))
    
    def test(self):
        for items in self.data:
            print(items)
    
    