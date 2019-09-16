def power(max):
    for i in range(max):
        yield 2**i

print(next(power(3)))