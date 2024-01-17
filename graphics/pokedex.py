import data
import pygame
import graphics

class Pokedex:
    def __init__(self, display) -> None:
        self.display = display
        self.text = graphics.Text(display)

        self.data_manager = data.Data_manager()
        self.data = self.data_manager.get_pokedex_data()

        self.pokemon_list = self.list_pokemon()
        self.pokemon_image = None
        
        self.background = pygame.image.load('assets/images/pokedex/pokedexbg.png')

        self.rect_list = self.load_rect_list()
        
    def draw(self):
        self.display.screen.fill('green')
        self.display.screen.blit(self.background, (0,0))

        self.draw_pokemon_list()
        if self.pokemon_image != None:
            self.display.screen.blit(self.pokemon_image, (540, 300 - (self.pokemon_image.get_height() / 2) - 10))
    
    def list_pokemon(self):
        list_pokemon = []
        for items in self.data:
            list_pokemon.append(items['name'])
        return list_pokemon
    
    def draw_pokemon_list(self):
        for i in range(len(self.pokemon_list)):
            self.text.draw_text(self.pokemon_list[i], 20, (60, 100 + i * 40))
    
    def load_rect_list(self):
        rect_list = []
        for i in range(len(self.pokemon_list)):
            rect_list.append(self.text.get_text_rect(self.pokemon_list[i], 20))
        return rect_list
    
    def show_pokemon_info(self, i):
        self.pokemon_image = pygame.image.load('assets/images/pokedex/' + self.pokemon_list[i] + '.png')
        self.pokemon_image = pygame.transform.scale2x(self.pokemon_image)
        print(self.pokemon_list[i])
        
    