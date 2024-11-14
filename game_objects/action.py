class Action:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def use(self, level):
        if self.type == 'print':
            print(self.value)
        elif self.type == 'move':
            level.move(self.value)
            return

    def __str__(self):
        return f"{self.name}: {self.type} - {self.value}"