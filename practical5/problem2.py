def evens(mylist):
    count=0
    for i in mylist:
        if i%2==0:
            count+=1
    return count

my_list=[50,54,5,6,5,4,6,8,9,4,56,2,1,6,5,4,8]

print(evens(my_list))