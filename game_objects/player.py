from game_objects.inventory import Inventory

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = Inventory()

    def take_damage(self, amount):
        if self.inventory.get_armor() != None:
            amount = amount/100*self.inventory.get_armor().get_armor_defense()

        self.health -= amount
        self.health = max(self.health, 0)
        return self.health

    def heal(self, amount):
        self.health += amount

    def get_inventory(self):
        return self.inventory

    def __str__(self):
        return f"Player {self.name}: Health={self.health}"
