def unique(my_list):
    res=[]
    for i in my_list:
        if my_list.count(i)==1:
            res.append(i)
    return res

mylist=[2,5,6,8,9,98,9,8,5,1,2,3]


print(unique(mylist))