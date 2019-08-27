import datetime
import time,calendar


dt=datetime.datetime.today()

#2)

print("date and time= ",dt)
print("year=",dt.year)
print("month=",dt.month)
print("day of a week=",dt.weekday())

#3)
delta=datetime.timedelta(days=5)


newdatetime=delta+dt
print(dt)
print(delta)
print("new date:",newdatetime.date(),"hour:",newdatetime.hour)
sec5plus=datetime.timedelta(seconds=5)
fiveseclater=dt+sec5plus
print(fiveseclater)

