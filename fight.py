class Fight:
    def __init__(self):
        self.attacker_attack = 0
        self.attacker_type = ""
        self.defender_type = ""


    def calculate_damage(self, attacker_type, attacker_attack, defender_type):
        type_chart = {
            'water': {'water': 1, 'fire': 2, 'grass': 0.5, 'neutral': 1},
            'fire': {'water': 0.5, 'fire': 1, 'grass': 2, 'neutral': 1},
            'grass': {'water': 2, 'fire': 0.5, 'grass': 1, 'neutral': 1},
            'neutral': {'water': 0.75, 'fire': 0.75, 'grass': 0.75, 'neutral': 1}
        }
    # voir comment mettre le lien avec les fichiers json pour le calcule
    def apply_defense(self):
        pass
    # voir comment la defense influ sur les degats subit
    def determine_winner(self, attacker_hp, defender_hp):
        if attacker_hp > defender_hp:
            return "Attacker"
        elif attacker_hp < defender_hp:
            return "Defender"
        else:
            return "Draw"
    def battle_result(self, attacker_name, defender_name, attacker_hp, defender_hp):
        winner = self.determine_winner(attacker_hp, defender_hp)
        if winner == "Attacker":
            return f"{attacker_name} wins! {defender_name} loses."
        elif winner == "Defender":
            return f"{defender_name} wins! {attacker_name} loses."
        else:
            return "It's a draw!"
    def save_to_pokedex(self, pokemon_name):
        print(f"{pokemon_name} added to the Pokedex!")