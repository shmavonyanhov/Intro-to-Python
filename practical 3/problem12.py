import argparse

p = argparse.ArgumentParser()

p.add_argument("value", type=int)
a = p.parse_args()

set3 = {3, 10, 2, 100, 300, 2}

l = list(set3)

l.sort()

minimum = l[0]
maximum = l[-1]

print(a.value > minimum & a.value < maximum)
