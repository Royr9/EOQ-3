import random

# A dictionary to store the stat of our game, this can be extended to include health, inventory, xp, whatever you like!
game_state = {
    "current_location": "igloo"
}


# Action to move to a different location
def move(new_location):
    print(f"You go from {game_state["current_location"]} to {new_location}")
    game_state["current_location"] = new_location
    print(locations[new_location]["description"])


# Actions can be as interactive/complex as you like:
def rubiks():
    print("You try to complete the rubiks cube...")
    while True:
        if random.randint(1, 6) < 3:
            print("In a pure stroke of luck you complete the rubiks cube, everyone claps!")
            return
        print("You try a few moves but the rubiks cube is now looking worse...")

        answer = input("Would you like to keep trying? [y/n]\n?> ")
        if answer == "n":
            return


def go_to_hallway():
    move("hallway")


def go_to_office():
    move("office")


# The dictionary with locations, the "current_location" variable maps to an item in this dict.
locations = {
    "igloo": {
        "description": "You feel comfortable here", # The description is shown before you enter a location
        "actions": {
            "get coffee": "The coffee machine is out of water",
            "solve rubiks": rubiks, # We can pass the function as a variable to call it later, in this case the rubiks() function is called when the user enters "solve rubiks" as an action.
            "leave igloo": go_to_hallway,
            "enter office": go_to_office,
        }
    },
    "hallway": {
        "description": "The hallway is long and filled with students",
        "actions": {
            "enter toilet": "The janitor blocks the door",
            "enter office": go_to_office,
        }
    },
    "office": {
        "description": "Its quiet here",
        "actions": {
            "leave office": lambda: move("hallway"), # Instead of making functions to go to each location, we can create an inline (lambda) function. This does the same as the go_to_hallway function. This creates a function which, when called, calls move with the "hallway" parameter.
            "enter igloo": lambda: move("igloo"),
            "talk to peter": "Peter says a terrible pun, Peter is happy now",
            "talk to tibor": "Tibor säger något svenskt",
        }
    }
}


def visit(location):
    print("What would you like to do?")
    for key in location["actions"]:
        print(f"- {key}")

    action = input("?> ")

    if action == "exit":
        exit()

    print("\n---------------------------------------")

    if action in location["actions"]:
        data = location["actions"][action]
        if isinstance(data, str):
            print(data)
        else:
            data()
    else:
        print("You can't do that here.")

    print("---------------------------------------\n")


def main():
    print("\n---------------------------------------")
    print("You wake up in the igloo")
    print(locations[game_state["current_location"]]["description"])
    print("---------------------------------------\n")

    while True:
        visit(locations[game_state["current_location"]])


main()
