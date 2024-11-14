levels = {
    1: [
        {
            "name": "igloo",
            "description": "You feel comfortable here",
            "actions": [
                {
                    "name": "get coffee",
                    "action": "The coffee machine is out of water"
                }, {
                    "name": "enter Hallway",
                    "action": lambda: move("hallway"),
                }, {
                    "name": "enter office",
                    "action": lambda: move("office"),
                }
            ]
        }, {
            "name": "hallway",
            "description": "The hallway is long and filled with students",
            "actions": [
                {
                    "name": "enter toilet",
                    "action": "The janitor blocks the door"
                }, {
                    "name": "enter office",
                    "action": lambda: move("office"),
                }
            ]
        }, {
            "name": "office",
            "description": "Its quiet here",
            "actions": [
                {
                    "name": "enter igloo",
                    "action": lambda: move("igloo")
                },
                {
                    "name": "enter hallway",
                    "action": lambda: move("hallway")
                }, {
                    "name": "talk to peter",
                    "action": "Peter says a terrible pun, Peter is happy now."
                }
            ]
        }
    ],
    2: [

    ]
}


def get_levels():
    return len(levels.keys())


def get_locations(level):
    locations = []
    for location in levels[level]:
        locations.append(location["name"])

    return locations


def visit(location):
    return


def move(name):
    return


if __name__ == '__main__':
    print(get_levels())
    print(get_locations(1))
