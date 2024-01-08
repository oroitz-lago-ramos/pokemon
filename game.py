from display import *
import sys


class Game:
    MENU = 1
    def __init__(self) -> None:
        self.__display = Display()
        self.__is_running = True
        self.__current_state = Game.MENU
    
    def run(self):
        while self.__is_running:
            if self.__current_state == self.MENU:
                self.__display.draw_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__is_running = False
        self.stop()
            
    def stop(self):
        self.display.stop()
        sys.exit()
        