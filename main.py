from game_objects.player import Player
from game_objects.locations import Location, Floor

def main():
    # Initialize floor and locations
    floor_0 = Floor(0)
    starting_location = Location(name="Lobby", description="The building's lobby is quiet and deserted.", actions={"Hallway": "move", "Office": "move"})
    hallway = Location(name="Hallway", description="A long, narrow hallway with flickering lights.", actions={"Lobby": "move", "Office": "move"})
    office = Location(name="Office", description="A small office with a desk and a computer.", actions={"Lobby": "move", "Hallway": "move"})

    # Add locations to the floor
    floor_0.add_location(starting_location)
    floor_0.add_location(hallway)
    floor_0.add_location(office)
    
    # Create player in starting location
    player = Player(name="notDemonFrank", health=100, location=starting_location)
    
    # Simple game loop
    while True:
        # Describe the current location
        print("\n" + player.location.description)
        
        # Show available actions
        print("\nAvailable actions:")
        for action_name in player.location.actions:
            print(f"- {action_name}")

        # Get player choice
        choice = input("\nWhere do you want to go? ").strip()

        # Move to the chosen location if valid
        if choice in player.location.actions:
            new_location_name = choice
            new_location = next((loc for loc in floor_0.locations if loc.name == new_location_name), None)
            if new_location:
                player.location = new_location
            else:
                print("Invalid location. Try again.")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
