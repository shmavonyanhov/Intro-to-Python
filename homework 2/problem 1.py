import argparse
import datetime

p = argparse.ArgumentParser()

p.add_argument("--num_y", help="amount of years", type=int)
p.add_argument("--num_d", help="amount of days", type=int)

now = datetime.datetime.now()
final = datetime.datetime

print("Current date: ", now)

arg = p.parse_args()

if arg.num_y:
    print("Given years: ", arg.num_y)
    final = datetime.datetime(now.year + arg.num_y, now.month, now.day, now.hour, now.minute, now.second,
                              now.microsecond)

# timedelta does not take the year as an argument. Please discuss this !!!

else:
    print("Given years: not given")
    final = now

if arg.num_d:
    print("Given days: ", arg.num_d)
    final = final + datetime.timedelta(days=arg.num_d)
else:
    print("Given days: not given")

print("Final date: ", final)
