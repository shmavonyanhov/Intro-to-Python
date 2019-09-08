name = input("name: ")
age = int(input("age: "))
password = input("password: ")

if name == "Batman":
    print("Welcome Mr. Batman!")
elif age < 16:
    print("Dear", name, ", you are too young to register")
elif ("*" not in password) and ("&" not in password):
    print("Please enter a different password")
