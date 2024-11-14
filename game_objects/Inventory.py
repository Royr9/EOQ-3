from game_objects.items import Item, Weapon, Armor

class Inventory:
    def __init__(self):
        self.inventory = []
        self.armor = None

    def add_item(self, item: Item):
        if isinstance(item, Item):
            self.inventory.append(item)

    def remove_item(self, item: Item):
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_armor(self, armor: Armor):
        if isinstance(armor, Armor):
            self.armor = armor

    def unequip_armor(self):
        self.armor = None

    # Can be none
    def get_armor(self) -> Armor:
        return self.armor