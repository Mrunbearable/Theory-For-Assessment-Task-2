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

class Sword(Weapon):
    def __init__(self, name, category, damage, range_type):
        super().__init__(name, category, damage)
        self.melee_type = range_type

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Melee-Type: {self.melee_type}")

    def set_stats(self, name, category, damage, melee_type):
        self.name = name
        self.category = category
        self.damage = damage
        self.melee_type = melee_type

sword = Sword("jit", "broadsword", 1, "Slashing" )
print(f"Sword name: {sword.name}")
print(f"Sword category: {sword.category}")
print(f"Sword damage: {sword.damage}")
print(f"Sword type: {sword.melee_type}")

class Bow(Weapon):
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Range-Type: {self.melee_type}")

    def set_stats(self, name, category, damage, melee_type):
        self.name = name
        self.category = category
        self.damage = damage
        self.melee_type = melee_type

bow = Bow("hello", "crossbow", 145, "Explosive" )
print(f"Bow name: {bow.name}")
print(f"Bow category: {bow.category}")
print(f"Bow damage: {bow.damage}")
print(f"Bow type: {bow.melee_type}")