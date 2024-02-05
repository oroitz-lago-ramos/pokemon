import game
import time
import data
import random

class Fight:
    def __init__(self, game, sound_effects) -> None:
        self.game = game
        self.sound_effects = sound_effects
        
        self.data_manager = data.Data_manager()
        self.type_chart = self.data_manager.get_type_chart_data()
        
        self.enemy_pokemon = None
        self.player_pokemon = None
        self.turn = None
        self.first_turn = None
        
        self.waiting_for_player = True
        self.attack_selected = False
        self.combat_state = None


    def start_fight(self, player_pokemon_name):
        enemy_id = self.determine_enemy()
        print("Fight started")
        self.player_pokemon = game.Player_pokemon(player_pokemon_name)
        self.enemy_pokemon = game.Enemy_pokemon(enemy_id)
        self.first_turn = self.determine_turn_order()
        self.turn = self.first_turn
        self.combat_state = 'select_attack'
        
        
    def update(self):
        if self.verify_if_fight_is_over():
            self.game.change_current_state(self.game.MENU)
            print("Fight is over")
        
        if self.combat_state == 'select_attack' and not self.attack_selected:
            return
        elif self.combat_state == 'select_attack' and self.attack_selected:
            self.combat_state = 'attack'
            
        if self.combat_state == 'attack':
            if self.waiting_for_player:
                return 
            if self.turn == 'player':
                print("Player's turn")
                self.sound_effects.play_attack_effective_sound()
                self.player_attack()
                print(self.player_pokemon.get_name() + " attacks")
                self.turn = 'enemy'
                self.waiting_for_player = True
                if self.first_turn == 'enemy':
                    time.sleep(0.2)
                    self.combat_state = 'select_attack'
                    self.attack_selected = False
                    
            elif self.turn == 'enemy':
                print("Enemy's turn")
                
                self.sound_effects.play_attack_sound()
                self.enemy_attack()
                print(self.enemy_pokemon.get_name() + " attacks")
                self.turn = 'player'
                self.waiting_for_player = True
                self.attack_selected = False
                if self.first_turn == 'player':
                    time.sleep(0.2)
                    self.combat_state = 'select_attack'
                    self.attack_selected = False
                    
        if self.verify_if_fight_is_over():
            print("Fight is over")
            if self.determine_winner() == self.player_pokemon:
                self.data_manager.from_pokedex_to_pokemon(self.enemy_pokemon.get_name())
                print("Pokemon ajouté dans la liste des pokemons disponibles")
            else:
                print("Pokemon non ajouté dans la liste des pokemons disponibles, vous avez été vaincu")
            self.game.change_current_state(self.game.MENU)
            
    
        
        

    def player_attack(self):
        damage = self.calculate_damage(self.player_pokemon, self.enemy_pokemon)
        self.enemy_pokemon.take_damage(damage)
        
    def enemy_attack(self):
        damage = self.calculate_damage(self.enemy_pokemon, self.player_pokemon)
        self.player_pokemon.take_damage(damage)
    
    def check_damage_type(self,attacker, defender):
        attacker_type = attacker.get_type()
        defender_type = defender.get_type()
        return attacker_type, defender_type
        
        
    def calculate_damage(self, attacker, defender):
        attacker_type, defender_type = self.check_damage_type(attacker, defender)
        damage_multiplicator = self.type_chart[attacker_type][defender_type]
        damage = (attacker.get_attack() * damage_multiplicator) / (defender.get_defense() / 5)
        return damage
        
        
        
        
    def determine_enemy(self):
        #Utiliser fonction random pour
        return random.randint(1,26)
        
    def determine_turn_order(self):
        if self.player_pokemon.get_speed() > self.enemy_pokemon.get_speed():
            return 'player'
        else:
            return 'enemy'
    
    def verify_if_fight_is_over(self):
        if not self.player_pokemon.get_is_alive() or not self.enemy_pokemon.get_is_alive():
            return True
        else:
            return False
        
    def determine_winner(self):
        if self.player_pokemon.get_is_alive():
            return self.player_pokemon
        else:
            return self.enemy_pokemon
        
    def set_attack_selected(self, boolean):
        self.attack_selected = boolean