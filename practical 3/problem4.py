import argparse

list4 = [0, 10, 2, 100, 300, 2]

p = argparse.ArgumentParser()

p.add_argument("value", type=int)
a = p.parse_args()

list4.remove(a.value)

print(list4)
