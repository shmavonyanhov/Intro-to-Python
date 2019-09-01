import argparse


dict1={8:10,"odd":3,"name":"Armen"}

print(dict1)
p = argparse.ArgumentParser()

p.add_argument("key1", type=str)
p.add_argument("value1", type=str)
p.add_argument("key2", type=str)
p.add_argument("value2", type=str)

a = p.parse_args()

dict1[a.key1]=a.value1
dict1[a.key2]=a.value2
print(dict1)