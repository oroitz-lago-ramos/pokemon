def calculate_damage(self, attacker_type, attacker_attack, defender_type):
        type_chart = {
            'water': {'water': 1, 'fire': 2, 'grass': 0.5, 'neutral': 1},
            'fire': {'water': 0.5, 'fire': 1, 'grass': 2, 'neutral': 1},
            'grass': {'water': 2, 'fire': 0.5, 'grass': 1, 'neutral': 1},
            'neutral': {'water': 0.75, 'fire': 0.75, 'grass': 0.75, 'neutral': 1}
        }
        
       
       
       
       
        # damage_multiplier = type_chart.get(attacker_type, {}).get(defender_type, 1)
        # damage = attacker_attack * damage_multiplier
        # return damage

    # def apply_defense(self, current_hp, defense_points, attacker_attack):
    #     adjusted_damage = attacker_attack / max(1, defense_points)
    #     return adjusted_damage

    # def determine_winner(self, attacker_hp, defender_hp):
    #     if attacker_hp > defender_hp:
    #         return "Attacker"
    #     elif attacker_hp < defender_hp:
    #         return "Defender"
    #     else:
    #         return "Draw"

    # def battle_result(self, attacker_name, defender_name, attacker_hp, defender_hp):
    #     winner = self.determine_winner(attacker_hp, defender_hp)
    #     if winner == "Attacker":
    #         return f"{attacker_name} wins! {defender_name} loses."
    #     elif winner == "Defender":
    #         return f"{defender_name} wins! {attacker_name} loses."
    #     else:
    #         return "It's a draw!"