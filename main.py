from game_objects.player import Player
from game_objects.locations import Location
from game_objects.items import Item, Weapon, Armor, Key


def main():
    floor_1 = Location(starting_x=0, starting_y=0)
    player = Player(name="notDemonFrank", health=100, location=floor_1)
    print("you enter the building")
    print(player)


if __name__ == "__main__":
    main()
