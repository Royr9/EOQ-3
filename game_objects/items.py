import random
import json
from string import printable

# Load the JSON file containing game item data
with open("game_objects/items_db.json") as file:
    game_items = json.load(file)

class Spell:
    def __init__(self, multiplier: int):
        """
        Initialize a Spell object.
        
        :param multiplier: A factor to multiply the spell's power by
        """
        # Randomly select a spell from the database
        name, rarity, damage = random.choice(list(game_items["spells"])).values()
        self.name = name
        self.rarity = rarity
        # Calculate damage based on multiplier and random factor
        self.damage = damage * (int(multiplier) + 1)

    def get_name(self):
        """
        Get the name of the spell.
        
        :return: The spell's name
        """
        return self.name

    def get_rarity(self):
        """
        Get the rarity of the spell.
        
        :return: The spell's rarity
        """
        return self.rarity

    def get_damage(self):
        """
        Get the damage dealt by the spell.
        
        :return: The spell's damage value
        """
        return self.damage

class Armor:
    def __init__(self, multiplier: int):
        """
        Initialize an Armor object.
        
        :param multiplier: A factor to multiply the armor's defense by
        """
        # Randomly select armor from the database
        name, rarity, defense = random.choice(list(game_items["armor"])).values()
        self.name = name
        self.rarity = rarity
        # Calculate defense based on multiplier and random factor
        self.defense = defense * (int(multiplier) + 1)

    def get_name(self):
        """
        Get the name of the armor.
        
        :return: The armor's name
        """
        return self.name

    def get_rarity(self):
        """
        Get the rarity of the armor.
        
        :return: The armor's rarity
        """
        return self.rarity

    def get_armor_defense(self):
        """
        Get the defense provided by the armor.
        
        :return: The armor's defense value
        """
        return self.defense

    # Note: The class definition for Key is incomplete and doesn't contain any methods

class Key:
    def __init__(self, current_floor: int):
        """
        Initialize a Key object.
        
        :param current_floor: The floor number associated with this key
        """
        self.name = f"key_floor_{current_floor}"

spell = Spell(1)
