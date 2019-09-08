n_shoes=int(input("number of shoes: "))

amount=n_shoes*100

if amount>1000:
    print("You get a discount.")
else:
    print("You don't get a discount.")