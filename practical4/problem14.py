list1=["al","abc","xyz","as","aba","1221"]
list2=[i for i in list1 if ((len(i)>1) and (i[0]==i[-1]))]
print(list2.__len__())

