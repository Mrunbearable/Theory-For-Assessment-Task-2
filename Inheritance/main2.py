class Animal:
    def sound(self):
        print("a sound")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        super().sound
        print(self.name)
        
class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        super().sound
        print(self.name)


