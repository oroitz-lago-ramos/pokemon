import pygame
import graphics

class Combat:
    def __init__(self, display) -> None:
        self.display = display
        
         # Combat assets
        self.combat_background_sheet = pygame.image.load('assets/images/combat/combat_sheet.png')
        self.combat_elements_sheet = pygame.image.load('assets/images/combat/combat_elements_sheet.png')
        self.battle_background = self.get_sprite(self.combat_background_sheet, 249, 6, 240, 112, (self.display.WIDTH, 3 * self.display.HEIGHT / 4))
        self.battle_bottom = self.get_sprite(self.combat_elements_sheet, 297, 56, 240, 48, (self.display.WIDTH, 1 * self.display.HEIGHT / 4))

        #Trouver les memes tailles de sprites afin de enlever le pygame transform et ces variables là
        
    def draw(self):
        self.player_pokemon_sprite = self.display.game.fight.player_pokemon.get_pokemon_sprite()
        self.player_pokemon_sprite = pygame.transform.scale(self.player_pokemon_sprite, (self.player_pokemon_sprite.get_width() * 2, self.player_pokemon_sprite.get_height() *2))
        
        self.enemy_pokemon_sprite = self.display.game.fight.enemy_pokemon.get_pokemon_sprite()
        self.enemy_pokemon_sprite = pygame.transform.scale(self.enemy_pokemon_sprite, (self.enemy_pokemon_sprite.get_width() / 10, self.enemy_pokemon_sprite.get_height() / 10))
        
        
        if self.display.game.combat_started():
            self.start_time = pygame.time.get_ticks()
        self.display.game.set_combat_started(False)
                
        if pygame.time.get_ticks() - self.start_time < 3100:
            self.display.screen.fill("black")
            pygame.display.update()
            pygame.time.delay(200)
            self.display.screen.fill("gray")
            pygame.display.update()
            pygame.time.delay(200)
            self.display.screen.fill((2,2,2))
            pygame.display.update()
            pygame.time.delay(200)

        self.display.screen.blit(self.battle_background, (0,0))
        self.display.screen.blit(self.player_pokemon_sprite, (-10,160))
        
        
        self.display.screen.blit(self.enemy_pokemon_sprite, (510, 70))
        
        
        
        self.display.screen.blit(self.battle_bottom,(0, 3 * self.display.HEIGHT / 4))
    
    def get_sprite(self, sheet, x, y, width, height, size):
        sprite = pygame.Surface((width, height))
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, size)
        return sprite