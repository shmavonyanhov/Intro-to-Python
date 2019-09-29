class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def getName(self):
        print("My name is %s" % self.name)

    def getLegs(self):
        print("I have %s legs" % self.legs)


class Exnik(Animal):
    def __init__(self):
        Animal.__init__(self, "Exnik", 4)


Bambi = Exnik()

Bambi.getLegs()
Bambi.getName()
