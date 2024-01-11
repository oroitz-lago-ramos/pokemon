import pygame

class Pokedex:
    def __init__(self, screen, data_manager):
        self.screen = screen
        self.data_manager = data_manager
        self.data = data_manager.load_data("pokemon.json")



    def draw(self):
        self.screen.fill('purple')
        # Draw each Pokemon in the Pokedex
        for i, pokemon in enumerate(self.data):
            print(i, pokemon)

    def update(self):
        pygame.display.update()