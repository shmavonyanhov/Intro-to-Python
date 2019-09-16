list1=["Anna","Edgar"]
list2=["Eliza","Ani","Vardan"]

def dec(func):
    def wrapper(*args,**kwargs):
        global list1
        print(list1)
        list1=func(*args,**kwargs)
        print(list1)
    return wrapper


@dec
def add_values(l):
    return l+list2



add_values(list1)
