# items:
# keys to open door
# weapons
# armor
from abc import ABC, abstractmethod
import random
import json

# Load the JSON file
with open("game_items.json") as file:
    game_items = json.load(file)

# Access weapons and armors
WEAPONS = game_items["weapons"]
ARMORS = game_items["armors"]


class Item(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def generate_random(self) -> str:
        """Generate a random string based on the given class list"""
    

class Weapon(Item):
    """Generates a random weapon with random damage
    """
    def __init__(self, multiplier: int, name: str = ""):
        """
        Args:
            multiplier (int)
            name (str, optional): optional new name or leave empty to get random name
        """
        self.type = "weapons"
        super().__init__(name or random.choice(game_items[self.type]))
            
        self.damage = random.randint(1, 5) * int(multiplier)
    

class Armor(Item):
    def __init__(self, multiplier: int, name: str = ""):
        """_summary_

        Args:
            multiplier (int): _description_
            name (str, optional): _description_. Defaults to "".
        """
        self.type = "armors"
        super().__init__(name or random.choice(game_items[self.type]))
            
        self.armor = random.randint(1, 5) * int(multiplier)
    
    
class Key(Item):
    def __init__(self, current_floor: int):
        self.name = f"key_floor_{current_floor}"

