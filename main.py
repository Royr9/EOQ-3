from game_objects.player import Player
from game_objects.locations import Location


def main():
    floor_1 = Location(starting_x=0, starting_y=0)
    player = Player(name="player", health=100, location=Location)


if __name__ == "__main__":
    main()
