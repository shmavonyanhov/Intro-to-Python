def iter_num(n):
    for i in range(1,n):
        yield i


print(next(iter_num(8)))