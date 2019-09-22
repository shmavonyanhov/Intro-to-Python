class Police_car:
    tax_value = 0.2

    def __init__(self, owner, price, pass_code):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code

    def tax(self):
        return self.tax_value * self.price

    def greeting(self):
        if self.__pass_code == "admin":
            print("Welcome to your car " + self.owner)
    def set_pass_code(self,pass_code):
        self.__pass_code=pass_code

    def get_pass_code(self):
        return self.__pass_code


car1=Police_car("Garnik",4500,"admin")

print(car1.tax())

car1.greeting()


car1.set_pass_code("ad")
car1.greeting()
print(car1.get_pass_code())



