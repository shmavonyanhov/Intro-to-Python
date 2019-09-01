import argparse

p = argparse.ArgumentParser()

p.add_argument("str", help="odd length string, longer than 7", type=str)

arg = p.parse_args()
length = len(arg.str)
A = length % 2 == 0
B = length < 7

if A & B:
    print("length is even and your string is too short")
elif B:
    print("your string is too short")
elif A:
    print("length is even")
else:
    print("The old string: ", arg.str)
    print("Middle 3 characters: ", arg.str[length // 2 - 1:length // 2 + 2])
    print("The new string: ",
          arg.str[:length // 2 - 1:] + arg.str[length // 2 - 1:length // 2 + 2].upper() + arg.str[length // 2 + 2:])
