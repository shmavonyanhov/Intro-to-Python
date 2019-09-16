def list_els(list1):
    for i in list1:
        yield i


l1=[1,2,3,4,5,6]

l=list_els(l1)


print(next(l))
