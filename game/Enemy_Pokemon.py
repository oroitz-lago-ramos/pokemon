import game
import data
import pygame

class Enemy_pokemon(game.Pokemon):
    def __init__(self, id):
        self.data_manager = data.Data_manager()
        self.pokemon_name = self.data_manager.get_pokemon_name_by_id(id)
        self.pokedex_data = self.data_manager.get_pokemon_by_name_in_pokedex(self.pokemon_name)
        super().__init__(self.pokemon_name, self.pokedex_data)
        self.pokemon_sprite = pygame.image.load(f'assets/images/sprites/face/{self.id}.png')