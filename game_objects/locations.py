class Location:
    def __init__(self, name, description, actions=None):
        self.name = name
        self.description = description
        self.actions = actions if actions is not None else {}

    def add_action(self, action_name, action):
        self.actions[action_name] = action

    def remove_action(self, action_name):
        del self.actions[action_name]

    def describe(self):
        print(self.description)


class Floor:
    def __init__(self, level_number, locations=None):
        self.level_number = level_number
        self.locations = locations if locations is not None else []

    def add_location(self, location):
        self.locations.append(location)

    def remove_location(self, location):
        self.locations.remove(location)

    def describe(self):
        print(f"Floor {self.level_number} has the following locations:")
        for location in self.locations:
            print(f"- {location.name}: {location.description}")
