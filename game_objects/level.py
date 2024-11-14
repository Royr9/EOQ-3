from location import Location
from action import Action

levels = {
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
                    "name": "enter Hallway",
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
                }
            ]
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
        self.level = level
        self.current_location = starting_location
        self.locations = locations

    def get_current_location(self):
        return self.locations[self.current_location]

    def get_location_names(self):
        return list(self.locations.keys())

    def move(self, location):
        self.current_location = location

def load():
    level_list = []

    for level in levels:
        locations = {}
        starting_location = None

        for location in levels[level]:
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