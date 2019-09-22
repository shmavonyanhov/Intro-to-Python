class Car:
    def __init__(self,model,color,max_speed):
        self.model=model
        self.color=color
        self.max_speed=max_speed
    def compareCar(self,car2):
        assert isinstance(car2,Car)
        if self.max_speed>car2.max_speed:
            print("%s is better than %s"%(self.model,car2.model))
        else:
            print("%s is better than %s" % (car2.model,self.model))




Mercedes=Car("Mercedes","Black",350)
BMW=Car("BMW","Blue",340)

Mercedes.compareCar(BMW)


