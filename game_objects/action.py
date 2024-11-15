class Action:
    def __init__(self, name, type, value):
        """
        Initialize an Action object.

        :param name: The name of the action
        :param type: The type of action
        :param value: The value associated with the action
        """
        self.name = name
        self.type = type
        self.value = value

    def use(self, game, player) -> str:
        """
        Execute the action.

        :param level: The current game level
        :param player: The player object
        :return: A string describing the result of the action
        """
        if self.type == 'print':
            # Print the value directly
            return self.value
        elif self.type == 'move':
            # Move the player to a new location
            game.get_current_level().move(self.value)
            return f"You walked to the {self.value}"
        elif self.type == "next_level":
            game.next_level()
            return "You went to the next floor."
        elif self.type == 'give':
            #player.get_inventory().add_item()
            return f"You received the {self.value}"

    def __str__(self):
        """
        Return a string representation of the Action object.

        :return: A formatted string containing the action name, type, and value
        """
        return f"{self.name}: {self.type} - {self.value}"