class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("I can move")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Dog")

    def move(self):
        print("I can run really fast")


Puppy = Dog()

Puppy.move()
