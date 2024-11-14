class Location:
    def __init__(self, starting_x=0, starting_y=0):
        self.x = starting_x
        self.y = starting_y

    def get_location(self):
        return self.x, self.y

    def move_left(self, amount=1):
        self.x -= amount

    def move_right(self, amount=1):
        self.x += amount

    def move_up(self, amount=1):
        self.y += amount

    def move_down(self, amount=1):
        self.y -= amount

    def __str__(self):
        return f'{self.x}, {self.y}'
