from abc import ABC, abstractmethod
from demon_attacks import attacks
import random


class Demon(ABC):
    def __init__(self):
        self.health = 100
        self.attacks = attacks

    def get_damage(self):
        return self.health

    @abstractmethod
    def set_damage(self, damage):
        pass

    @abstractmethod
    def attack(self):
        pass


class Frank(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/frank.jpg'

    def set_damage(self, damage):
        self.health -= damage * 0.3

    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["damage"] >= 30 and attack[1]["Damage"] <= 35:
                break
        return attack
            

class Tibor(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/tibor.jpg'
        self.custom_attacks = {
            "Insults you in Swedish": {
                "Message": "Din dator är en potatis för helvete.", "Damage": 18
                }
            }

    def set_damage(self, damage):
        self.health -= damage * 0.8

    def attack(self):
        attack_type = random.choice([attacks.items(), self.custom_attacks.items()])
        while True:
            attack = random.choice(list(attack_type))
            if attack[1]["Damage"] >= 15 and attack[1]["Damage"] <= 20:
                break
        return attack


class Peter(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/peter.jpg'

    def set_damage(self, damage):
        self.health -= damage * 0.8

    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["Damage"] >= 20 and attack[1]["Damage"] <= 25:
                break
        return attack


class Olivier(Demon):
    def __init__(self):
        super().__init__()
        self.image = '/images/demons/olivier.jpg'

    def set_damage(self, damage):
        self.health -= damage * 0.7

    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["Damage"] >= 25 and attack[1]["Damage"] <= 30:
                break
        return attack

demon = Tibor()
demon.attack()