d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7]}

grade=d["grades"]

avg=sum(grade)/len(grade)

print(avg)

if avg>7:
    print("Good job")
else:
    print("You need to work more")