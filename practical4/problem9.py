correct_num=5

for i in range(10):
    guess=int(input("your guess: "))
    if guess==correct_num:
        print("That was a good guess")
        break

