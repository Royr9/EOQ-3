from game_objects.player import Player
from game_objects.level import *
from game_objects.location import Location
from game_objects.action import Action

def main():
    # Initialize floor and locations
    levels = load()

    level = levels[0]
    
    # Create player in starting location
    player = Player(name="notDemonFrank", health=100)
    
    # Simple game loop
    while True:
        # Describe the current location
        location = level.get_current_location()
        print("\n" + location.name)
        
        # Show available actions
        print("\nAvailable actions:")
        for action_name in location.get_action_names():
            print(f"- {action_name}")

        # Get player choice
        choice = input("\nWhere do you want to go? ").strip()

        # Move to the chosen location if valid
        if choice in location.get_action_names():
            location.get_action(choice).use(level)

if __name__ == "__main__":
    main()
