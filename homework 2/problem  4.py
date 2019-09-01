import argparse

p = argparse.ArgumentParser()

p.add_argument("text", help="given text", type=str)
a = p.parse_args()

print("The given string: ", a.text)
s = a.text.lower()
print("The USA count is: ", s.count("usa"))
f = a.text.replace("USA", "Armenia")
g = f.replace("usa", "Armenia")

print("The new string: ", g)
