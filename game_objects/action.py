class Action:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def use(self, level, player) -> str:
        if self.type == 'print':
            return self.value
        elif self.type == 'move':
            return f"You moved to {self.value}"

    def __str__(self):
        return f"{self.name}: {self.type} - {self.value}"