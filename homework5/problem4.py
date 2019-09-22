def dec1(func):
    def wrap():
        return func()+", it is me"
    return wrap

def dec2(func):
    def wrap():
        return "<u> "+func()+" </u>"
    return wrap


@dec2
@dec1
def my_func():
    return "Hi"

print(my_func())

