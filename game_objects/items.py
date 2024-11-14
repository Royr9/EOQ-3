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
    def __init__(self, current_floor: int, name: str = ""):
        self.type = "weapons"
        
        if not name:
            self.name = game_items[self.type]
        else:
            self.name = name
            
        self.damage = random.randint(1, 5) * int(current_floor)
    

class Armor(Item):
    def __init__(self, current_floor: int, name: str = ""):
        self.type = "armors"
        
        if not name:
            self.name = game_items[self.type]
        else:
            self.name = name
            
        self.armor = random.randint(1, 5) * int(current_floor)
    
    
class Key(Item):
    def __init__(self, current_floor: int):
        self.name = f"key_floor_{current_floor}"
