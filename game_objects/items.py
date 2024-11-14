
import random
import json

# Load the JSON file
with open("game_objects/items_db.json") as file:
    game_items = json.load(file)


class Spell:
    def __init__(self, multiplier: int):

        
        name, rarity, damage = random.choice(game_items["spells"]).values()
        self.name = name
        self.rarity = rarity
        self.damage = damage * random.choice((0.5, 1)) * int(multiplier)
    
    def get_name(self):
        return self.name
    
    def get_rarity(self):
        return self.rarity
    
    def get_damage(self):
        return self.damage

class Armor:
    """Generates a random weapon with random damage
    """
    def __init__(self, multiplier: int):
        """
        Args:
            multiplier (int)
            name (str, optional): optional new name or leave empty to get random name
        """
        
        name, rarity, defense = random.choice(game_items["spells"]).values()
        self.name = name
        self.rarity = rarity
        self.defense = defense * random.choice((0, 0.2, 0.4, 0.6, 0.8, 1)) * int(multiplier)
    
    
    def get_name(self):
        return self.name
    
    def get_rarity(self):
        return self.rarity
    
    def get_armor_defense(self):
        return self.defense
    
        
class Key:
    def __init__(self, current_floor: int):
        self.name = f"key_floor_{current_floor}"



spell = Spell(1)