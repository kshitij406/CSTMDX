class Animal:
    def __init__(self, no_legs, color):
        self.no_legs = no_legs
        self.color =color
class Cat(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)
    def __str__(self):
        return f'Cat has {self.no_legs}, his color is: {self.color}'