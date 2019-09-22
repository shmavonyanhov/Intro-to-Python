class Circle:
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
    def getDesc(self):
        print("A %s circle with radius %s."%(self.color,self.radius))


Red=Circle(20,"red")
Blue=Circle(10,"blue")

Red.getDesc()
Blue.getDesc()

