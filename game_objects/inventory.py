from game_objects.items import Spell, Armor, Key

class Inventory:
    def __init__(self):
        self.inventory = []
        self.armor = None

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def equip_armor(self, armor: Armor):
        self.armor = armor

    def unequip_armor(self):
        self.armor = None

    # Can be none
    def get_armor(self) -> Armor | None:
        return self.armor
