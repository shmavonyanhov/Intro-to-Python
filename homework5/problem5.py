def my_range(n):
    for i in range(n+1):
        yield i
    yield "there are no values left"

a=my_range(3)

print(list(a))