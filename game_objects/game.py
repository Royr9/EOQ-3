# Import necessary modules
from game_objects.action import Action
from game_objects.level import Level
from game_objects.location import Location

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
        },
        {
            "name": "Entrance",
            "description": "As you walk in you see the receptionist is trying to get your attention. Maybe you should check it out.",
            "actions": [
                {
                    "name": "Go to the reception",
                    "type": "move",
                    "value": "Reception"
                },
                {
                    "name": "Go to the toilets",
                    "type": "move",
                    "value": "Toilets"
                },
                {
                    "name": "Use escalator",
                    "type": "print",
                    "value": "The escalator is broken. Again..."
                },
                {
                    "name": "Use stairs",
                    "type": "print",
                    "value": "The stairs are broken. Not sure how that happened"
                },
                {
                    "name": "Use elevator",
                    "type": "move",
                    "value": "Elevator"
                }
            ]
        },
        {
            "name": "Elevator",
            "description": "Before you stands the mighty demon Tibor",
            "demon": "Tibor",
            "actions": [
                {
                    "name": "Fight Tibor",
                    "type": "fight",
                    "value": ""
                },
                {
                    "name": "Use elevator",
                    "type": "next_level",
                    "value": ""
                },
                {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        },
        {
            "name": "Toilets",
            "description": "Description",
            "actions": [
                {
                    "name": "Check sink",
                    "type": "print",
                    "value": "You drank some and it made you feel refreshed."
                },
                {
                    "name": "Check toilet",
                    "type": "give_spell",
                    "value": ""
                },
                {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        },
        {
            "name": "Reception",
            "description": "As you walk up to there the receptionist starts screaming that there are demons in the building. If only there was someone to kill them.",
            "actions": [
                {
                    "name": "Learn spell",
                    "type": "give_spell",
                    "value": ""
                },
                {
                    "name": "Go back",
                    "type": "move",
                    "value": "Entrance"
                }
            ]
        }
    ],
    1: [
        {
            "name": "Elevator",
            "description": "Floor 1: The Canteen Demon",
            "actions": [
                {
                    "name": "Use elevator",
                    "type": "next_level",
                    "value": ""
                },
                {
                    "name": "Enter hallway",
                    "type": "move",
                    "value": "Hallway"
                }
            ]
        },
        {
            "name": "Hallway",
            "description": "The hallway is long and filled with students",
            "actions": [
                {
                    "name": "Enter elevator",
                    "type": "move",
                    "value": "Elevator"
                },
                {
                    "name": "Enter canteen",
                    "type": "move",
                    "value": "Canteen"
                }
            ]
        },
        {
            "name": "Canteen",
            "description": "In front of you stands Timothy. He has eaten everything there including the lunch ladies, Except the one he holds hostage to make him more food.",
            "demon": "Timothy",
            "actions": [
                {
                    "name": "Pickup Sandwich",
                    "type": "give_spell",
                    "value": ""
                },
                {
                    "name": "Fight Timothy",
                    "type": "fight",
                    "value": ""
                },
                {
                    "name": "Enter hallway",
                    "type": "move",
                    "value": "Hallway"
                }
            ]
        }
    ],
    5: [
        {
            "name": "Elevator",
            "description": "Floor 5: Panic in the Office",
            "actions": [
                {
                    "name": "Use elevator",
                    "type": "next_level",
                    "value": ""
                },
                {
                    "name": "Enter hallway",
                    "type": "move",
                    "value": "Hallway"
                },
                {
                    "name": "Enter igloo",
                    "type": "move",
                    "value": "Igloo"
                }
            ]
        },
        {
            "name": "Hallway",
            "description": "The hallway is long and filled with students",
            "actions": [
                {
                    "name": "Enter toilet",
                    "type": "print",
                    "value": "The janitor blocks the door"
                },
                {
                    "name": "Enter office",
                    "type": "move",
                    "value": "Office"
                },
                {
                    "name": "Enter elevator",
                    "type": "move",
                    "value": "Elevator"
                }
            ]
        },
        {
            "name": "Igloo",
            "description": "You feel comfortable here",
            "actions": [
                {
                    "name": "Get coffee",
                    "type": "give_spell",
                    "value": ""
                },
                {
                    "name": "Enter elevator",
                    "type": "move",
                    "value": "Elevator"
                },
                {
                    "name": "Enter office",
                    "type": "move",
                    "value": "Office"
                }
            ]
        },
        {
            "name": "Office",
            "description": "As you enter you see Olivier playing open rct 2. It would not be wise to disturb him.",
            "demon": "Olivier",
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
                },
                {
                    "name": "Disturb olivier",
                    "type": "fight",
                    "value": ""
                }
            ]
        }
    ],
    9: [
        {
            "name": "Elevator",
            "description": "Floor 9: The Final Battle.",
            "actions": [
                {
                    "name": "Enter roof terrace",
                    "type": "move",
                    "value": "Roof"
                },
                {
                    "name": "Drink liquid courage",
                    "type": "give_spell",
                    "value": ""
                }
            ]
        },
        {
            "name": "Roof",
            "description": "The wind blows through your hair. And you know the time has come, You need to slay the mighty demon Frank.",
            "demon": "Frank",
            "actions": [
                {
                    "name": "Fight Frank",
                    "type": "fight",
                    "value": ""
                }
            ]
        }
    ]
}


# Define levels data structure


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

    def get_level(self):
        return self.current_level
