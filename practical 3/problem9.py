import argparse

p = argparse.ArgumentParser()

p.add_argument("value", type=int)
a = p.parse_args()

set2 = {2, 8, "hi"}
print(set2)

set2.remove(a.value)

print(set2)

