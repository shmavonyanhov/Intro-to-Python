import argparse
p=argparse.ArgumentParser()
p.add_argument("name")
a=p.parse_args()
print("Welcome %s!" % a.name)