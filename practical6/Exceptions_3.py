my_list=["a",0,2]

for i in my_list:
    print("The entry is: ",i)
    try:
         print("the reciprocal of ", i , " is ",1/i)
    except Exception as e:
        print("Oops!",e)