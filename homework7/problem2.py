class My_Time:
    def __init__(self,time):
        self.time=time

    def printTime(self):
        print("The current time is %s" % self.time)


class My_Date:
    def __init__(self,date):
        self.date=date

    def printDate(self):
        print("The current date is %s" % self.date)


class Date_Time(My_Date,My_Time):
    def __init__(self,d,t):
        My_Date.__init__(self,d)
        My_Time.__init__(self,t)


a=Date_Time("12PM","13.03.2013")

a.printTime()
a.printDate()