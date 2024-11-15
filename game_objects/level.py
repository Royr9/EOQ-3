class Level:
    def __init__(self, level, starting_location, locations):
        """
        Initialize a Level object.

        :param level: The level number
        :param starting_location: The name of the starting location
        :param locations: A dictionary of all locations in this level
        """
        self.level = level
        self.current_location = starting_location
        self.locations = locations
        self.is_killed = False

    def get_current_location(self):
        """
        Get the current location object.

        :return: The Location object representing the current location
        """
        return self.locations[self.current_location]

    def get_location_names(self):
        """
        Get a list of all location names in this level.

        :return: List of location names
        """
        return list(self.locations.keys())

    def add_location(self, location):
        """
        Add a new location to the level.

        :param location: The Location object to be added
        """
        self.locations.append(location)

    def remove_location(self, location):
        """
        Remove a location from the level.

        :param location: The Location object to be removed
        """
        self.locations.remove(location)

    def move(self, location):
        """
        Move to a different location within the same level.

        :param location: The name of the new location to move to
        """
        self.current_location = location

    def is_demon_killed(self):
        return self.is_killed

    def kill_demon(self):
        self.is_killed = True





