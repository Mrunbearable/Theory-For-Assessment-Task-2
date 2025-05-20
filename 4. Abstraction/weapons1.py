from abc import ABC, abstractmethod


class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    @abstractmethod
    def get_stats(self):
        pass
        
    def set_stats(self):
        pass

class Sword:
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Melee-xType: {self.melee_type}")
        