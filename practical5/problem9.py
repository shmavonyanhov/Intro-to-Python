def low(func):
    def wrapper(*args,**kwargs):
        string=func(*args,**kwargs)
        return string[0]+string.lower()[1:]
    return wrapper


def add(func):
    def wrapper(*args,**kwargs):
        string=func(*args,**kwargs)
        return string+"!!! Welcome to the party"
    return wrapper



@add
@low
def hi_everyone():
    return "HI EVERYONE"


print(hi_everyone())
