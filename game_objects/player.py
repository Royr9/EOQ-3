class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        self.health = max(self.health, 0)

    def heal(self, amount):
        self.health += amount

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def __str__(self):
        return f"Player {self.name}: Health={self.health}"
