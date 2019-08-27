import argparse

p=argparse.ArgumentParser()
p.add_argument("str")
a=p.parse_args()
print("The given string:"+a.str)
print("All lowercase:"+a.str.lower())
print("All uppercase:"+a.str.upper())