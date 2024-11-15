from abc import ABC, abstractmethod
from game_objects.demon_attacks import attacks
import random
import math

class Demon(ABC):
    def __init__(self, name):
        self.health = 100
        self.attacks = attacks
        self.name = name

    def get_damage(self):
        return self.health

    @abstractmethod
    def set_damage(self, damage) -> int:
        pass

    @abstractmethod
    def attack(self):
        pass


class Frank(Demon):
    def __init__(self):
        name = "Frank"
        super().__init__(name)
        self.image = 'demons/elf_frank.png'

    def set_damage(self, damage) -> int:
        dmg = math.floor(damage * 0.3)
        self.health -= dmg
        self.health = max(self.health, 0)
        if self.health <= 50:
            self.image = 'demons/frank.png'
        else:
            self.image = 'demons/elf_frank.png'
        return dmg

    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["Damage"] >= 30 and attack[1]["Damage"] <= 40:
                break
        return attack
            

class Tibor(Demon):
    def __init__(self):
        name = "Tibor"
        super().__init__(name)
        self.health = 80
        self.image = f'/demons/{name}.png'
        self.custom_attacks = {
            "Insults you in Swedish": {
                "Message": "Din dator är en potatis för helvete.", "Damage": 18
                }
            }
    
    def set_damage(self, damage) -> int:
        dmg = math.floor(damage * 0.8)
        self.health -= dmg
        self.health = max(self.health, 0)
        return dmg



    def attack(self):
        attack_type = random.choice([attacks.items(), self.custom_attacks.items()])
        while True:
            attack = random.choice(list(attack_type))
            if attack[1]["Damage"] >= 15 and attack[1]["Damage"] <= 20:
                break
        return attack


class Peter(Demon):
    def __init__(self):
        name = "Peter"
        super().__init__(name)
        self.image = f'/demons/{name}.png'
        self.health = 90
        
    def set_damage(self, damage) -> int:
        dmg = math.floor(damage * 0.7)
        self.health -= dmg
        self.health = max(self.health, 0)
        return dmg


    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["Damage"] >= 20 and attack[1]["Damage"] <= 25:
                break
        return attack


class Olivier(Demon):
    def __init__(self):
        name = "Olivier"
        super().__init__(name)
        self.image = f'/demons/{name}.png'

    def set_damage(self, damage) -> int:
        dmg = math.floor(damage * 0.5)
        self.health -= dmg
        self.health = max(self.health, 0)
        return dmg


    def attack(self):
        while True:
            attack = random.choice(list(attacks.items()))
            if attack[1]["Damage"] >= 15 and attack[1]["Damage"] <= 40:
                break
        return attack
    
class Timothy(Demon):
    def __init__(self):
        name = "Timothy"
        super().__init__(name)
        self.image = f'/demons/{name}.png'
        self.custom_attacks = {
            "Start of the weekend yell": {
                "Message": "DEAR STUDENTS I'M LEAVING BYYYEE!!!", "Damage": 27
                }
            }
        
    def set_damage(self, damage) -> int:
        dmg = math.floor(damage * 0.5)
        self.health -= dmg
        self.health = max(self.health, 0)
        return dmg


    def attack(self):
        attack_type = random.choice([attacks.items(), self.custom_attacks.items()])
        while True:
            attack = random.choice(list(attack_type))
            if attack[1]["Damage"] >= 25 and attack[1]["Damage"] <= 30:
                break
        return attack

def get_demon_by_name(name):
    match name:
        case "Frank":
            return Frank()
        case "Peter":
            return Peter()
        case "Olivier":
            return Olivier()
        case "Tibor":
            return Tibor()
        case "Timothy":
            return Timothy()
        case _:
            return print("demon doesnt exist")
