import pygame

class Event_handler:
    def __init__(self, game):
        self.game = game

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(pygame.mouse.get_pos()):
                    button.click()