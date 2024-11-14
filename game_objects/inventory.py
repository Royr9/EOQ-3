from game_objects.items import Spell, Armor, Key

class Inventory:
    def __init__(self):
        """
        Initialize the Inventory object.

        Creates an empty inventory list and sets armor to None.
        """
        self.items = []
        self.armor = None

    def add_item(self, item):
        """
        Add an item to the inventory.

        :param item: The item to be added (e.g., Spell, Armor, Key)
        """
        self.inventory.append(item)

    def remove_item(self, item):
        """
        Remove an item from the inventory.

        :param item: The item to be removed
        """
        self.inventory.remove(item)

    def equip_armor(self, armor: Armor):
        """
        Equip armor in the inventory.

        :param armor: The Armor object to be equipped
        """
        self.armor = armor

    def unequip_armor(self):
        """
        Unequip the current armor.
        """
        self.armor = None

    def get_armor(self) -> Armor | None:
        """
        Get the currently equipped armor or None if none is equipped.

        :return: The equipped Armor object or None
        """
        return self.armor
