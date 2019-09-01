import datetime
import time
import calendar

B_Day = datetime.date(1993, 7, 15)

print("date of birth: ", B_Day)
print("year of birth: ", B_Day.year)
print("month of birth: ", B_Day.month)
print("day of birth: ", B_Day.day)
week = calendar.weekheader(3).split()
print("day of week: ", week[B_Day.weekday()])
tday = datetime.date.today()
if tday.month > B_Day.month:
    next_B_Day = datetime.date(tday.year + 1, B_Day.month, B_Day.day)
    print("days until next birthday: ", (next_B_Day - tday).days)
elif tday.month < B_Day.month:
    next_B_Day = datetime.date(tday.year, B_Day.month, B_Day.day)
    print("days until next birthday: ", (next_B_Day - tday).days)
elif tday.day < B_Day.day:
    next_B_Day = datetime.date(tday.year, B_Day.month, B_Day.day)
    print("days until next birthday: ", (next_B_Day - tday).days)
elif tday.day > B_Day.day:
    next_B_Day = datetime.date(tday.year + 1, B_Day.month, B_Day.day)
    print("days until next birthday: ", (next_B_Day - tday).days)
else:
    print("Happy B-Day!!!")
print(calendar.month(2017, 5))
yesterday = datetime.datetime.today() + datetime.timedelta(days=-1)
print(yesterday)
print(yesterday + datetime.timedelta(days=2))
print(yesterday + datetime.timedelta(days=-3))
