class Location:
    def __init__(self, name, description, actions):
        """
        Initialize a Location object.

        :param name: The name of the location
        :param description: A brief description of the location
        :param actions: A dictionary of action objects available in this location
        """
        self.name = name
        self.description = description
        self.actions = actions

    def get_action_names(self):
        """
        Get a list of action names available in this location.

        :return: List of action names
        """
        return list(self.actions.keys())

    def get_action(self, name):
        """
        Get an action object by its name.

        :param name: The name of the action
        :return: The Action object corresponding to the given name
        """
        return self.actions[name]

    def use_action(self, name):
        """
        Execute an action in this location.

        :param name: The name of the action to execute
        """
        self.get_action(name).use()

    def add_action(self, action_name, action):
        """
        Add a new action to the available actions in this location.

        :param action_name: The name to give the new action
        :param action: The Action object to add
        """
        self.actions[action_name] = action

    def remove_action(self, action_name):
        """
        Remove an action from the available actions in this location.

        :param action_name: The name of the action to remove
        """
        del self.actions[action_name]

    def __str__(self):
        """
        Return a string representation of the Location object.

        :return: A formatted string containing the location name and description
        """
        return self.name + ": " + self.description