import argparse

given = "This is a sample text"

p = argparse.ArgumentParser()

p.add_argument("first", help="first word", type=str)
p.add_argument("second", help="second word", type=str)

a = p.parse_args()

print("The given text: ", given)
print("First word: ", a.first)
print("Second word: ", a.second)
print("Output string: ", given.replace(a.first, a.second))
