import argparse

p=argparse.ArgumentParser()
p.add_argument("t")
p.add_argument("i")
p.add_argument("j")
l=p.parse_args()
i=int(l.i)
j=int(l.j)
print(l.t[i:j])