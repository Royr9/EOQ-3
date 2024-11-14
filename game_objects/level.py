# Import necessary modules
from game_objects.location import Location
from game_objects.action import Action

# Define levels data structure
levels = {
    0: [
        {
            "name": "Entrance",
            "description": "Something funny",
            "actions": [
                {
                    "name": "use escalator",
                    "type": "print",
                    "value": "The escalator is broken. Again..."
                }
            ]
        }
    ],
    1: [
        {
            "name": "igloo",
            "description": "You feel comfortable here",
            "actions": [
                {
                    "name": "get coffee",
                    "type": "print",
                    "value": "The coffee machine is out of water"
                }, {
                    "name": "enter hallway",
                    "type": "move",
                    "value": "hallway",
                }, {
                    "name": "enter office",
                    "type": "move",
                    "value": "office",
                }
            ]
        }, {
            "name": "hallway",
            "description": "The hallway is long and filled with students",
            "actions": [
                {
                    "name": "enter toilet",
                    "type": "print",
                    "value": "The janitor blocks the door"
                }, {
                    "name": "enter office",
                    "type": "move",
                    "value": "office",
                }, {
                    "name": "enter igloo",
                    "type": "move",
                    "value": "igloo",
                }            ]
        }, {
            "name": "office",
            "description": "Its quiet here",
            "actions": [
                {
                    "name": "enter igloo",
                    "type": "move",
                    "value": "igloo"
                },
                {
                    "name": "enter hallway",
                    "type": "move",
                    "value": "hallway"
                }, {
                    "name": "talk to peter",
                    "type": "print",
                    "value": "Peter says a terrible pun, Peter is happy now."
                }
            ]
        }
    ]
}


class Level:
    def __init__(self, level, starting_location, locations):
        """
        Initialize a Level object.

        :param level: The level number
        :param starting_location: The name of the starting location
        :param locations: A dictionary of all locations in this level
        """
        self.level = level
        self.current_location = starting_location
        self.locations = locations

    def get_current_location(self):
        """
        Get the current location object.

        :return: The Location object representing the current location
        """
        return self.locations[self.current_location]

    def get_location_names(self):
        """
        Get a list of all location names in this level.

        :return: List of location names
        """
        return list(self.locations.keys())

    def add_location(self, location):
        """
        Add a new location to the level.

        :param location: The Location object to be added
        """
        self.locations.append(location)

    def remove_location(self, location):
        """
        Remove a location from the level.

        :param location: The Location object to be removed
        """
        self.locations.remove(location)

    def move(self, location):
        """
        Move to a different location within the same level.

        :param location: The name of the new location to move to
        """
        self.current_location = location


def load():
    """
    Load level data into Level objects.

    :return: A list of Level objects representing all levels
    """
    level_list = []

    for level, locations_data in levels.items():
        locations = {}
        starting_location = None

        for location in locations_data:
            name = location["name"]
            description = location["description"]
            actions = {}

            if starting_location is None:
                starting_location = name

            for action in location["actions"]:
                actions[action["name"]] = Action(action["name"], action["type"], action["value"])

            locations[name] = (Location(name, description, actions))
        level_list.append(Level(level, starting_location, locations))

    return level_list
