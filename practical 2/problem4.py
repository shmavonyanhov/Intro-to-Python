import argparse

p = argparse.ArgumentParser()

p.add_argument("--age")

a=p.parse_args()

print("Happy B-Day, you are already %s years old!!" % a.age)
