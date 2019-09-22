def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error is detected")


print(div(8, 0))