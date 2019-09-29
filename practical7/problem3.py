import abc


class Bird(abc.ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abc.abstractmethod
    def fly(self):
        pass


class Hav(Bird):
    def __init__(self, name, weight):
        Bird.__init__(self, name, weight)

    def fly(self):
        print("I believe I can fly")


havik = Hav("havik", 2)

havik.fly()
