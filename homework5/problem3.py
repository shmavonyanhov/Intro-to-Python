def dec(f):
    def wrap():
        return "Before function call\n"+f()+"\nAfter the function call"
    return wrap


@dec
def func():
    return "Inside the function"



print(func())
