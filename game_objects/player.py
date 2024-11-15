from game_objects.inventory import Inventory

class Player:
    def __init__(self, name, health):
        """
        Initialize a Player object.

        :param name: The player's name
        :param health: The player's initial health
        """
        self.name = name
        self.health = health
        self.inventory = Inventory()
        self.image = f"/player/player.png"

    def take_damage(self, amount):
        """
        Reduce the player's health by a specified amount.

        :param amount: The damage to apply
        :return: The final health value after applying damage
        """
        if self.inventory.get_armor() != None:
            # Apply armor reduction if equipped
            amount = amount / 100 * self.inventory.get_armor().get_armor_defense()

        self.health -= amount
        # Ensure health doesn't go below zero
        self.health = max(self.health, 0)
        return self.health

    def heal(self, amount):
        """
        Increase the player's health by a specified amount.

        :param amount: The healing amount
        """
        self.health += amount

    def get_inventory(self):
        """
        Get the player's inventory.

        :return: The player's Inventory object
        """
        return self.inventory

    def get_armor(self):
        """
        Get the currently equipped armor.

        :return: The Armor object if equipped, otherwise None
        """
        return self.inventory.get_armor()
    

    def __str__(self):
        """
        Return a string representation of the Player object.

        :return: A formatted string containing player name and health
        """
        return f"Player {self.name}: Health={self.health}"
