a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3],a[5])


a_sorted=a.copy()
a_sorted.sort()
a_sorted.reverse()
print(a_sorted)

print(a_sorted[1:3])
print(a_sorted[2:6])

a_sorted.pop(3)
a_sorted.pop(2)

print(a_sorted)

b=["grapes", "Potatoes","tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted=b.copy()
b_sorted.sort()
print(b_sorted)

c=a[1:3]+b[4:6]
print(c)
