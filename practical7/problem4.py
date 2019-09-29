class Model:
    def __init__(self, name):
        self.name = name

    def printModel(self):
        print("The model of the vehicle is %s" % self.name)


class Color:
    def __init__(self, color):
        self.color = color

    def printColor(self):
        print("The color of the vehicle is %s" % self.color)


class Car(Model, Color):
    def __init__(self, model, color):
        Model.__init__(self, model)
        Color.__init__(self, color)


BMW = Car("BMW", "red")

BMW.printModel()
BMW.printColor()
