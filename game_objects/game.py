# Import necessary modules
from game_objects.action import Action
from game_objects.level import Level
from game_objects.location import Location

# Define levels data structure
game_data = {
    0: [
        {
            "name": "Outside",
            "description": "You stand before the Epi Drost building about to go to school, but something feels wrong.",
            "actions": [
                {
                    "name": "Enter school",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        }, {
            "name": "Entrance",
            "description": "Something funny",
            "actions": [
                {
                    "name": "Go to the reception",
                    "type": "move",
                    "value": "Reception"
                }, {
                    "name": "Go to the toilets",
                    "type": "move",
                    "value": "Toilets"
                }, {
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
                }, {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        }, {
            "name": "Toilets",
            "description": "Description",
            "actions": [
                {
                    "name": "Check sink",
                    "type": "print",
                    "value": "You drank some and it made you feel refreshed."
                }, {
                    "name": "Check toilet",
                    "type": "print",
                    "value": "todo maybe give the player something?"
                }, {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        }, {
            "name": "Reception",
            "description": "As you walk up to there the receptionist starts screaming that there are demons in the building. If only there was someone to kill them.",
            "actions": [
                {
                    "name": "Pickup weapon",
                    "type": "print",
                    "value": "Give the player a weapon."
                }, {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        }
    ],
    5: [
        {
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
                }
            ]
        }, {
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
            "name": "Office",
            "description": "Its quiet here",
            "demon": "Peter",
            "actions": [
                {
                    "name": "Enter igloo",
                    "type": "move",
                    "value": "Igloo"
                }, {
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
    ],
    9: [
        {
            "name": "Roof",
            "description": "The wind blows through your hair.",
            "actions": [

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
