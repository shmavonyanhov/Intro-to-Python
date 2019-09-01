import argparse

list2 = [0, 10, 2, 100, 300, 2]

p = argparse.ArgumentParser()

p.add_argument("value", type=int)
a = p.parse_args()

print(list2.count(a.value))
