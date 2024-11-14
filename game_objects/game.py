# Import necessary modules
from game_objects.level import Level
from game_objects.location import Location
from game_objects.action import Action

# Define levels data structure
game_data = {
    0: [
        {
            "name": "Entrance",
            "description": "Something funny",
            "actions": [
                {
                    "name": "Use escalator",
                    "type": "print",
                    "value": "The escalator is broken. Again..."
                }, {
                    "name": "Use stairs",
                    "type": "print",
                    "value": "The stairs are broken. Not sure how that happened"
                }, {
                    "name": "Use elevator",
                    "type": "move",
                    "value": "Elevator"
                }
            ]
        }, {
            "name": "Elevator",
            "description": "Before you stands the mighty demon Tibor",
            "demon": "Tibor",
            "actions": [
                {
                    "name": "Use elevator",
                    "type": "next_level",
                    "value": ""
                }
            ]
        }
    ],
    1: [
        {
            "name": "Igloo",
            "description": "You feel comfortable here",
            "actions": [
                {
                    "name": "Get coffee",
                    "type": "print",
                    "value": "The coffee machine is out of water"
                }, {
                    "name": "Enter hallway",
                    "type": "move",
                    "value": "Hallway",
                }, {
                    "name": "Enter office",
                    "type": "move",
                    "value": "Office",
                }
            ]
        }, {
            "name": "Hallway",
            "description": "The hallway is long and filled with students",
            "actions": [
                {
                    "name": "Enter toilet",
                    "type": "print",
                    "value": "The janitor blocks the door"
                }, {
                    "name": "Enter office",
                    "type": "move",
                    "value": "Office",
                }, {
                    "name": "Enter igloo",
                    "type": "move",
                    "value": "Igloo",
                }            ]
        }, {
            "name": "Office",
            "description": "Its quiet here",
            "demon": "Peter",
            "actions": [
                {
                    "name": "Enter igloo",
                    "type": "move",
                    "value": "Igloo"
                },
                {
                    "name": "Enter hallway",
                    "type": "move",
                    "value": "Hallway"
                }, {
                    "name": "Talk to peter",
                    "type": "print",
                    "value": "Peter says a terrible pun, Peter is happy now."
                }
            ]
        }
    ]
}

def load():
    """
    Load level data into Level objects.

    :return: A list of Level objects representing all levels
    """
    level_list = []

    for level, locations_data in game_data.items():
        locations = {}
        starting_location = None

        for location in locations_data:
            name = location["name"]
            description = location["description"]
            actions = {}

            if starting_location is None:
                starting_location = name


            if "demon" in location:
                demon = location["demon"]
            else:
                demon = None

            for action in location["actions"]:
                actions[action["name"]] = Action(action["name"], action["type"], action["value"])

            locations[name] = (Location(name, description, actions, demon))
        level_list.append(Level(level, starting_location, locations))

    return Game(level_list)

class Game:
    def __init__(self, levels):
        self.levels = levels
        self.current_level = 0

    def get_current_level(self):
        return self.levels[self.current_level]

    def next_level(self):
        self.current_level += 1