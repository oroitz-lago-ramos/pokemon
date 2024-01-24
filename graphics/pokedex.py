import data
import pygame
import graphics

class Pokedex:
    def __init__(self, display) -> None:
        self.display = display
        self.text = graphics.Text(display)

        self.data_manager = data.Data_manager()
        self.data = self.data_manager.get_pokedex_data()

        self.offset = 0
        self.pokemon_list = self.list_pokemon()
        self.pokemon_names_list = self.list_pokemon_names()
        self.pokemon_types_list = self.list_types()
        self.rect_list = self.load_rect_list()
        
        
        self.pokemon_image = None
        self.pokemon_type = None
        self.pokemon_name = None
        self.pokemon_max_hp = None
        self.pokemon_attack = None
        self.pokemon_defense = None
        self.pokemon_speed = None

        self.pokemon_selected_rect = self.text.get_text_rect("SELECTIONNER POKEMON", 15)
        
        self.background = pygame.image.load('assets/images/pokedex/pokedexbg.png')

        
    def draw(self):
        self.display.screen.fill('green')
        self.display.screen.blit(self.background, (0,0))
        
        self.draw_pokemon_list()
        if self.pokemon_image != None and self.pokemon_type != None and self.pokemon_name != None:
            self.display.screen.blit(self.pokemon_image, (540, 300 - (self.pokemon_image.get_height() / 2) - 10))
            self.display.screen.blit(self.pokemon_type, (530 + (self.pokemon_image.get_height() / 2), 300 + (self.pokemon_image.get_height() / 2) + 10))
            self.text.draw_text(self.pokemon_name, 20, (540, 300 - (self.pokemon_image.get_height() / 2) - 10 - 30),"black")
            self.text.draw_text(f"Vie : {self.pokemon_max_hp} ", 12, (450, 400),"Black")
            self.text.draw_text(f"Attaque : {self.pokemon_attack} ", 12, (620, 400),"Black")
            self.text.draw_text(f"Vitesse : {self.pokemon_speed} ", 12, (620, 430),"Black")
            self.text.draw_text(f"Defense : {self.pokemon_defense} ", 12, (450, 430),"Black")
            if self.pokemon_name == self.display.game.selected_pokemon:
                self.text.draw_text("SELECTIONNER POKEMON", 15, (450, 470),"Green")
            else:
                self.text.draw_text("SELECTIONNER POKEMON", 15, (450, 470),"Red") 
    

        elif self.pokemon_image != None:
            self.display.screen.blit(self.pokemon_image, (540, 300 - (self.pokemon_image.get_height() / 2) - 10))
            
    def list_pokemon(self):
        list_pokemon = []
        for items in self.data:
            list_pokemon.append(items)
        return list_pokemon
    
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
        for i in range(self.offset, min(self.offset + 12, len(self.pokemon_list))):
            if self.pokemon_list[i]["discovered"] == True:
                self.text.draw_text(self.pokemon_list[i]["name"], 20, (60, 95 + (i - self.offset) * 40), 'black')
            else:
                self.text.draw_text("?????", 20, (60, 95 + (i - self.offset) * 40), 'black')

    
    def show_pokemon_info(self, i):
        self.pokemon_image = None
        self.pokemon_name = None
        self.pokemon_type = None
        self.pokemon_max_hp = None
        self.pokemon_attack = None
        self.pokemon_defense = None
        self.pokemon_speed = None
        
        actual_index = i + self.offset  # Calculate the actual index in the full list
        
        if 0 <= actual_index < len(self.pokemon_list) and self.pokemon_list[actual_index]['discovered']:
            self.pokemon_image = pygame.image.load('assets/images/sprites/face/' + str(self.pokemon_list[actual_index]['id']) + '.png')
            self.pokemon_image = pygame.transform.scale2x(self.pokemon_image)
            
            self.pokemon_type = pygame.image.load('assets/images/types/' + self.pokemon_types_list[actual_index] + '.png')
            
            self.pokemon_name = self.pokemon_names_list[actual_index]
            self.pokemon_max_hp = self.pokemon_list[actual_index]['max_health']
            self.pokemon_attack = self.pokemon_list[actual_index]['attack']
            self.pokemon_defense = self.pokemon_list[actual_index]['defense']
            self.pokemon_speed = self.pokemon_list[actual_index]['speed']
        else:
            self.pokemon_image = pygame.image.load('assets/images/pokedex/0.png')
            self.pokemon_image = pygame.transform.scale2x(self.pokemon_image)

            
    def select_pokemon(self):
        self.display.game.selected_pokemon = self.pokemon_name
        self.data_manager.update_selected_pokemon(self.pokemon_name)
        # Data manager pour enregistrer le choix