from abc import ABC, abstractmethod
from demon_attacks import attacks

class Demon(ABC):
    def __init__(self):
        self.health = 100
        self.image = ''
        self.attacks = {}


    @abstractmethod
    def set_damage(self):
        pass

    def get_damage(self):
        return self.health


class Frank(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/frank.jpg'
        self.attacks = attacks["frank"]

    def set_damage(self, damage):
        self.health -= damage - 70


class Tibor(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/tibor.jpg'

    def set_damage(self, damage):
        self.health -= damage - 20


class Peter(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/peter.jpg'

    def set_damage(self, damage):
        self.health -= damage - 15


class Olivier(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/olivier.jpg'

    def set_damage(self, damage):
        self.health -= damage - 30