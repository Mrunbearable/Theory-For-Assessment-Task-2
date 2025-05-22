class weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage
    
    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")

class sword(weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage, damage_category)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage * 3}")
        print(f"Damage: {self.damage_catergory}")

class bow(weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage, damage_category)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage * 2}")
        print(f"Damage: {self.damage_catergory}")

class long_bow(bow):
    def __init__(self, name, category, damage, damage_category, range_of_bow):
        super().__init__(name, category, damage, damage_category, range_of_bow)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage * 2}")
        print(f"Damage: {self.damage_catergory}")
        print(f"Range: {self.range_of_bow}")

class short_bow(bow):
    def __init__(self, name, category, damage, damage_category, range_of_bow):
        super().__init__(name, category, damage, damage_category, range_of_bow)

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage * 2}")
        print(f"Damage: {self.damage_catergory}")
        print(f"Range: {self.range_of_bow}")