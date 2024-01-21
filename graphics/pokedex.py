import data
import pygame
import graphics

class Pokedex:
    def __init__(self, display) -> None:
        self.display = display
        self.text = graphics.Text(display)

        self.data_manager = data.Data_manager()
        self.data = self.data_manager.get_pokedex_data()

        self.pokemon_names_list = self.list_pokemon_names()
        self.pokemon_types_list = self.list_types()
        self.rect_list = self.load_rect_list()
        
        
        self.pokemon_image = None
        self.pokemon_type = None
        self.pokemon_name = None
        
        self.background = pygame.image.load('assets/images/pokedex/pokedexbg.png')

        
    def draw(self):
        self.display.screen.fill('green')
        self.display.screen.blit(self.background, (0,0))

        self.draw_pokemon_list()
        if self.pokemon_image != None:
            self.display.screen.blit(self.pokemon_image, (540, 300 - (self.pokemon_image.get_height() / 2) - 10))
            self.display.screen.blit(self.pokemon_type, (530 + (self.pokemon_image.get_height() / 2), 300 + (self.pokemon_image.get_height() / 2) + 10))
            self.text.draw_text(self.pokemon_name, 20, (540, 300 - (self.pokemon_image.get_height() / 2) - 10 - 30),"black")
    
    def list_pokemon_names(self):
        list_pokemon = []
        for items in self.data:
            list_pokemon.append(items['name'])
        return list_pokemon
    def list_types(self):
        list_types = []
        for items in self.data:
            list_types.append(items['type'])
        return list_types
    def load_rect_list(self):
        rect_list = []
        for i in range(len(self.pokemon_names_list)):
            rect_list.append(self.text.get_text_rect(self.pokemon_names_list[i], 20))
        return rect_list
    
    
    def draw_pokemon_list(self):
        for i in range(len(self.pokemon_names_list)):
            self.text.draw_text(self.pokemon_names_list[i], 20, (60, 100 + i * 40),"black")
    
    def show_pokemon_info(self, i):
        self.pokemon_image = pygame.image.load('assets/images/pokedex/' + self.pokemon_names_list[i] + '.png')
        self.pokemon_image = pygame.transform.scale2x(self.pokemon_image)
        
        self.pokemon_type = pygame.image.load('assets/images/types/' + self.pokemon_types_list[i] + '.png')
        
        self.pokemon_name = self.pokemon_names_list[i]
    