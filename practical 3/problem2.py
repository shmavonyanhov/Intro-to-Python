import sys

list1 = ["hello", 1, True]
print(list1)
list2 = list1 + sys.argv[1:]
print(list2)
