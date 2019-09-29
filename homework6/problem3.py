import time


def dec(func):
    def wrap(*args,**kwargs):
        t=time.time()
        func(*args,**kwargs)
        print(time.time()-t)
    return wrap




class Person:
    def __init__(self, name, last_name, age, gender, student):
        assert isinstance(student, bool), "student can be True or False"
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password=None

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    @dec
    def Greeting(self, second_person):
        print("Welcome dear %s." % second_person.name)

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        return "My favourite number is %s" % num1

    def Read_file(self, filename):
        try:
            open("%s.txt" % filename)
        except FileNotFoundError:
            print("file is not found")
        except:
            print("Something went wrong")

Hovo=Person("Hovhannes","Shmavonyan",26,"Male",True)
Nikol=Person("Nikol","Pashinyan",42,"Male",False)

Hovo.set_password("pass")

print(Hovo.get_password())
Hovo.Goodbye()
Hovo.Greeting(Nikol)

Hovo.Read_file("file")