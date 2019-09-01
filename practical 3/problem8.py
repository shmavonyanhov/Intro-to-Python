import argparse

p = argparse.ArgumentParser()

p.add_argument("value", type=int)
a = p.parse_args()

set1 = {2, 8, "hi"}

print(set1)

set1.add(a.value)

print(set1)
