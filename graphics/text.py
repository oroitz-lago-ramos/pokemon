
import pygame

class Text:
    def __init__(self, display) -> None:
        self.display = display
        self.font_path = 'assets/fonts/PokemonGb-RAeo.ttf'
    
    def create_text(self, item, font_size,color):
        self.font = pygame.font.Font(self.font_path, font_size)
        text = self.font.render(item, True, color)
        return text
    
    def get_text_rect(self, item, font_size):
        text = self.create_text(item, font_size,"black")
        rect = text.get_rect()
        return rect
    
    def draw_text(self, item, font_size, coords,color):
        text = self.create_text(item, font_size,color)
        self.display.screen.blit(text, coords)