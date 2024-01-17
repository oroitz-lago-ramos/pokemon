import pygame
import graphics

class Combat:
    def __init__(self, display, fight) -> None:
        self.display = display
        self.fight = fight
        
         # Combat assets
        self.combat_background_sheet = pygame.image.load('assets/images/combat/combat_sheet.png')
        self.combat_elements_sheet = pygame.image.load('assets/images/combat/combat_elements_sheet.png')
        self.battle_background = self.get_sprite(self.combat_background_sheet, 249, 6, 240, 112, (self.display.WIDTH, 3 * self.display.HEIGHT / 4))
        self.battle_bottom = self.get_sprite(self.combat_elements_sheet, 297, 56, 240, 48, (self.display.WIDTH, 1 * self.display.HEIGHT / 4))
        
        # self.player_life_bar = self.get_sprite(self.combat_elements_sheet, 2, 44, 104, 37, 2)
        # self.enemy_life_bar = self.get_sprite(self.combat_elements_sheet, 2, 2, 100, 29, 2)
        self.player_life_bar = pygame.image.load('assets/images/combat/player_life_bar.png')
        self.enemy_life_bar = pygame.image.load('assets/images/combat/enemy_life_bar.png')
        self.player_life_bar = pygame.transform.scale2x(self.player_life_bar)
        self.enemy_life_bar = pygame.transform.scale2x(self.enemy_life_bar)
        
        #Trouver les memes tailles de sprites afin de enlever le pygame transform et ces variables là
        
        self.pokemon_bounce = 0
        self.pokemon_bounce_direction = 1
        
    def draw(self):
        self.player_pokemon_sprite = self.fight.player_pokemon.get_pokemon_sprite()
        self.player_pokemon_sprite = pygame.transform.scale(self.player_pokemon_sprite, (self.player_pokemon_sprite.get_width() * 2, self.player_pokemon_sprite.get_height() *2))
        
        self.enemy_pokemon_sprite = self.fight.enemy_pokemon.get_pokemon_sprite()
        self.enemy_pokemon_sprite = pygame.transform.scale(self.enemy_pokemon_sprite, (self.enemy_pokemon_sprite.get_width() / 10, self.enemy_pokemon_sprite.get_height() / 10))
        
        
        if self.display.game.combat_started():
            self.start_time = pygame.time.get_ticks()
        self.display.game.set_combat_started(False)
                
        if pygame.time.get_ticks() - self.start_time < 3000:
            self.display.screen.fill("black")
            pygame.display.update()
            pygame.time.delay(120)
            self.display.screen.fill("gray")
            pygame.display.update()
            pygame.time.delay(120)
            self.display.screen.fill((2,2,2))
            pygame.display.update()
            pygame.time.delay(120)
        
        bounce_speed = 2
        max_bounce = 15
        if self.pokemon_bounce > max_bounce:
            self.pokemon_bounce_direction = -1
        elif self.pokemon_bounce < -max_bounce:
            self.pokemon_bounce_direction = 1

        self.pokemon_bounce += bounce_speed * self.pokemon_bounce_direction       

        self.display.screen.blit(self.battle_background, (0,0))
        self.display.screen.blit(self.player_pokemon_sprite, (-10, 160 + self.pokemon_bounce))
        self.display.screen.blit(self.enemy_pokemon_sprite, (510, 70 - self.pokemon_bounce))
        self.display.screen.blit(self.battle_bottom,(0, 3 * self.display.HEIGHT / 4))
        
        # print(f"{self.fight.player_pokemon.get_health()} / {self.fight.player_pokemon.get_max_health()} ")
    
    def update_combat(self):
        self.display.screen.fill("white")
        bounce_speed = 0.05
        max_bounce = 3
        if self.pokemon_bounce > max_bounce:
            self.pokemon_bounce_direction = -1
        elif self.pokemon_bounce < -max_bounce:
            self.pokemon_bounce_direction = 1

        self.pokemon_bounce += bounce_speed * self.pokemon_bounce_direction

        self.display.screen.blit(self.battle_background, (0,0))
        self.display.screen.blit(self.player_pokemon_sprite, (-10, 160 + self.pokemon_bounce))
        self.display.screen.blit(self.enemy_pokemon_sprite, (510, 70 - self.pokemon_bounce))
        
        
        
        self.display.screen.blit(self.battle_bottom,(0, 3 * self.display.HEIGHT / 4))
        self.display.screen.blit(self.player_life_bar, (510, 376))
        self.display.screen.blit(self.enemy_life_bar, (50, 50))
        
       # pygame.draw.rect(self.display.screen, "black", (20, 500, self.display.WIDTH - 20, self.display.HEIGHT - 20))
        pygame.draw.rect(self.display.screen, self.hp_bar_color(self.fight.enemy_pokemon), (126, 82, self.fight.enemy_pokemon.get_health() / self.fight.enemy_pokemon.get_max_health() * 100, 10))
        self.fight.enemy_pokemon.take_damage(0.1)
    
    def get_sprite(self, sheet, x, y, width, height, size):
        sprite = pygame.Surface((width, height))
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        if size != None and size != 2:
            sprite = pygame.transform.scale(sprite, size)
        elif size == 2:
            sprite = pygame.transform.scale2x(sprite)
        return sprite
    
    def hp_bar_color(self, pokemon):
        if pokemon.get_health() <= pokemon.get_max_health() * 0.25:
            return 'red'
        elif pokemon.get_health() <= pokemon.get_max_health() * 0.5:
            return 'yellow'
        else:
            return 'green'