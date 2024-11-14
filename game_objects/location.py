class Location:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions

    def get_action_names(self):
        return list(self.actions.keys())

    def get_action(self, name):
        return self.actions[name]

    def use_action(self, name):
        self.get_action(name).use()

    def add_action(self, action_name, action):
        self.actions[action_name] = action

    def remove_action(self, action_name):
        del self.actions[action_name]

    def __str__(self):
        return self.name + ": " + self.description