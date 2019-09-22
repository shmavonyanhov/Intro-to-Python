class MyException(Exception):
    pass

username=input()

try:
   if username=="Rambo":
       raise MyException("Rambo is an invalid username")
except Exception as e:
    print(e)
else:
    print("Welcome, ",username)

print("Ok")

