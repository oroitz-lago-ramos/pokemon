import pygame
import graphics

class Combat:
    def __init__(self, display, fight) -> None:
        self.display = display
        self.fight = fight
        self.text = graphics.text.Text(self.display)
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
        
        self.attack_rect = self.text.get_text_rect("Attaquer", 20)
        self.run_rect = self.text.get_text_rect("Fuir", 20)
        
    def draw(self):
        self.player_pokemon_sprite = self.fight.player_pokemon.get_pokemon_sprite()
        self.player_pokemon_sprite = pygame.transform.scale(self.player_pokemon_sprite, (self.player_pokemon_sprite.get_width() * 4, self.player_pokemon_sprite.get_height() * 4))
        
        self.enemy_pokemon_sprite = self.fight.enemy_pokemon.get_pokemon_sprite()
        self.enemy_pokemon_sprite = pygame.transform.scale(self.enemy_pokemon_sprite, (self.enemy_pokemon_sprite.get_width() * 4, self.enemy_pokemon_sprite.get_height() * 4))
        
        
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
        self.display.screen.blit(self.player_pokemon_sprite, (100, 260 + self.pokemon_bounce))
        self.display.screen.blit(self.enemy_pokemon_sprite, (450, 70 - self.pokemon_bounce))
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
        self.display.screen.blit(self.player_pokemon_sprite, (100, 260 + self.pokemon_bounce))
        self.display.screen.blit(self.enemy_pokemon_sprite, (450, 70 - self.pokemon_bounce))
        
        
        
        self.display.screen.blit(self.battle_bottom,(0, 3 * self.display.HEIGHT / 4))
        self.display.screen.blit(self.player_life_bar, (540, 376))
        self.display.screen.blit(self.enemy_life_bar, (60, 50))
        self.text.draw_text(self.fight.player_pokemon.get_name(), 12, (582, 389),"black")
        self.text.draw_text(self.fight.enemy_pokemon.get_name(), 12, (82, 63),"black")
        self.text.draw_text(str(self.fight.enemy_pokemon.get_level()), 12, (224, 64),"black")
        self.text.draw_text(str(self.fight.player_pokemon.get_level()), 12, (722, 390),"black")
        pygame.draw.rect(self.display.screen, self.hp_bar_color(self.fight.enemy_pokemon), (139, 84, self.fight.enemy_pokemon.get_health() / self.fight.enemy_pokemon.get_max_health() * (100 - 5), 6))
        pygame.draw.rect(self.display.screen, self.hp_bar_color(self.fight.player_pokemon), (636, 410, self.fight.player_pokemon.get_health() / self.fight.player_pokemon.get_max_health() * (100 - 4), 6))
        
        if self.fight.combat_state == 'select_attack':
            self.text.draw_text("Attaquer",20, (565, 488),"white")
            self.text.draw_text("Fuir",20, (593, 545),"white")
            pygame.draw.line(self.display.screen, pygame.Color("white"), (500, 578), (500, 472), 7)
            pygame.draw.line(self.display.screen, pygame.Color("white"), (500, 525), (775, 525), 7)
        else:
            if self.fight.turn == 'player':
                self.text.draw_text(f"{self.fight.player_pokemon.get_name()} va attaquer",16, (50, 500),"white")
            else:
                self.text.draw_text(f"{self.fight.enemy_pokemon.get_name()} va attaquer",16, (50, 500),"white")
            
        
        
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