class Location:
    """
    Represents a location in a 2D coordinate system.
    """

    def __init__(self, starting_x=0, starting_y=0):
        """
        Initializes a Location object with starting coordinates.

        Args:
            starting_x (int): The initial x-coordinate (default is 0).
            starting_y (int): The initial y-coordinate (default is 0).
        """
        self.x = starting_x
        self.y = starting_y

    def get_location(self):
        """
        Returns the current coordinates as a tuple.

        Returns:
            tuple: A tuple containing the current x and y values.
        """
        return self.x, self.y

    def move_left(self, amount=1):
        """
        Moves the location left by a specified amount.

        Args:
            amount (int): The distance to move left (default is 1).
        """
        self.x -= amount

    def move_right(self, amount=1):
        """
        Moves the location right by a specified amount.

        Args:
            amount (int): The distance to move right (default is 1).
        """
        self.x += amount

    def move_up(self, amount=1):
        """
        Moves the location up by a specified amount.

        Args:
            amount (int): The distance to move up (default is 1).
        """
        self.y += amount

    def move_down(self, amount=1):
        """
        Moves the location down by a specified amount.

        Args:
            amount (int): The distance to move down (default is 1).
        """
        self.y -= amount

    def __str__(self):
        """
        Returns a string representation of the location.

        Returns:
            str: A formatted string containing the current x and y values.
        """
        return f'{self.x}, {self.y}'