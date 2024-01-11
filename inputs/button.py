import pygame

class Button:
    def __init__(self, x, y, width, height, action) -> None:
       self.rect = pygame.Rect(x,y,width,height)
       self.action = action 
        
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def click(self):
        if self.action is not None:
            self.action()