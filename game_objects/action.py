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

    def use(self, level, player) -> str:
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
            level.move(self.value)
            return f"You walked to the {self.value}"

    def __str__(self):
        """
        Return a string representation of the Action object.

        :return: A formatted string containing the action name, type, and value
        """
        return f"{self.name}: {self.type} - {self.value}"